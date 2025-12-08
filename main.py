"""
Entry point for weather collector: fetches weather for configured cities and uploads batch JSON to S3.
"""
import os
import json
from datetime import datetime
from dotenv import load_dotenv
from weather import fetch_weather_for_city
from s3_uploader import upload_text_to_s3

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
S3_BUCKET = os.getenv("S3_BUCKET_NAME")
CITIES = [c.strip() for c in os.getenv("CITIES", "").split(",") if c.strip()]

if not API_KEY:
    raise SystemExit("OPENWEATHER_API_KEY is required in environment")
if not S3_BUCKET:
    raise SystemExit("S3_BUCKET_NAME is required in environment")
if not CITIES:
    raise SystemExit("At least one city must be provided in CITIES env var")

def main():
    batch_ts = datetime.utcnow().isoformat() + "Z"
    results = []
    for city in CITIES:
        try:
            data = fetch_weather_for_city(city, API_KEY)
            payload = {
                "city": city,
                "timestamp": batch_ts,
                "fetched_at": datetime.utcnow().isoformat() + "Z",
                "weather": data,
            }
            results.append(payload)
        except Exception as e:
            # log and continue
            print(f"[ERROR] Fetching {city}: {e}")

    if results:
        key = f"weather/{datetime.utcnow().strftime('%Y/%m/%d/%H%M%S')}_batch.json"
        body = json.dumps({"batch_timestamp": batch_ts, "data": results}, indent=2)
        upload_text_to_s3(body, S3_BUCKET, key)
        print(f"Uploaded {len(results)} records to s3://{S3_BUCKET}/{key}")

if __name__ == "__main__":
    main()
