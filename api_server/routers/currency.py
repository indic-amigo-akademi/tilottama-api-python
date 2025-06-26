from fastapi import APIRouter
from api_server.models.currency import CurrencyCode
import requests

router = APIRouter(prefix="/currency")
URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{dateVersion}/{apiVersion}/{endpoint}"

CONNECTION_ERR = "Couldn't connect to currency exchange server!"


@router.get("/")
async def get_currency_list():
    """
    Get the list of currencies from the API.

    Returns:
        dict: A dictionary containing the success status, message, and data.
    """
    try:
        url = URL.format(
            dateVersion="latest", apiVersion="v1", endpoint="currencies.json"
        )

        response = requests.get(url)
        if response.status_code == 200:
            return {
                "success": True,
                "message": "Currency list fetched successfully!",
                "data": response.json(),
            }

        return {"success": False, "message": "Failed to fetch currency list!"}

    except requests.ConnectionError:
        return {"success": False, "message": CONNECTION_ERR}


@router.get("/{currency_code}")
async def get_currency_details(currency_code: CurrencyCode):
    """
    Get the details of a specific currency from the API.

    Args:
        *currency_code (CurrencyCode)*: The currency code to fetch details for.

    Returns:
        *dict*: A dictionary containing the success status, message, and data.
    """

    try:
        url = URL.format(
            dateVersion="latest",
            apiVersion="v1",
            endpoint=f"currencies/{currency_code}.json",
        )

        response = requests.get(url)
        if response.status_code == 200:
            return {
                "success": True,
                "message": f"Currency details for {currency_code.symbol} fetched successfully!",
                "data": response.json(),
            }

        return {
            "success": False,
            "message": f"Failed to fetch currency details for {currency_code.symbol}!",
        }

    except requests.ConnectionError:
        return {"success": False, "message": CONNECTION_ERR}


@router.get("/exchange-rate/{from_currency_code}/{to_currency_code}")
async def get_exchange_rate(
    from_currency_code: CurrencyCode, to_currency_code: CurrencyCode
):
    """
    Get the exchange rate between two currencies from the API.

    Args:
        *from_currency (CurrencyCode)*: The currency code to convert from.
        *to_currency (CurrencyCode)*: The currency code to convert to.

    Returns:
        *dict*: A dictionary containing the success status, message, and data.
    """
    url = URL.format(
        dateVersion="latest",
        apiVersion="v1",
        endpoint=f"currencies/{from_currency_code.value}.json",
    )

    try:
        response = requests.get(url)
        if response.status_code == 200:
            exchange_rate = response.json()[from_currency_code.value][
                to_currency_code.value
            ]
            return {
                "success": True,
                "message": f"Exchange rate from {from_currency_code} to {to_currency_code} fetched successfully!",
                "data": {"exchange_rate": exchange_rate},
            }
        else:
            return {
                "success": False,
                "message": f"Failed to fetch exchange rate from {from_currency_code} to {to_currency_code}!",
            }

    except requests.ConnectionError:
        return {"success": False, "message": CONNECTION_ERR}

    except Exception:
        return {
            "success": False,
            "message": f"{to_currency_code} is not a valid currency code!",
        }
