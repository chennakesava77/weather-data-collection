import boto3
from botocore.exceptions import BotoCoreError, ClientError
from pathlib import Path

# Initialize S3 client
s3 = boto3.client("s3")

def upload_text_to_s3(text: str, bucket: str, key: str) -> None:
    """Upload a single text string to S3."""
    try:
        s3.put_object(Bucket=bucket, Key=key, Body=text.encode("utf-8"))
        print(f" Uploaded {key} successfully.")
    except (BotoCoreError, ClientError) as e:
        print(f"Error uploading {key}: {e}")
        raise

def upload_folder_to_s3(folder_path: str, bucket: str) -> None:
    """Upload all .json files from a folder (including subfolders) to S3."""
    folder = Path(folder_path)
    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"The folder path {folder_path} does not exist or is not a directory.")

    for file_path in folder.rglob("*.json"):  # recursively find JSON files
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Generate S3 key relative to the folder path
        s3_key = str(file_path.relative_to(folder))
        upload_text_to_s3(content, bucket, s3_key)

if __name__ == "__main__":
    BUCKET_NAME = "my-weather-data-collection-2025"  # your bucket name
    FOLDER_PATH = "/mnt/c/Users/user/weather-data-collection/weather-json"  # local folder path

    upload_folder_to_s3(FOLDER_PATH, BUCKET_NAME)
