# ${{ values.name }}

${{ values.description }}

Gurujix golden-path FastAPI service (same layout as `service-orders`).

## Run locally

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload --port 8080
```

```sh
curl http://127.0.0.1:8080/health
curl http://127.0.0.1:8080/ready
pytest -q
```

## Docker

```sh
docker build -t ${{ values.name }}:local .
docker run --rm -p 8080:8080 ${{ values.name }}:local
```

## Catalog

Owner: `${{ values.owner }}` · System: `${{ values.system }}`
