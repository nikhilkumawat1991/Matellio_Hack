import json, os, requests
import argparse
from PIL import Image
import base64

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
print(args["image"])


subscription_key = "f14c956c6839404499b188309e23432f"
assert subscription_key
personGroupId="matellio"
headers = {'Ocp-Apim-Subscription-Key': subscription_key }

FACE_ENDPOINT="https://matelliofacerecognition.cognitiveservices.azure.com/"

def face_detect_identify():
    headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-Key': subscription_key }
    # Request URL 
    FaceApiDetect = FACE_ENDPOINT + '/face/v1.0/detect?returnFaceId=true' 
    with open(args["image"], 'rb') as img:
        try:
            # REST Call 
            response = requests.post(FaceApiDetect, headers=headers, data=img) 
            responseJson = response.json()
            faceId = responseJson[0]["faceId"]
            print("FACE ID: "+str(faceId))
            identify_confidence(faceId)

        except Exception as e:
            print(e)

def identify_confidence(faceId):
    faceIdsList = [faceId]

    # Request Body
    body = dict()
    body["personGroupId"] = personGroupId
    body["faceIds"] = faceIdsList
    body["maxNumOfCandidatesReturned"] = 1 
    body["confidenceThreshold"] = 0.5
    body = str(body)

    # Request URL 
    FaceApiIdentify = FACE_ENDPOINT + '/face/v1.0/identify' 

    try:
        # REST Call 
        response = requests.post(FaceApiIdentify, data=body, headers=headers) 
        responseJson = response.json()
        print(responseJson)
        personId = responseJson[0]["candidates"][0]["personId"]
        confidence = responseJson[0]["candidates"][0]["confidence"]
        print("PERSON ID: "+str(personId)+ ", CONFIDENCE :"+str(confidence))
        identify_person(personId)
        
    except Exception as e:
        print("Could not detect")

def identify_person(personId):
    # Request URL 
    FaceApiGetPerson = FACE_ENDPOINT + '/face/v1.0/persongroups/'+personGroupId+'/persons/'+personId

    try:
        response = requests.get(FaceApiGetPerson, headers=headers) 
        responseJson = response.json()
        print("This Is "+str(responseJson["name"]))
    
    except Exception as e:
        print(e)


def main():
    face_detect_identify()

if __name__ == '__main__':
    main()


