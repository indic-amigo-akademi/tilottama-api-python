from fastapi import APIRouter
import requests

router = APIRouter()
URL = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{dateVersion}/{apiVersion}/{endpoint}"


@router.get("/")
async def get_currency_list():
    """
    Get the list of currencies from the API.
    Returns:
        dict: A dictionary containing the success status, message, and data.
    """
    url = URL.format(dateVersion="latest", apiVersion="v1", endpoint="currencies.json")

    response = requests.get(url)
    if response.status_code == 200:
        return {
            "success": True,
            "message": "Currency list fetched successfully!",
            "data": response.json(),
        }
    else:
        return {"success": False, "message": "Failed to fetch currency list!"}


@router.get("/{currency_code}")
async def get_currency_details(currency_code: str):
    """
    Get the details of a specific currency from the API.
    Args:
        currency_code (str): The currency code to fetch details for.
    Returns:
        dict: A dictionary containing the success status, message, and data.
    """
    currency_code = currency_code.lower().strip()
    url = URL.format(
        dateVersion="latest",
        apiVersion="v1",
        endpoint=f"currencies/{currency_code}.json",
    )

    response = requests.get(url)
    if response.status_code == 200:
        return {
            "success": True,
            "message": f"Currency details for {currency_code.upper()} fetched successfully!",
            "data": response.json(),
        }
    else:
        return {
            "success": False,
            "message": f"Failed to fetch currency details for {currency_code}!",
        }


@router.get("/exchange-rate/{from_currency_code}/{to_currency_code}")
async def get_exchange_rate(from_currency_code: str, to_currency_code: str):
    """
    Get the exchange rate between two currencies from the API.
    Args:
        from_currency (str): The currency code to convert from.
        to_currency (str): The currency code to convert to.
    Returns:
        dict: A dictionary containing the success status, message, and data.
    """
    from_currency = from_currency_code.lower().strip()
    to_currency = to_currency_code.lower().strip()
    url = URL.format(
        dateVersion="latest",
        apiVersion="v1",
        endpoint=f"currencies/{from_currency}.json",
    )

    response = requests.get(url)
    if response.status_code == 200:
        try:
            exchange_rate = response.json()[from_currency][to_currency]
            return {
                "success": True,
                "message": f"Exchange rate from {from_currency.upper()} to {to_currency.upper()} fetched successfully!",
                "data": {"exchange_rate": exchange_rate},
            }
        except Exception:
            return {
                "success": False,
                "message": f"Failed to fetch exchange rate from {from_currency} to {to_currency}!",
            }
    else:
        return {
            "success": False,
            "message": f"Failed to fetch exchange rate from {from_currency} to {to_currency}!",
        }
