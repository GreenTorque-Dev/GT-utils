# main.py
import os
import shutil
import time
from datetime import datetime, timedelta
from pathlib import Path
from zipfile import ZipFile

import requests
import config


def download_file(url, output_path):
    response = requests.get(url, stream=True)
    with open(output_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)


def extract_zip(zip_path, extract_path):
    with ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)


def find_file_with_cidr(directory, match):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if match in file:
                return os.path.abspath(os.path.join(root, file))


def process_cidr_file(file_path, output_directory):
    # Get the current date
    today = datetime.now()

    # Calculate yesterday and tomorrow
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)

    # Define the date formats
    dates = {
        'yesterday': yesterday.strftime('%d%m%Y'),
        'today': today.strftime('%d%m%Y'),
        'tomorrow': tomorrow.strftime('%d%m%Y'),
    }

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Create copies with specified filenames
    for key, date in dates.items():
        filename = f'IP2LOCATION-IPV4-{date * 4}.ZIP'
        output_path = os.path.join(output_directory, filename)
        shutil.copyfile(file_path, output_path)
        print(f'Created {output_path}')

    print('All files have been created successfully.')


def cleanup_cidr_files(directory):
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        # Check if the filename starts with the specified prefix
        if filename.startswith("IP2LOCATION-IPV4-"):
            # Construct the full path to the file
            file_path = os.path.join(directory, filename)
            # Check if it is a file (not a directory)
            if os.path.isfile(file_path):
                # Delete the file
                os.remove(file_path)
                print(f"Deleted {file_path}")

    print("Cleanup completed successfully.")


def main():
    download_url = f"https://www.ip2location.com/download?token={config.TOKEN}&file={config.DB_CODE}"

    output_path = str(resource_path / 'testip.zip')
    download_file(download_url, output_path)

    extraction_path = str(resource_path / 'testzip')
    extract_zip(output_path, extraction_path)

    cidr_file = find_file_with_cidr(directory=extraction_path, match='CIDR')

    cleanup_cidr_files(directory=config.OUTPUT_DIR)
    process_cidr_file(cidr_file, output_directory=config.OUTPUT_DIR)

    time.sleep(2)
    os.remove(output_path)
    os.remove(extraction_path)
    print(f"File downloaded successfully to: {cidr_file}")


if __name__ == "__main__":
    resource_path = Path('resources')
    resource_path.mkdir(exist_ok=True, parents=True)
    main()
