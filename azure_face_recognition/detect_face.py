import json, os, requests
import argparse

subscription_key = "17a60b69cfc54de5bf8f06406a02ae31"
assert subscription_key
personGroupId="matellio"
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
FACE_ENDPOINT="https://facerecognitionresource.cognitiveservices.azure.com/"


def face_detect():
    face_api_url = FACE_ENDPOINT + '/face/v1.0/detect'

    image_url = 'http://www.imagozone.com/var/albums/vedete/Matthew%20Perry/Matthew%20Perry.jpg?m=1355670659'


    params = {
        'detectionModel': 'detection_01',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    'returnFaceId': 'true'
    }

    response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})
    print(json.dumps(response.json()))

def main():
    face_detect()

if __name__ == '__main__':
    main()


