import requests
import os
from pathlib import Path
from zipfile import ZipFile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def main():
    for link in download_uris:
        file_name = link.split('/')[3].split('.')[0]

        print(f'Attempting to download {file_name}..')
        response = requests.get(link)

        if response.status_code != 200:
            print(f'{link} is an invalid URI')
            continue


        output_file = Path(f'downloads/{file_name}.zip')
        output_file.parent.mkdir(exist_ok=True, parents=True)
        with open(output_file, 'wb') as f:
            f.write(response.content)

        with ZipFile(output_file) as zipref:
            zipref.extract(f'{file_name}.csv', path='./downloads')

        os.remove(output_file)

        print(f'Downloaded {file_name}!')

if __name__ == "__main__":
    main()
