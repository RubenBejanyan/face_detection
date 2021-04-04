import dlib
import cv2 as cv
import numpy as np
from photo_maker import make_photo
from image_rename import image_rename


def face_detection(image_path):
    if image_path == -1:
        return -1
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
    image = cv.imread(image_path)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces = detector(gray)
    face_counter = len(faces)
    faces_params = {}
    if face_counter == 1:
        print(f'1 face detected')
    elif face_counter > 1:
        print(f'{face_counter} faces detected')
    else:
        print('No faces detected')
        return -1
    for index, face in enumerate(faces):
        # take detected face in rectangle
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 1)
        landmarks = predictor(gray, face)
        # draw landmarks for eyes(points 36-47) and nose(points 27-35) for every detected face
        for n in range(27, 48):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv.circle(image, (x, y), 3, (255, 0, 0), -1)
        nose_start, nose_end = landmarks.part(28), landmarks.part(31)
        nose_length = np.sqrt((nose_start.x - nose_end.x) ** 2 + (nose_start.y - nose_end.y) ** 2)
        # eye center in the middle of rectangle of points 37, 38, 40, 41
        # for find center enough find middle of any diagonal
        left_eye = ((landmarks.part(37).x + landmarks.part(40).x)//2, (landmarks.part(37).y + landmarks.part(40).y)//2)
        right_eye = ((landmarks.part(43).x + landmarks.part(46).x)//2, (landmarks.part(43).y + landmarks.part(46).y)//2)
        eye_distance = np.sqrt((left_eye[0] - right_eye[0]) ** 2 + (left_eye[1] - right_eye[1]) ** 2)
        faces_params.update({f'Person {index + 1}': [{'Nose': nose_length, 'Eyes': eye_distance}]})
    cv.imwrite(image_path, image)
    return faces_params


if __name__ == '__main__':
    photo = make_photo()
    new_name = input('Please input image name: ')
    face_params = face_detection(photo)
    face_params = face_detection('./image.jpg')
    renamed_image = image_rename(photo, new_name)
    print(face_params)
