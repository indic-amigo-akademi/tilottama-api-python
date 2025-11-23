from fastapi import APIRouter
from fastapi.responses import JSONResponse
import os
import httpx
from api_server.models.openweather import WeatherUnits, parse_forecast_data
from api_server.models.forecast import (
    ForecastByCity,
    ForecastByCityID,
    ForecastByCoordinates,
)


router = APIRouter(
    prefix="/forecast",
    tags=["Forecast"],
    responses={404: {"description": "Not found"}},
)
URL = "https://api.openweathermap.org/data/{apiVersion}/forecast?appid={apiKey}&units={units}"
API_TOKEN = os.getenv("OPENWEATHER_API_KEY")
if not API_TOKEN:
    raise RuntimeError("OPENWEATHER_API_KEY environment variable not set.")


FETCH_FAILED = "Failed to fetch weather forecast data!"
FETCH_SUCCESS = "Weather forecast data fetched successfully!"
CONNECTION_ERR = "Couldn't connect to forecast server!"


@router.post("/by-name/{city_name}", operation_id="get_forecast_by_city_name")
async def get_forecast_by_city_name(request: ForecastByCity):
    """
    Get the weather forecast by City Name from the API.

    Args:
        *city_name (str)* : The city name to fetch weather forecast for.
        *country_code (str)* [Optional] : The country code to fetch weather forecast for.
        *state_code (str)* [Optional]: The state code to fetch weather forecast for.
        *units (WeatherUnits)* : The units for the weather data (standard, metric, imperial).

    Returns:
        *dict*: A dictionary containing the success status, message, and data.
    """

    url = URL.format(
        apiVersion="2.5", apiKey=API_TOKEN, units=request.units.value
    ) + "&q={city_name}".format(city_name=request.city_name)

    if request.state_code:
        url += "," + request.state_code
    if request.country_code:
        url += "," + request.country_code

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.status_code == 200:
                return {
                    "success": True,
                    "message": FETCH_SUCCESS,
                    "data": parse_forecast_data(response.json(), unit=request.units),
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
                status_code=504,
                content={
                    "success": False,
                    "message": CONNECTION_ERR,
                },
            )


@router.post("/by-id/{city_id}", operation_id="get_forecast_by_city_id")
async def get_forecast_by_city_id(request: ForecastByCityID):
    """
    Get the weather forecast by City ID from the API.

    Args:
        *city_id (str)* : The city ID to fetch weather forecast for.
        *units (WeatherUnits)* : The units for the weather data (standard, metric, imperial).

    Returns:
        *dict*: A dictionary containing the success status, message, and data.
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
                    "data": parse_forecast_data(response.json(), unit=request.units),
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
                status_code=504,
                content={
                    "success": False,
                    "message": CONNECTION_ERR,
                },
            )


@router.post("/by-coordinates/{lat}/{lon}", operation_id="get_forecast_by_coordinates")
async def get_forecast_by_coordinates(request: ForecastByCoordinates):
    """
    Get the weather forecast by Coordinates from the API.

    Args:
        *lat (float)* : The latitude to fetch weather forecast for.
        *lon (float)* : The longitude to fetch weather forecast for.
        *units (WeatherUnits)* : The units for the weather data (standard, metric, imperial).

    Returns:
        *dict*: A dictionary containing the success status, message, and data.
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
                    "data": parse_forecast_data(response.json(), unit=request.units),
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
                status_code=504,
                content={
                    "success": False,
                    "message": CONNECTION_ERR,
                },
            )
