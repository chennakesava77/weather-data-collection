# Output the S3 bucket name
output "s3_bucket_name" {
  value = aws_s3_bucket.weather_bucket.bucket
}

# =========================================
# IAM-related outputs removed since IAM is skipped
# =========================================

# output "app_access_key_id" {
#   value = aws_iam_access_key.app_key.id
# }

# output "app_secret_access_key" {
#   value     = aws_iam_access_key.app_key.secret
#   sensitive = true
# }
