import logging
import json
from flask import Flask, request, render_template,jsonify, redirect, url_for
import re
from flask_cors import CORS, cross_origin
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import BlobClient

app = Flask(__name__)
CORS(app, support_credentials=True)


blob_name = []
emp_data={}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/services', methods=['GET','POST'])
def services():
    return render_template("services.html")    

@app.route('/get_emp_details', methods=['GET','POST'])
def getEmpDetails():
    details = []
    blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=empdetailstorage;AccountKey=XfDymEx6ZabXF7pJqtnp8i28HhqkfQ/4/2bW6M1Cfkj/HOlaTm3xxfkXeJs4xBAiUBVHH9J4ZXh4tUlx5wq49Q==;EndpointSuffix=core.windows.net")

    container_client = blob_service_client.get_container_client("empdetailsnew")
    #print(container_client.__dict__)
    blobs_list = container_client.list_blobs()
    for blob in blobs_list:
        blob_name.append(blob.name)

    blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=empdetailstorage;AccountKey=XfDymEx6ZabXF7pJqtnp8i28HhqkfQ/4/2bW6M1Cfkj/HOlaTm3xxfkXeJs4xBAiUBVHH9J4ZXh4tUlx5wq49Q==;EndpointSuffix=core.windows.net", container_name="empdetailsnew", blob_name=str(blob_name[0]))
    blob_data = blob.download_blob()
    byte_data = blob_data._current_content
    json_data = byte_data.decode('utf-8')
    print(type(json_data))
    res = re.findall(r'\{.*?\}', json_data)
    for i in res:
        details.append(json.loads(i))
    emp_data["data"]=details
    logging.debug(emp_data)
    logging.debug(type(emp_data))
    return jsonify(emp_data)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
