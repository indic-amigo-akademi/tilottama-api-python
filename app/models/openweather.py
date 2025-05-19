from pydantic import BaseModel
from enum import Enum
import datetime

ICON_URL = "https://openweathermap.org/img/wn/{icon}@2x.png"


class WeatherUnits(Enum):
    STANDARD = "standard"
    METRIC = "metric"
    IMPERIAL = "imperial"


def from_lat_to_str(lat: float) -> str:
    """
    Convert latitude to string format.

    Args:
        *lat (float)*: The latitude to convert.

    Returns:
        *str*: The latitude in string format.
    """
    return "%d°%d′%d″ %c" % (
        abs(int(lat)),
        abs(int((lat - int(lat)) * 60)),
        abs(int((lat * 3600) % 60)),
        "N" if lat >= 0 else "S",
    )


def from_lon_to_str(lon: float) -> str:
    """
    Convert longitude to string format.

    Args:
        *lon (float)*: The longitude to convert.

    Returns:
        *str*: The longitude in string format.
    """
    return "%d°%d′%d″ %c" % (
        abs(int(lon)),
        abs(int((lon - int(lon)) * 60)),
        abs(int((lon * 3600) % 60)),
        "E" if lon >= 0 else "W",
    )


def from_temp_to_str(temp: float, unit: WeatherUnits = WeatherUnits.METRIC) -> str:
    """
    Convert temperature to string format based on the unit.

    Args:
        *temp (float)*: The temperature to convert.
        *unit (WeatherUnits)*: The unit of the temperature.

    Returns:
        *str*: The temperature in string format.
    """
    if unit == WeatherUnits.STANDARD:
        return "{:.2f} K".format(temp)
    elif unit == WeatherUnits.METRIC:
        return "{:.2f} °C".format(temp)
    elif unit == WeatherUnits.IMPERIAL:
        return "{:.2f} °F".format(temp)
    else:
        raise ValueError("Invalid unit")


def from_pressure_to_str(pressure: float) -> str:
    """
    Convert pressure to string format.

    Args:
        *pressure (float)*: The pressure to convert.

    Returns:
        *str*: The pressure in string format.
    """
    return "{:.2f} hPa".format(pressure)


def from_speed_to_str(speed: float, unit: WeatherUnits = WeatherUnits.METRIC) -> str:
    """
    Convert speed to string format.

    Args:
        *speed (float)*: The speed to convert.

    Returns:
        *str*: The speed in string format.
    """
    if unit == WeatherUnits.STANDARD:
        return "{:.2f} m/s".format(speed)
    elif unit == WeatherUnits.METRIC:
        return "{:.2f} km/h".format(speed * 3.6)
    elif unit == WeatherUnits.IMPERIAL:
        return "{:.2f} mph".format(speed)
    else:
        raise ValueError("Invalid unit")


def parse_weather_data(
    data, source="openweathermap", unit: WeatherUnits = WeatherUnits.METRIC
):
    """
    Parse the weather data from the API response.

    Args:
        *data (dict)*: The weather data to parse.

    Returns:
        *dict*: A dictionary containing the parsed weather data.
    """
    return {
        "info": {
            "city": "{}({})".format(data["name"], data["id"]),
            "country": data["sys"]["country"],
            "coordinates": {
                "latitude": from_lat_to_str(data["coord"]["lat"]),
                "longitude": from_lon_to_str(data["coord"]["lon"]),
            },
            "weather": {
                "main": data["weather"][0]["main"],
                "description": data["weather"][0]["description"],
                "icon": ICON_URL.format(icon=data["weather"][0]["icon"]),
            },
        },
        "datetime": {
            "timezone": data["timezone"],
            "main": data["dt"],
            "sunrise": data["sys"]["sunrise"],
            "sunset": data["sys"]["sunset"],
        },
        "visibility": "{:.3f} km".format(data["visibility"] / 1000),
        "temperature": {
            "main": from_temp_to_str(data["main"]["temp"], unit),
            "min": from_temp_to_str(data["main"]["temp_min"], unit),
            "max": from_temp_to_str(data["main"]["temp_max"], unit),
            "feels_like": from_temp_to_str(data["main"]["feels_like"], unit),
            "dew_point": from_temp_to_str(data["main"].get("dew_point", 0), unit),
        },
        "humidity": "{:.2f} %".format(data["main"]["humidity"]),
        "pressure": {
            "main": from_pressure_to_str(data["main"]["pressure"]),
            "sea_level": from_pressure_to_str(data["main"]["sea_level"]),
            "ground_level": from_pressure_to_str(data["main"]["grnd_level"]),
        },
        "wind": {
            "speed": from_speed_to_str(data["wind"]["speed"], unit),
            "degree": "{}°".format(data["wind"]["deg"]),
            "gust": from_speed_to_str(data["wind"].get("gust", 0), unit),
        },
        "clouds": "{} %".format(
            data["clouds"]["all"] if "all" in data["clouds"] else 0
        ),
        "rain": {
            "1h": "{:.2f} mm".format(data.get("rain", {}).get("1h", 0)),
            "3h": "{:.2f} mm".format(data.get("rain", {}).get("3h", 0)),
        },
        "snow": {
            "1h": "{:.2f} mm".format(data.get("snow", {}).get("1h", 0)),
            "3h": "{:.2f} mm".format(data.get("snow", {}).get("3h", 0)),
        },
        "copyright": {
            "source": source,
            "url": "https://openweathermap.org",
        },
    }
