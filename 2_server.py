import os
import ftplib
import time
import cv2
import numpy as np



server = 'telematics.transtrack.id'
user = '15874661a9be9feafb0'
password = 'b193a4a95ef9fb64'


nms_threshold = 0.2
thres = 0.45

classNames = 'person'
classFile = 'coco.names'
with open(classFile) as f :
    classNames = f.read().rstrip('\n').split('\n')

#print(classNames)

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    if os.path.isfile('queue.txt'):
        f = open('queue.txt')
        lines = f.read()
        imgname = lines.strip()
        print(imgname)

        print("Read queue.txt :", lines)
        ftp = ftplib.FTP(server, user, password)
        

        if os.path.isfile(imgname):
             
                img = cv2.imread(imgname) 
                # cv2.imshow('Output',img)
                # cv2.waitKey(5000)   
                classIds, confs, bbox = net.detect(img, confThreshold=thres)
                #print(classIds, bbox)
                bbox = list(bbox)
                confs = list(np.array(confs).reshape(1,-1)[0])
                confs = list(map(float,confs))
                indices = cv2.dnn.NMSBoxes(bbox,confs,thres,nms_threshold)

                count = 0
                for i in indices:
                    box = bbox[i]
                    if classNames[classIds[i]-1] == 'person'  :
                        x,y,w,h = box[0], box[1], box[2], box[3]
                        cv2.rectangle(img, (x,y),(x+w,y+h), color=(0,255,0), thickness=1)
                        # cv2.putText(img,classNames[classIds[i]-1].upper(),(box[0]+10,box[1]+20),
                        # cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
                        cv2.putText(img,'Person',(box[0]+10,box[1]+20),
                        cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
                        cv2.putText(img,str(int(confs[i]*100)) + "%",(box[0]+10,box[1]+40),
                        cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
                        
                        count+= 1 
                        
                    
                if count>0:
                    print(str(count) + " Human Detected")
                    
                    imgname_detect = imgname +'_detect.jpg'
                    cv2.imwrite(imgname_detect,img)

                    img_send = open(imgname, 'rb')
                    ftp.storbinary('STOR '+imgname, img_send)
                    img_send_detect = open(imgname_detect, 'rb')
                    ftp.storbinary('STOR '+imgname_detect,img_send_detect)
                    os.remove(imgname_detect)
                    print("Sending success")
                    #time.sleep(10)
                else :
                    print("no human")
                    #time.sleep(10)
                
                os.remove(imgname)           
        
        count = 0
        os.remove('queue.txt')                    
        open('mulai_interval.txt', 'w+')                
        
#print(bbox)
#for classId,confidence, box in zip(classIds.flatten(),confs.flatten(), bbox):
    # if classId == 1 :
    #         cv2.rectangle(img,box,color=(0,255,0),thickness=2)
    #         cv2.putText(img,classNames[classId-1],(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)    

             
           
        #ftp.quit()
        

    #cv2.imshow('output',img)
    
    print("waiting....")
    time.sleep(2)
