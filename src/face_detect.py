import cv2
import numpy as np
from skimage import io

# find face in document
def face_detect(file_name):
    print(f'run face_detect., args: file_name: {file_name}')
    image = io.imread(file_name)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    # запускаем детектор лиц
    faces = face_cascade.detectMultiScale(image,
                                          scaleFactor=1.2,
                                          minNeighbors=3)

    if '.png' in file_name:
        detections = cv2.imread(file_name)
    else:
        detections = np.copy(image)  # создаем копию изображения для визуализации результатов
    for ind, (x, y, w, h) in enumerate(faces):
        if w < 35 and h < 35:
            continue
        cropped = detections[y:y + h, x:x + w]
        cv2.imwrite(f'output/output_image_{ind}.png', cropped)
        break
    print(f'finish face_detect.')


