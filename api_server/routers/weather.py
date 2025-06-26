from fastapi import APIRouter
from fastapi.responses import JSONResponse
import os
import httpx
from api_server.models.openweather import WeatherUnits, parse_weather_data

router = APIRouter(prefix="/weather")
URL = "https://api.openweathermap.org/data/{apiVersion}/weather?appid={apiKey}&units={units}"
API_TOKEN = os.getenv("OPENWEATHER_API_KEY")
if not API_TOKEN:
    raise RuntimeError("OPENWEATHER_API_KEY environment variable not set.")

FETCH_FAILED = "Failed to fetch weather data!"
FETCH_SUCCESS = "Weather data fetched successfully!"
CONNECTION_ERR = "Couldn't connect to weather server!"


@router.get("/by-name/{city_name}")
async def get_weather_by_city_name(
    city_name: str,
    country_code: str | None = None,
    state_code: str | None = None,
    units: WeatherUnits = WeatherUnits.METRIC,
):
    """
    Get the weather data by City Name from the API.

    Args:
        *city_name (str)* : The city name to fetch weather data for.
        *country_code (str)* [Optional] : The country code to fetch weather data for.
        *state_code (str)* [Optional]: The state code to fetch weather data for.
        *units (WeatherUnits)* : The units for the weather data (standard, metric, imperial).

    Returns:
        *dict*: A dictionary containing the success status, message, and data.
    """

    url = URL.format(
        apiVersion="2.5", apiKey=API_TOKEN, units=units.value
    ) + "&q={city_name}".format(city_name=city_name)

    if country_code:
        url += "," + country_code
    if state_code:
        url += "," + state_code

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.status_code == 200:
                return {
                    "success": True,
                    "message": FETCH_SUCCESS,
                    "data": parse_weather_data(response.json(), unit=units),
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


@router.get("/by-id/{city_id}")
async def get_weather_by_city_id(
    city_id: str, units: WeatherUnits = WeatherUnits.METRIC
):
    """
    Get the weather data by City ID from the API.

    Args:
        *city_id (str)*: The city ID to fetch weather data for.
        *units (WeatherUnits)*: The units for the weather data (standard, metric, imperial).

    Returns:
        *dict*: A dictionary containing the success status and message.
    """

    url = URL.format(
        apiVersion="2.5", apiKey=API_TOKEN, units=units.value
    ) + "&id={city_id}".format(city_id=city_id)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.status_code == 200:
                return {
                    "success": True,
                    "message": FETCH_SUCCESS,
                    "data": parse_weather_data(response.json(), unit=units),
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


@router.get("/by-coordinates/{lat}/{lon}")
async def get_weather_by_coordinates(
    lat: float, lon: float, units: WeatherUnits = WeatherUnits.METRIC
):
    """
    Get the weather data by Coordinates (Latitude, Longitude) from the API.

    Args:
        *lat (float)*: The latitude to fetch weather data for.
        *lon (float)*: The longitude to fetch weather data for.

    Returns:
        *dict*: A dictionary containing the success status and message.
    """
    url = URL.format(
        apiVersion="2.5", apiKey=API_TOKEN, units=units.value
    ) + "&lat={lat}&lon={lon}".format(lat=lat, lon=lon)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.status_code == 200:
                return {
                    "success": True,
                    "message": FETCH_SUCCESS,
                    "data": parse_weather_data(response.json(), unit=units),
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
