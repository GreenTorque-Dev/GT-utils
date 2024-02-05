# main.py
import os
import shutil
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


def move_file(source, destination):
    shutil.move(source, destination)
    # res = os.popen(sudo_string + f' mv {source} {destination}').read()
    # print(res)


def main():
    download_url = f"https://www.ip2location.com/download?token={config.TOKEN}&file={config.DB_CODE}"

    output_path = str(resource_path / 'testip.zip')
    download_file(download_url, output_path)

    extraction_path = str(resource_path / 'testzip')
    extract_zip(output_path, extraction_path)

    cidr_file = find_file_with_cidr(directory=extraction_path, match='CIDR')

    move_file(source=cidr_file, destination=config.OUTPUT_DIR)

    print(f"File downloaded successfully to: {cidr_file}")


if __name__ == "__main__":
    resource_path = Path('resources')
    resource_path.mkdir(exist_ok=True, parents=True)
    main()
