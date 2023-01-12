import cv2 
from PIL import Image
import numpy as np
import torch
import os
#load model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

# frame = cv2.imread('D:\ylv5\drive-download-20230111T074839Z-001\IMG_20230111_135917_684.jpg')
k=0
os.chdir('drive-download-20230111T074839Z-001')
for img in os.listdir('D:\ylv5\drive-download-20230111T074839Z-001'):
    frame = cv2.imread(img)

    frame = cv2.resize(frame, (int(frame.shape[1]*0.4),int(frame.shape[0]*0.4)), interpolation = cv2.INTER_AREA)
    detections = model(frame)
    
    results = detections.pandas().xyxy[0].to_dict(orient = 'records')
    x = np.array(results)
    #filer
    frame_lss = []
    
    if (len(results)>0):
        i=0
        for result in results:
            accu = result['confidence']
            name = result['name']
            clas = result['class']
            
            if clas == 0 and accu >= 0.5:
                x_min = int(result['xmin'])
                y_min = int(result['ymin'])
                x_max = int(result['xmax'])
                y_max = int(result['ymax'])
                print(x_min,y_min,x_max,y_max)
                frame = frame[y_min-10:y_max+10, x_min-10 :x_max+10 ]
                # cv2.imshow('img', frame)
            
                path = 'D:\ylv5\out'
                
                cv2.imwrite(os.path.join(path , str(i)+img),frame)
            i= i+1
                
                #vex
                # cv2.rectangle(frame, (x_min,y_min), (x_max, y_max),(255,0,0), 3)
                # cv2.putText(frame, name, (x_min+3, y_min-10), cv2.FONT_HERSHEY_COMPLEX,1, (0,0,255),1)
                # frame = frame[y_min:y_max, x_min :x_max ]
                # frame_lss.append(frame)
                # i=0
                
            #     for frame_ls in frame_lss:
            #         cv2.imshow('img', frame_ls)
            #         # cv2.imwrite('D:\ylv5\out'+str(i)+img, frame_ls)
            #         path = 'D:\ylv5\out'
            #         cv2.imwrite(os.path.join(path , str(i)+img),frame_ls)
            #         i = i+1
                    
                        
            # else:
            #     pass
    else:
        pass       
    # i=0
            
    # for frame_ls in frame_lss:
    #     cv2.imshow('img', frame_ls)
    #     # cv2.imwrite('D:\ylv5\out'+str(i)+img, frame_ls)
    #     path = 'D:\ylv5\out'
    #     cv2.imwrite(os.path.join(path , str(i)+img),frame_ls)
        

# print('Original Dimensions : ',frame.shape)
# cv2.imshow('img', frame)
# cv2.waitKey(0)
        '''
        

#detect
#detect = model(frame)
detections = model(frame)

#print results
results = detections.pandas().xyxy[0].to_dict(orient = 'records')
x = np.array(results)
# print(x)

#filer
frame_lss = []
for result in results:
    accu = result['confidence']
    name = result['name']
    clas = result['class']
    if clas == 0 and accu >= 0.5:
        x_min = int(result['xmin'])
        y_min = int(result['ymin'])
        x_max = int(result['xmax'])
        y_max = int(result['ymax'])
        print(x_min,y_min,x_max,y_max)
        
        #vex
        # cv2.rectangle(frame, (x_min,y_min), (x_max, y_max),(255,0,0), 3)
        # cv2.putText(frame, name, (x_min+3, y_min-10), cv2.FONT_HERSHEY_COMPLEX,1, (0,0,255),1)
        frame = frame[y_min:y_max, x_min :x_max ]
        # frame_lss.append(frame)
        
i=0
        
for frame_ls in frame_lss:
    cv2.imshow('img', frame_ls)
    cv2.imwrite('haha'+str(i)+'.jpg', frame_ls)
    path = 'D:\ylv5\out'
    cv2.imwrite(os.path.join(path , str(i)),img)
    cv2.waitKey(0)
#     i=i+1
#     # cv2.waitKey(0)
        
        
        
        

# if predict_value>=0.5 and pred[5] == 1:
#         print(pred)
#         x_min = int(pred[0] /512 * frame.shape[1])
#         y_min = int(pred[1] /512 * frame.shape[0])
#         x_max = int(pred[2] /512 * frame.shape[1])
#         y_max = int(pred[3] /512 * frame.shape[0])'''''''''