import cv2

class objectDetect:
    def initialize():
        objectDetect.classNames = []
        objectDetect.classFile = "/home/daniel/document/piCamServer/Object/coco.names"
        with open(objectDetect.classFile,"rt") as f:
            objectDetect.classNames = f.read().rstrip("\n").split("\n")

        objectDetect.configPath = "/home/daniel/document/piCamServer/Object/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
        objectDetect.weightsPath = "/home/daniel/document/piCamServer/Object/frozen_inference_graph.pb"

        objectDetect.net = cv2.dnn_DetectionModel(objectDetect.weightsPath,objectDetect.configPath)
        objectDetect.net.setInputSize(320,320)
        objectDetect.net.setInputScale(1.0/ 127.5)
        objectDetect.net.setInputMean((127.5, 127.5, 127.5))
        objectDetect.net.setInputSwapRB(True)
    
    def getObjects(img, thres, nms, draw=True, objects=[]):
        classIds, confs, bbox = objectDetect.net.detect(img,confThreshold=thres,nmsThreshold=nms)
        #print(classIds,bbox)
        if len(objects) == 0: objects = objectDetect.classNames
        objectInfo =[]
        if len(classIds) != 0:
            for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
                #print(classId)
                className = objectDetect.classNames[classId - 1]
                if className in objects:
                    objectInfo.append([box,className])
                    if (draw):
                        cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                        cv2.putText(img,objectDetect.classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                        cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                        cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                        cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

        return img,objectInfo






if __name__ == "__main__":

    picam2 = Picamera2()
    camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)},
    lores={"size": (640, 480)}, display="lores")
    picam2.configure(camera_config)
    #cap = cv2.VideoCapture(0)
    #cap.set(3,640)
    #cap.set(4,480)
    #cap.set(10,70)
    picam2.start()
    time.sleep(1)
    while True:
        #success, img = cap.read()
        success = True
        img = picam2.capture_array()
        if success:
                result, objectInfo = getObjects(img,0.45,0.2)
                print(objectInfo)
                cv2.imwrite("Output.jpg",img)
        #cv2.waitKey(1)
        time.sleep(0.1)
