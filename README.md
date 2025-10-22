# FastAPI Deployment Test

A minimal FastAPI app to verify that the `deploy.sh` automation script runs successfully.

### How to run locally

```bash
docker build -t fastapi-deploy-test .
docker run -d -p 8000:8000 fastapi-deploy-test
```
