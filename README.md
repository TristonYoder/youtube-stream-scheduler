#Step-by-Step Guide:

##Install Homebrew:
        If you don't have Homebrew installed on your macOS or Linux system, you can install it by running the following command in your terminal:
    ``` sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`
    ```
    Follow the on-screen instructions to complete the installation.

##Install Python:

    brew install python
    
##Install Required Python Libraries:

    pip3 install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

##Download and Configure the Script:
  Download the provided Python script and save it as main.py on your computer.

##Set Configuration Variables:
  Open main.py in a text editor or code editor of your choice.
  Replace the placeholders in the script with your actual information.

##Authentication:
  Ensure that you have set up the correct authentication method (either service account or OAuth2) in the script based on your configuration.

##Run the Script:
  Navigate to the directory where main.py is located.

    cd ~/Projects/youtube-stream-scheduler

  Run the script using the following command:
    
    python main.py

Result:
  The script will create the live broadcast, live stream, bind them together, and add the live broadcast to the specified playlist.
  If everything is configured correctly and the script runs without errors, you should see the message "Stream [stream_title] Created Successfully!" printed in the terminal.

Check YouTube:
  Go to your YouTube channel and check the "Live Control Room" to ensure that the live stream is scheduled and set up correctly according to your specified details.
