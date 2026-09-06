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
ruff check .
ruff format --check .
pytest -q
```

CI (`.github/workflows/ci.yml`): gitleaks → ruff → pip-audit → pytest → docker smoke → optional ECR on `main`.

**Repo secrets / vars for a created service:**

| Name | Type | Purpose |
| --- | --- | --- |
| `GITLEAKS_LICENSE` | secret | Required for `gitleaks-action` (wire as `GITLEAKS_LICENSE: ${{ secrets.GITLEAKS_LICENSE }}`). Do not create `GITHUB_TOKEN`. |
| `AWS_ROLE_ARN` | secret | OIDC role for ECR publish |
| `ECR_PUBLISH` | variable | Set `true` to enable publish on `main` |

Also fill `AWS_REGION` / `ECR_REPOSITORY` in the workflow. Dependabot weekly PRs for pip + Actions.

## Docker

```sh
docker build -t ${{ values.name }}:local .
docker run --rm -p 8080:8080 ${{ values.name }}:local
```

## Catalog

Owner: `${{ values.owner }}` · System: `${{ values.system }}`
