# IP Location Cron Job Setup

This repository provides a Bash script to automate the setup of a cron job for fetching IP location information using a Python script (`main.py`). The cron job is scheduled to run at the start and mid of the day.

## Prerequisites

Before setting up the cron job, ensure the following prerequisites are met:

1. Python3 and pip are installed on your system.
2. Clone this repository to your local machine.

## Setup Instructions

1. Open a terminal and navigate to the cloned repository directory.

2. Make the setup script executable and run it using sudo:
   ```bash
   chmod +x setup_script.sh
   sudo ./setup_script.sh
