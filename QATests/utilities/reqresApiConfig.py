# API Service Model - Configuration File: A configuration file 
# (e.g., config.py or config.json) is used to store environment-specific 
# variables like base URLs, API keys, and common headers. This prevents 
# hardcoding values and makes it easy to switch between different environments 
# (e.g., development, staging).

BASE_URL = 'https://reqres.in'
HEADERS = {
    'Content-Type': 'application/json',
    'x-api-key': 'reqres-free-v1'
}
