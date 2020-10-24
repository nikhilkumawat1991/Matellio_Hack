import json, os, requests

subscription_key = "17a60b69cfc54de5bf8f06406a02ae31"
assert subscription_key
personGroupId="matellio"
headers = {'Ocp-Apim-Subscription-Key': subscription_key}
FACE_ENDPOINT="https://facerecognitionresource.cognitiveservices.azure.com/"


def person_group():
    body = dict()
    body["name"] = "matellio"
    body["userData"] = "All employee images of matellio"
    body = str(body)

    #Request URL
    FaceApiCreateLargePersonGroup = FACE_ENDPOINT + '/face/v1.0/persongroups/'+personGroupId

    try:
        # REST Call
        response = requests.put(FaceApiCreateLargePersonGroup, data=body, headers=headers)
        print("RESPONSE:" + str(response.status_code))

    except Exception as e:
        print(e)

def main():
    person_group()

if __name__ == '__main__':
    main()


