import json, os, requests


subscription_key = "f14c956c6839404499b188309e23432f"
assert subscription_key
personGroupId="matellio"
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
FACE_ENDPOINT="https://matelliofacerecognition.cognitiveservices.azure.com/"


def face_train():
    #Request Body
    body = dict()

    #Request URL
    FaceApiTrain = FACE_ENDPOINT + '/face/v1.0/persongroups/'+personGroupId+'/train'

    try:
        # REST Call
        response = requests.post(FaceApiTrain, data=body, headers=headers)
        print("RESPONSE:" + str(response.status_code))

    except Exception as e:
        print(e)



def main():
    face_train()

if __name__ == '__main__':
    main()

