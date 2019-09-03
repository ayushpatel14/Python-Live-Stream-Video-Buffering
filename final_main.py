import cv2
import numpy as np
from time import time
from datetime import datetime
from os import path,getcwd,makedirs

cur_dir = getcwd()
final_dir = path.join(cur_dir, r'Output')
if not path.exists(final_dir):              #Check if Output Folder exist
   makedirs(final_dir)                      #creates Output folder in current direcctory
   print("Output Folder Created")


print("Reading Config.txt. Got ",end=" ")
try:
    with open("config.txt","r") as f:               #open config.txt
        data=f.read().split()
        x,y,z,speed=int(data[1]),int(data[3]),int(data[5]),float(data[7])
        print("X=",x,"Y=",y,"Z=",z,"Speed=",speed,end="\n\n")

except (OSError,IOError,ValueError) as e :
        print("Error Reading config.txt!! \nMake sure file exist in the same directory with this python file.")
        print("Confirm that there is a space between '=' and values of x,y & z.")
        print("Aborting!!")
        exit()
del data

print("Live Video Feed Starting")
cap=cv2.VideoCapture(0)                         # cv2.VideoCapture(a), here 'a' is camera index.
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))      # Basically in what order camera devices are attached
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))     # Starts from 0 if camera present.

buff=list()
frame=[]
count,flag=0,0

t_start=time()
t,t1=t_start, t_start
try:
    print("Press R to Record")
    while cap:
        t2=time()
        rec=cv2.waitKey(1)
        res, image = cap.read()
        cv2.imshow("Live Feed",image)
        count+=1

        if t2-t1 < 1.0:
            frame.append(image)

        if t2-t1 >= 1.0:
                buff.append(frame)
                t1=time()
                frame=[]

        if len(buff)== x and flag==0 :
            del buff[0]
            t=time()

        if flag ==1 and t2-t >y:
            print("Live Video Feed Exit")
            break
        if rec==27:
            print("\nAborting!!")
            cap.release()
            cv2.destroyAllWindows()
            exit()
        if rec==82 or rec==114:
            t=time()
            print("R Pressed")
            flag=1

    t_stop=time()
    cap.release()
    cv2.destroyAllWindows()
    print("\nLive Video Time: %.2f" %(t_stop-t_start),"& FPS: %.2f" %(count/(t_stop-t_start)))
    del frame,flag,image,t_stop, t_start,t,t2,count
except cv2.error as e:
        print("\nFailed To Read Camera!!\nCheck the camera index at line 27 of python file")
        print("Aborting")
        exit()

fps=0
bufflen=len(buff)
for i in range(bufflen):
    fps+=len(buff[i])
fps=(fps/(bufflen))*speed

t1=datetime.now()
t1 = str(t1.strftime("@%H-%M, %d %b"))			
t2="Output/Recorded{}.mp4".format(t1)
	
fourcc=cv2.VideoWriter_fourcc(*'mp4v')					 	
out = cv2.VideoWriter(t2,fourcc,fps,(w,h))

print("Record time:",bufflen,"sec & Fps: %.2f" %(fps/speed))
fps=int(1000/(fps))
k,ch=z,1
print("\nPress and hold key (other than ESC) to speed up the current playback.")
while(k>0):
    for i in range(bufflen):
        for j in range(len(buff[i])):
            cv2.imshow("Recorded",buff[i][j])
            if (k==z):
                out.write(buff[i][j])
            if cv2.waitKey(fps)==27:                # Press ESC to exit after the current iteration of video ends
                ch=0
                print("Exiting video play after current iteration of video ends")
    if ch==0:
        break
    k-=1

out.release()
del buff
cv2.destroyAllWindows()
