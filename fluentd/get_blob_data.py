from azure.storage.blob import BlobServiceClient
import pandas as pd
from azure.storage.blob import BlobClient
import json

blob_name = []

def main():
    blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=empcognitivestorage;AccountKey=2VFFnLiSbNW1ZdSWv7hU17sfh8WAf8X4p/m8J5WWvzLXJV1fYkQ3T6wXVEYYY0rYJYXhIWZWr//QUvapbfJH4g==;EndpointSuffix=core.windows.net")

    container_client = blob_service_client.get_container_client("empdetails")
    #print(container_client.__dict__)
    blobs_list = container_client.list_blobs()
    print(blobs_list.__dict__)
    for blob in blobs_list:
        blob_name.append(blob.name)

    blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=empcognitivestorage;AccountKey=2VFFnLiSbNW1ZdSWv7hU17sfh8WAf8X4p/m8J5WWvzLXJV1fYkQ3T6wXVEYYY0rYJYXhIWZWr//QUvapbfJH4g==;EndpointSuffix=core.windows.net", container_name="empdetails", blob_name=str(blob_name[0]))
    blob_data = blob.download_blob()
    byte_data = blob_data._current_content
    json_data = json.dumps(byte_data.decode('utf-8'))
    print(json_data)


if __name__ == '__main__':
    main()

