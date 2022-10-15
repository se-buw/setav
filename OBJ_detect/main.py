import time
import cv2
import numpy as np



# Yolo model execution
net_obj = cv2.dnn.readNet("./weights/yolov3-tiny.weights", "./configuration/yolov3-tiny.cfg")
sections = []
with open("./configuration/coco.names", "r") as f:
    sections = [line.strip() for line in f.readlines()]
layerlist = net_obj.getLayerNames()
layers_result = [layerlist[i[0] - 1] for i in net_obj.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(sections), 3))

# Execution of webcam
capture = cv2.VideoCapture(0)
cam_font = cv2.FONT_HERSHEY_SIMPLEX

starting_time = time.time()
frame_id = 0


while True:
    # webcam setup
    a, frame = capture.read()
    frame_id += 1
    ht, wt, channels = frame.shape

    # Detecting objects (Extracting features)
    blob_obj = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net_obj.setInput(blob_obj)
    out_obj = net_obj.forward(layers_result)

    # Visualising data
    class_ids = [], confidences = [], boxes = []
    for out in out_obj:
        for det in out:
            outcome = det[5:]
            class_id = np.argmax(outcome)
            confidence = outcome[class_id]

            if confidence > 0.1:
                # detect of objects
                cent_x = int(det[0] * wt)
                cent_y = int(det[1] * ht)
                w = int(det[2] * wt)
                h = int(det[3] * ht)

                # co-ordinates of rectangle
                x = int(cent_x - w / 2)
                y = int(cent_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Non Max suppression
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.8, 0.3)

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            title = str(sections[class_ids[i]])
            confidence = confidences[i]
            color = colors[class_ids[i]]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, title + " " + str(round(confidence, 2)), (x, y + 30), cam_font, 3, color, 3)


    timeElapse = time.time() - starting_time
    fps = frame_id / timeElapse
    cv2.putText(frame, "FPS: " + str(round(fps, 2)), (40, 670), cam_font, .7, (0, 255, 255), 1)
    cv2.putText(frame, "press [esc] to exit", (40, 690), cam_font, .45, (0, 255, 255), 1)
    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if key == 27:
        print("[Videocapturing is stopped succesfully]")
        break
#end

capture.release()
cv2.destroyAllWindows()