import cv2
import torch


path_to_model = './yolov5'
path_to_train = 'yolov5/runs/train/exp/weights/best.pt'

model = torch.hub.load(path_to_model, 'custom', path = path_to_train, source='local')

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    frame = cv2.resize(frame, (640, 480))

    result = model(frame)
    df = result.pandas().xyxy[0]

    for ind in df.index:
        x1, y1 = int(df['xmin'][ind]), int(df['ymin'][ind])
        x2, y2 = int(df['xmax'][ind]), int(df['ymax'][ind])
        label = df['name'][ind]
        conf = df['confidence'][ind]
        text = label + ' ' + str(conf.round(decimals= 2))
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 2)
        cv2.putText(frame, text, (x1 + 10, y1 + 10), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)

    cv2.imshow('Video',frame)
    print(result.pandas().xyxy)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()