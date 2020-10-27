import json, os, requests
import argparse


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, help="Path to the image")
ap.add_argument("-n","--name", required=True, help="id of employee")
args = vars(ap.parse_args())
print(args["name"])
print(args["path"])

subscription_key = "f14c956c6839404499b188309e23432f"
assert subscription_key
personGroupId="matellio"
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
FACE_ENDPOINT="https://matelliofacerecognition.cognitiveservices.azure.com/"

def create_person(personGroupId):
    #Request Body
    body = dict()
    body["name"] = args["name"]
    body["userData"] = args["name"]
    body = str(body)

    #Request URL 
    FaceApiCreatePerson = FACE_ENDPOINT + '/face/v1.0/persongroups/'+personGroupId+'/persons' 

    try:
        # REST Call 
        response = requests.post(FaceApiCreatePerson, data=body, headers=headers) 
        responseJson = response.json()
        personId = responseJson["personId"]
        print("PERSONID: "+str(personId))
        return personId
    
    except Exception as e:
        print(e)

def add_images(personGroupId, personId):

    headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-Key': subscription_key }

    #Request URL 
    FaceApiCreatePerson = FACE_ENDPOINT + '/face/v1.0/persongroups/'+personGroupId+'/persons/'+personId+'/persistedFaces' 

    for file in os.listdir(args["path"]):
        if file.startswith(args["name"]):
            with open(args["path"]+"/"+file, 'rb') as img:

                try:
                    # REST Call 
                    response = requests.post(FaceApiCreatePerson, data=img, headers=headers) 
                    responseJson = response.json()
                    persistedFaceId = responseJson["persistedFaceId"]
                    print("PERSISTED FACE ID: "+str(persistedFaceId))
    
                except Exception as e:
                    print(e)


def main():
    print("creating a person within the group")
    personId = create_person(personGroupId)
    print("adding the images now..!!")
    add_images(personGroupId, personId)
    


if __name__ == '__main__':
    main()
