# Tilottama API Python

Tilottama is a multi utility assistant and uses multiple online resources to fetch the results. This repo serves as the seamless availability of those features over a REST API endpoint.

## Endpoints

The API provides the following endpoints:

| Endpoint           | Method | Description                                       |
| ------------------ | ------ | ------------------------------------------------- |
| `/`                | `GET`  | Serves the frontend web application's index page. |
| `/app`             | `GET`  | Serves the main page for the web application.     |
| `/api/v1`          | `GET`  | Returns a list of all available API routes.       |
| `/api/v1/weather`  | `GET`  | Fetches the current weather for a given city.     |
| `/api/v1/forecast` | `GET`  | Fetches the weather forecast for a given city.    |
| `/api/v1/currency` | `GET`  | Fetches currency exchange rates.                  |

## Getting Started

- Clone the repository

```bash
git clone https://github.com/indic-amigo-akademi/tilottama-api-python.git
```

- Change directory to the cloned repository

```bash
cd tilottama-api-python
```

- Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate
```

- Install the required dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_md
```

- Run the ml models train to buid initial model

```bash
python ml_models/train_model.py
```

- Run the rest api server

```bash
fastapi run api_server/main.py --host 127.0.0.1 --port 5050
```

- Run the mcp server

```bash
python mcp_server/main.py
```
