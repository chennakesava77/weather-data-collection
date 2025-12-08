resource "aws_s3_bucket" "weather_bucket" {
  bucket = var.bucket_name

  tags = {
    Name        = var.bucket_name
    Environment = var.environment
    Project     = "weather-data-collection"
  }
}

resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.weather_bucket.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "lifecycle" {
  bucket = aws_s3_bucket.weather_bucket.id

  rule {
    id     = "expire-old"
    status = "Enabled"

    expiration {
      days = 365
    }
  }
}

resource "aws_s3_bucket_public_access_block" "block_public" {
  bucket                  = aws_s3_bucket.weather_bucket.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
