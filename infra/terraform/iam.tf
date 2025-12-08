# =========================================
# IAM resources removed/skipped
# =========================================

# resource "aws_iam_user" "app_user" {
#   name = "weather-app-user"
#   force_destroy = true
# }

# data "aws_iam_policy_document" "s3_put_policy" {
#   statement {
#     sid = "AllowS3Actions"
#     actions = [
#       "s3:PutObject",
#       "s3:PutObjectAcl",
#       "s3:GetObject",
#       "s3:ListBucket"
#     ]
#     resources = [
#       aws_s3_bucket.weather_bucket.arn,
#       "${aws_s3_bucket.weather_bucket.arn}/*"
#     ]
#   }
# }

# resource "aws_iam_policy" "app_policy" {
#   name   = "weather-app-s3-policy"
#   policy = data.aws_iam_policy_document.s3_put_policy.json
# }

# resource "aws_iam_user_policy_attachment" "attach" {
#   user       = aws_iam_user.app_user.name
#   policy_arn = aws_iam_policy.app_policy.arn
# }

# resource "aws_iam_access_key" "app_key" {
#   user = aws_iam_user.app_user.name
# }
