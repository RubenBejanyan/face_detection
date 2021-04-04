from photo_maker import make_photo
from image_rename import image_rename
from face_detector import face_detection
import os
import json

if __name__ == '__main__':
    photo = make_photo()
    if photo != -1:
        new_name = input('Please input image name: ')
        detected_faces = face_detection(photo)
        new_photo = image_rename(photo, new_name)
        path = os.path.join('.', 'face_params.txt')
        if detected_faces != -1:
            with open(path, 'a+') as mf:
                json.dump(detected_faces, mf, indent=4)
