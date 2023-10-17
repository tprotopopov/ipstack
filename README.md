# ipstack

Docker Container Setup
-   docker build -t ipstack .
Run the app: 
-   docker run ipstack python3 main.py YOUR_IP_ADDRESS YOUR_ACCESS_TOKEN

Security Notes.
1. The API key should be kept secure. Avoid storing it in plain text or hard-coding it within the script. In this example, the key is expected to be passed as a command-line argument, but for enhanced security, consider using environment variables or secure vaults.

2. The script uses HTTP. Depending on your requirements, you might want to use HTTPS to ensure the confidentiality and integrity of the data in transit. The IPStack supports HTTPS in paid plans.

3. Error handling in the script checks for request failures but does not explicitly handle all potential edge cases for data input/output or potential API-specific errors (like rate limiting or service outages). Further robustness and security checks may be necessary for production-level applications.