import mlflow

# point MLflow to your local DB + artifacts
mlflow.set_tracking_uri("sqlite:///mlflow.db")