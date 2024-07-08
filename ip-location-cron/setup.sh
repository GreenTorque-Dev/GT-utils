#!/bin/bash

# Get the current script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Task 1: Install Python3 and pip
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Task 3: Install libraries from requirements.txt using xargs
cat requirements.txt | xargs -n 1 sudo pip3 install

# Task 4: Set up a cron job to run main.py at the start and mid of the day
CRON_LOG_FILE="$SCRIPT_DIR/cron_job_log.txt"
echo "0 0,12 * * * /usr/bin/python3 $SCRIPT_DIR/main.py >> $CRON_LOG_FILE 2>&1" | sudo crontab -

# Task 5: Give full permissions to /var/html/www and its contents
sudo chmod -R 777 /var/www/html

# Additional Task: Make sure to replace /path/to/main.py with the actual path to your main.py script
# Note: Adjust the cron schedule according to your requirements

echo "Setup completed successfully!"
