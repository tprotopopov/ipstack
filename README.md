# ipstack

## Security Notes

- The API key should be kept secure. Avoid storing it in plain text or hard-coding it within the script.

- The script uses HTTP. Depending on your requirements, you might want to use HTTPS to ensure the confidentiality and integrity of the data in transit. The IPStack supports HTTPS in paid plans.

- Error handling in the script checks for request failures but does not explicitly handle all potential edge cases for data input/output or potential API-specific errors (like rate limiting or service outages). Further robustness and security checks may be necessary for production-level applications.

## Python Setup Summary

Before you can run the script in your local environment, you need to set up your Python environment. Here's a step-by-step guide:

1. **Install Dependencies**: The script requires certain Python packages to work correctly. These dependencies are listed in the `requirements.txt` file. To install these packages, run the following command in your terminal:
    ```sh
    pip3 install -r requirements.txt
    ```
    This command will automatically install all the necessary packages.

2. **Access Token File Setup**: The script reads the IPStack API access key from a file. Here's how to set up the access token file:

    - Create a text file that will store your access token. In the directory where your script is located create a new file named `token` (with no file extension).

    - Open the `token` file in a text editor. Paste the access key as plain text. Here's an example of how the content of the `token` file should look:

      ```
      YOUR_IPSTACK_ACCESS_KEY
      ```

      Replace `YOUR_IPSTACK_ACCESS_KEY` with your actual access key. Ensure there are no spaces or blank lines before or after the key within the file.

    - Ensure that the script has read permissions for the `token` file, like so:

      ```sh
      chmod 600 token
      ```
3. **Running the Script**: 
   - Use the following command, replacing `YOUR_IP_ADDRESS` with the actual IP address you wish to query.
    ```sh
    python main.py YOUR_IP_ADDRESS
    ```
   
## Docker Container Setup

- Build the Docker image with the following command:
    ```sh
    docker build -t ipstack .
    ```

- To enhance security, it's recommended to use a token file to store your sensitive information. You can pass this file to the container when you run it. 

    ```sh
    docker run -v /path/to/your/token/file:/app/token:ro ipstack python3 main.py YOUR_IP_ADDRESS
    ```
  
- Run the app using the following command:

    ```sh
    docker run ipstack python3 main.py YOUR_IP_ADDRESS
    ```
