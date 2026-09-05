# Gurujix golden-path Software Template for FastAPI services.
#
## Loaded by platform-portal as a catalog Template.
## Skeleton files use ${{ values.* }} placeholders filled by the scaffolder.

## Local layout

```text
template.yaml     ← Template entity (form + steps)
skeleton/         ← files copied into each new service repo
```

## How it is used

1. Open platform-portal → Create
2. Choose **Gurujix Python Service**
3. Fill name, description, owner, system, GitHub repo
4. Scaffolder renders `skeleton/`, publishes to GitHub, registers catalog-info

## Register in the portal

`platform-portal` loads this template from the sibling path in `app-config.yaml` (local).
