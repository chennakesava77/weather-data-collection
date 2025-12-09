  # weather-data-collection   Authour:Chenna kesava reddy Boreddy

# Project Overview:-
                 This project collects real-time weather data for multiple cities using the OpenWeather API, processes it using Python, and automatically uploads the data files to AWS S3.

# DevOps workflow:-
# 1.API Integration: -API Integration means connecting one software application with another using an API.
# 2.Cloud Automation:-Automatically managing cloud services like EC2, S3, VPC, IAM, Lambda using scripts or tools (Terraform, Ansible, CloudFormation, etc.)
# 3.Infrastructure as Code (IaC) :- managing and creating cloud infrastructure (like servers, databases, networks, and storage) using code instead of doing it manually.
# 4.CI/CD readiness:means your project is prepared to be used in a CI/CD pipeline — meaning it can be automatically tested, built, deployed, and delivered without manual work.
               --------->my project is ready for automation.
               --------->my code can be integrated and deployed smoothly.
# 5.Logging:-recording important events and information while a program is running.
# 6.Error Handling (Managing Failures):-catching and managing errors so your program does not crash.
               ---->Instead of stopping, your code handles the error safely.
# 7.Modular Code (Code in Small Parts):-writing your program in small, separate files or functions instead of one big file.

# main Feature of this project:-
       The main feature of this project is fetching real-time weather data for multiple cities and automatically storing it in AWS S3 with timestamps for historical tracking.”
 # in my Project:
 -->Connects to OpenWeather API
 -->Fetches live weather data (temperature, humidity, conditions)
 -->Supports multiple cities
 -->Adds timestamps to each data record
 -->Saves the data as JSON/CSV files
 -->Uploads the files automatically to AWS S3
 -->Maintains history for each city.
# Technical Architecture:
Languages / Tools:
# 1.Python 3.x:This is the programming language used to build your project.
# 2.AWS S3 (Simple Storage Service):AWS S3 is cloud storage.
     -->my project uploads weather data files to S3
# 3.OpenWeather API:This is the external weather API you use to get live weather data.
# 4.Terraform (Infrastructure as Code):Terraform is a tool used to automatically create AWS resources like S3 buckets.
# 5.boto3: boto3 is AWS SDK for Python.
     -->It allows Python code to talk to AWS.
# 6.python-dotenv:This library is used to load environment variables from a .env file.
# 7.requests:A Python library used to call APIs.

# project structure:
weather-data-collection-system/
│── src/
│   ├── weather_fetcher.py
│   ├── s3_uploader.py
│   ├── main.py
│── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│── .env.example
│── requirements.txt
│── README.md
->First we create virtual environment i mean .env
-> intall all dependencies.
    pip install -r requirements.txt
->Next Run the application
    python main.py
# Terraform Setup (AWS S3 Bucket Creation)
-> First i initialize terraform
     terraform init
-->After to validate terraform
     Terraform validate
-->Plan to terraform
      Terraform plan
--> apply to terraform
  terraform apply -auto-approve

# High-Level Architecture Diagram
┌───────────────────────┐       ┌────────────────────┐
│   Python Application   │──────▶│  OpenWeather API    │
└──────────┬────────────┘       └────────────────────┘
           │
           ▼
┌─────────────────────────┐
│  Weather Data (JSON)    │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│      AWS S3 Bucket      │
│  (Stores weather files) │
└─────────────────────────┘
# after i am doing aws configure
how to create access key id and access key:-

-->First i login to AWS console next go to IAM and click to users 
-->select my users i mean kesava 
--> go  to "security credentials" tab next scroll down to access keys after to create access key
--> choose CLI->next->create
# next to check AWS status(aws sts get_caller_identity)
-->next we check list of files in this project.
--> make a directory to the project root on weather_json.
-->after i add one city i mean weather.json in my cities group.
-->upload the data in my s3 bucket.
-->after i check the s3 bucket in aws account with data add or not.
-->Next i make change directory.
-->after i install  boto3.
 From boto3
--Upload files to S3
--Manage AWS resources programmatically
--> next uploaded weather.json files in my s3 bucket successfully.
-->after deactivate to venv(Virtual environment)
-->next i add 2 cities temparature and humidity
-->after i am activate venv 
-->and i am dpoing all citys uploaded in my s3 bucket.

# Error Handling:-The system logs errors safely without interrupting execution.
1. Invalid API key:-the API key you are using is wrong, expired, missing, or not recognized by the server.
                    ---->This error comes from the OpenWeather API when it cannot verify your key.
2. Missing environment variables: your program is trying to read a value (like API key or AWS credentials), but that value is not found in the environment or .env file.
3. AWS upload exceptions:-occur when your Python program tries to upload a file to AWS S3, but something goes wrong.
4. Network/API timeout:-A network/API timeout occurs when your Python program requests data from the OpenWeather API.
                             ------>but the API does not respond within a certain time limit.

# Now i am using git commands and i push my data in github repository/
git commands:1.Initialize Git(git init)
             2.check git status(git status)
             3.Add files to staging(git add .)
             4.Commit changes(git commit -m "my message")
             5.Add remote(git remote add origin my repositort http url)
             6.Push code first time(git push -u origin main)

# summery:
          The Weather Data Collection System is a DevOps-focused project that integrates real-time weather data retrieval with cloud automation and infrastructure management. It demonstrates essential skills in API integration, cloud storage, automation, and code organization.
             
             
