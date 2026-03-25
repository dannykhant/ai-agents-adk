# AI Agents with Google ADK

AI agents built with Google Agent Development Kit (ADK)

## Usage

### Google Cloud commands:
To set project:
```bash
gcloud config set project $PROJECT_ID
```

To enable vertex-ai:
```bash
gcloud services enable aiplatform.googleapis.com
```

### Interface:
To run cli:
```bash
adk run personal_assistant
```

To run ADK web-based ui:
```bash
adk web --allow_origins "*"
```

### Deployment:

To deploy on Cloud Run:
```bash
adk deploy cloud_run \
  --project=$PROJECT_ID \
  --region=europe-west1 \
  --service_name=$SERVICE_NAME \
  --allow_origins="*" \
  --with_ui \
  . \
  -- \
  --labels=dev-tutorial=codelab-adk \
  --service-account=$SERVICE_ACCOUNT
```

To cleanup:
```bash
gcloud run services delete $SERVICE_NAME --region=europe-west1 --quiet

gcloud artifacts repositories delete cloud-run-source-deploy --location=europe-west1 --quiet
```