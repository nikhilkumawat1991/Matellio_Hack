import datetime
import os
import time
import led_function
import cv2
import pandas as pd
import merg_file
import numpy as np
import multiprocessing
import led_function
#-------------------------
def recognize_attendence():
    #os.chdir()
    #print(os.getcwd())
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel"+os.sep+"Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv("EmployeeDetails"+os.sep+"EmployeeDetails.csv")
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    count=0
    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height
    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    cont=0
    while True:
        ret, im = cam.read()
        #conf=0;
        result=""
        res=""
        #aa=""
        lis_=[]
        sh=""
        #confstr=0;
        #print(im)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5,minSize = (int(minW), int(minH)),flags = cv2.CASCADE_SCALE_IMAGE)
        #print(sh)
        for(x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x+w, y+h), (10, 159, 255), 2)
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])
            #print(conf)

            if conf < 100:

                aa = df.loc[df['Id'] == Id]['Name'].values
                confstr = "  {0}%".format(round(100 - conf))
                #print(Id)
                tt = str(Id)+"-"+aa
               


            else:
                Id = '  Unknown  '
                #aa="Unknown"
                tt = str(Id)
                confstr = "  {0}%".format(round(100 - conf))
                

            if (100-conf) > 55:
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = str(aa)[2:-2]
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]
               

            tt = str(tt)[2:-2]
            if(100-conf) > 55:
                tt = tt + "Recognized"
                res="Yes"
                #led_function.door_verifying()
                cv2.putText(im, str(tt), (x+5,y-5), font, 1, (255, 255, 255), 2)
                #print("Red Led Off")
                #print("White Led Off")
                #print("Green_LED ON")
                #time.sleep(2)
                #print("Green_LED Off")
                #cv2.destroyAllWindows()
                #print("Recognized successfully ")
               
        
            else:
                cv2.putText(im, "", (x + 5, y - 5), font, 1, (255, 0,0), 2)
                #print("Trying..")
                res="No"
                #print("Green_LED Off")
                #print("Red Led ON")
                #print("White Led Off")
                #lis_.append(res)
                #print(len(lis_))
               

            if (100-conf) > 55:
                cv2.putText(im, str(confstr), (x + 5, y + h - 5), font,1, (0, 255, 0),1 )
                #print("Green_LED Off")
            elif (100-conf) > 40:
                cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 255, 255), 1)

            else:
                cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 0, 255), 1)



        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('Recognition_Window', im)
        #k=60000
        #k = 0xFF & cv2.waitKey(60000)q
        if (cv2.waitKey(1) == ord('q')):
            break
        elif res=="Yes":
            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            Hour, Minute, Second = timeStamp.split(":")
            fileName = "Attendance"+os.sep+"Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
            attendance.to_csv(fileName, index=False)
            merg_file.merge_csv()
            print("Recognized successfully ")
            result="Yes"
            
            break
        elif res=="No" and count<30:
            time.sleep(.3)
            count=count+1;
            print(count)
        if count==30:
            result="fail"
        if result=="fail":
            led_function.door_fail_open()
            print("fail")
            break
    #print("Recognized successfully ")
    #cam.release()
    
    cv2.destroyAllWindows()
    cam.release()
    #cv2.destroyAllWindows()
    #return result


if __name__ == '__main__':
   print(recognize_attendence())
   
