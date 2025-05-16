import logging
import os
import requests


class Sources:
    """
    Class to handle the download of the CSV files and API endpoints used in the project.
    """
    def __init__(self, rebuild=False):
        """
        Initialize the Sources class.
        
        If rebuild is True, it will download all the CSV files used in the project.
        """
        self.__apiKey = os.getenv('SUBWAY_API_KEY')
        self.__datasetKey = os.getenv('SUBWAY_DATASET_KEY')


    def download_csv_file(self, url, filename):
        """
        Download the CSV file from the specified URL.
        It is then stored in the opendata/sources directory.
        """

        output_file = "opendata/sources/" + filename + ".csv"

        headers = {
            'apiKey': self.__datasetKey
            }
        # Send the HTTP GET request
        response = requests.get(url=url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Write the content to a CSV file
            with open(output_file, 'wb') as file:
                file.write(response.content)
            print(f"CSV successfully saved to {output_file}")
        else:
            print(f"Failed to download CSV. Status code: {response.status_code}")

if __name__ == "__main__":
    sources = Sources()
    sources.download_csv_file("https://data.iledefrance-mobilites.fr/api/explore/v2.1/catalog/datasets/schema_gares-gf/exports/csv", "stations")
    sources.download_csv_file("https://data.iledefrance-mobilites.fr/api/explore/v2.1/catalog/datasets/referentiel-des-lignes/exports/csv", "lines")
