import os

try:
    import boto3
    from botocore.exceptions import BotoCoreError, ClientError
except ImportError:
    boto3 = None  # Allows local use without requiring boto3

def get_secret(name: str, fallback_env: str = None) -> str:
    """
    Load a secret by name. Tries AWS Secrets Manager first (if boto3 is available),
    otherwise falls back to environment variables.

    :param name: Name of the secret or environment variable
    :param fallback_env: Environment variable name (if different)
    :return: Secret value or raises Exception
    """
    fallback_env = fallback_env or name
    if boto3:
        try:
            client = boto3.client("secretsmanager")
            response = client.get_secret_value(SecretId=name)
            return response.get("SecretString") or response["SecretBinary"]
        except (BotoCoreError, ClientError):
            pass  # Fallback to env if Secrets Manager fails

    value = os.getenv(fallback_env)
    if not value:
        raise Exception(f"Missing secret: {name}")
    return value

