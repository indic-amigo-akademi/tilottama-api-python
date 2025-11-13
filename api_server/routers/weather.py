from fastapi import APIRouter
from fastapi.responses import JSONResponse
import os
import httpx
from api_server.models.openweather import WeatherUnits, parse_weather_data
from pydantic import BaseModel, Field
from typing import List, Optional

router = APIRouter(
    prefix="/weather",
    tags=["Weather"],
    responses={404: {"description": "Not found"}},
)
URL = "https://api.openweathermap.org/data/{apiVersion}/weather?appid={apiKey}&units={units}"
API_TOKEN = os.getenv("OPENWEATHER_API_KEY")
if not API_TOKEN:
    raise RuntimeError("OPENWEATHER_API_KEY environment variable not set.")

FETCH_FAILED = "Failed to fetch weather data!"
FETCH_SUCCESS = "Weather data fetched successfully!"
CONNECTION_ERR = "Couldn't connect to weather server!"


class WeatherByCity(BaseModel):
    city_name: str = Field("Kolkata", min_length=2)
    country_code: Optional[str] = None
    state_code: Optional[str] = None
    units: WeatherUnits = WeatherUnits.METRIC


class WeatherByCoordinates(BaseModel):
    lat: float = Field(28.66, ge=-90, le=90)
    lon: float = Field(77.23, ge=-180, le=180)
    units: WeatherUnits = WeatherUnits.METRIC


class WeatherByCityID(BaseModel):
    city_id: str = Field("524901", min_length=1)
    units: WeatherUnits = WeatherUnits.METRIC


@router.post("/by-name/", operation_id="get_weather_by_city_name")
async def get_weather_by_city_name(
    request: WeatherByCity
):
    """
    Get the weather data by City Name from the API.

    Args:
    - *city_name (str)* : The city name to fetch weather data for.
    - *country_code (str)* [Optional] : The country code to fetch weather data for.
    - *state_code (str)* [Optional]: The state code to fetch weather data for.
    - *units (WeatherUnits)* : The units for the weather data (standard, metric, imperial).

    Returns:

    - *dict*: A dictionary containing the success status, message, and data.
    """

    url = URL.format(
        apiVersion="2.5", apiKey=API_TOKEN, units=request.units.value
    ) + "&q={city_name}".format(city_name=request.city_name)

    if request.country_code:
        url += "," + request.country_code
    if request.state_code:
        url += "," + request.state_code

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.status_code == 200:
                return {
                    "success": True,
                    "message": FETCH_SUCCESS,
                    "data": parse_weather_data(response.json(), unit=request.units),
                }

            return JSONResponse(
                status_code=response.status_code,
                content={
                    "success": False,
                    "message": response.json().get("message", FETCH_FAILED),
                },
            )

        except httpx.ConnectError:
            return JSONResponse(
                status_code=504, content={"success": False, "message": CONNECTION_ERR}
            )


@router.post("/by-id/", operation_id="get_weather_by_city_id")
async def get_weather_by_city_id(
    request: WeatherByCityID,
):
    """
    Get the weather data by City ID from the API.

    Args:
    - *city_id (str)*: The city ID to fetch weather data for.
    - *units (WeatherUnits)*: The units for the weather data (standard, metric, imperial).

    Returns:
    - *dict*: A dictionary containing the success status and message.
    """

    url = URL.format(
        apiVersion="2.5", apiKey=API_TOKEN, units=request.units.value
    ) + "&id={city_id}".format(city_id=request.city_id)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.status_code == 200:
                return {
                    "success": True,
                    "message": FETCH_SUCCESS,
                    "data": parse_weather_data(response.json(), unit=request.units),
                }

            return JSONResponse(
                status_code=response.status_code,
                content={
                    "success": False,
                    "message": response.json().get("message", FETCH_FAILED),
                },
            )

        except httpx.ConnectError:
            return JSONResponse(
                status_code=504, content={"success": False, "message": CONNECTION_ERR}
            )


@router.post("/by-coordinates/", operation_id="get_weather_by_coordinates")
async def get_weather_by_coordinates(
    request: WeatherByCoordinates,
):
    """
    Get the weather data by Coordinates (Latitude, Longitude) from the API.

    Args:
    - *lat (float)*: The latitude to fetch weather data for.
    - *lon (float)*: The longitude to fetch weather data for.
    - *units (WeatherUnits)*: The units for the weather data (standard, metric, imperial).

    Returns:
    - *dict*: A dictionary containing the success status and message.
    """
    url = URL.format(
        apiVersion="2.5", apiKey=API_TOKEN, units=request.units.value
    ) + "&lat={lat}&lon={lon}".format(lat=request.lat, lon=request.lon)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.status_code == 200:
                return {
                    "success": True,
                    "message": FETCH_SUCCESS,
                    "data": parse_weather_data(response.json(), unit=request.units),
                }

            return JSONResponse(
                status_code=response.status_code,
                content={
                    "success": False,
                    "message": response.json().get("message", FETCH_FAILED),
                },
            )

        except httpx.ConnectError:
            return JSONResponse(
                status_code=504, content={"success": False, "message": CONNECTION_ERR}
            )
