from pydantic import BaseModel, Field
from typing import Optional
from api_server.models.openweather import WeatherUnits


class ForecastByCity(BaseModel):
    city_name: str = Field("Kolkata", min_length=2)
    country_code: Optional[str] = None
    state_code: Optional[str] = None
    units: WeatherUnits = WeatherUnits.METRIC


class ForecastByCoordinates(BaseModel):
    lat: float = Field(28.66, ge=-90, le=90)
    lon: float = Field(77.23, ge=-180, le=180)
    units: WeatherUnits = WeatherUnits.METRIC


class ForecastByCityID(BaseModel):
    city_id: str = Field("524901", min_length=1)
    units: WeatherUnits = WeatherUnits.METRIC
