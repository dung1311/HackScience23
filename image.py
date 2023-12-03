import cv2
import torch
import gui
import text_to_speech

path_to_model = './yolov5'
path_to_train = 'yolov5/runs/train/exp/weights/best.pt'

model = torch.hub.load(path_to_model, 'custom', path = path_to_train, source='local')

def detect(file_path):
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    result = model(img)

    result.show()
    ids = str(result)
    if 'metal' in ids:
        text = 'This is metal, please throw it into trash can with label metal'
        text_to_speech.speak(text)
    elif 'glass' in ids:
        text = 'This is glass, please throw it into trash can with label glass'
        text_to_speech.speak(text)
    elif 'cardboard' in ids:
        text = 'This is cardboard, please throw it into trash can with label cardboard'
        text_to_speech.speak(text)
    elif 'paper' in ids:
        text = 'This is paper, please throw it into trash can with label paper'
        text_to_speech.speak(text)
    elif 'trash' in ids:
        text = "This is can not recycle, please throw it into the red trash can"
        text_to_speech.speak(text)
    elif 'plastic' in ids:
        text = "This is plastic, please throw it into trash can with label plastic"
        text_to_speech.speak(text)
        





