import pandas as pd
import lcd_function
import time
def id_verification(Userid=9090):
  x=Userid
  #x=int(input("enter the valid_id"))
  #lcd_function.inputMsg()
  id_file=pd.read_csv("/home/pi/Desktop/Face_Recong_System/EmployeeDetails/EmployeeDetails.csv")
  Id=id_file["Id"].values
  #print(x)
  #print(Id)
  #print(Id)
  if x in Id:
    #print("yes")
     name_id=id_file[id_file["Id"]==x]["Name"]
     name_=name_id.values.tolist()
     #print(str(name_[0]))
     name_id=str(name_[0])
     #lcd_function.key_input(str(name_[0])+"\nlook at camera")
  else:
    name_id="WrongId"
  return name_id,x
   #print("enter valid id")
   #lcd_function.key_input(str(x)+"\n is Wrong_ID")
    
   

#print(id_verification())
