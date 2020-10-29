from azure.storage.blob import BlobServiceClient
import pandas as pd
from azure.storage.blob import BlobClient
import json
import re

blob_name = []

def main():
    blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=empdetailstorage;AccountKey=XfDymEx6ZabXF7pJqtnp8i28HhqkfQ/4/2bW6M1Cfkj/HOlaTm3xxfkXeJs4xBAiUBVHH9J4ZXh4tUlx5wq49Q==;EndpointSuffix=core.windows.net")

    container_client = blob_service_client.get_container_client("empdetailsnew")
    #print(container_client.__dict__)
    blobs_list = container_client.list_blobs()
    print(blobs_list.__dict__)
    for blob in blobs_list:
        blob_name.append(blob.name)
    print(blob_name)

    blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=empdetailstorage;AccountKey=XfDymEx6ZabXF7pJqtnp8i28HhqkfQ/4/2bW6M1Cfkj/HOlaTm3xxfkXeJs4xBAiUBVHH9J4ZXh4tUlx5wq49Q==;EndpointSuffix=core.windows.net", container_name="empdetailsnew", blob_name=str(blob_name[0]))
    blob_data = blob.download_blob()
    byte_data = blob_data._current_content
    json_data = json.dumps(byte_data.decode('utf-8'))
    res = re.findall(r'\{.*?\}', json_data)
    print(res)


if __name__ == '__main__':
    main()

