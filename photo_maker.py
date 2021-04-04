import cv2 as cv
import os


def make_photo():
    cv.namedWindow("camera")
    vc = cv.VideoCapture(0)
    while True:
        _, frame = vc.read()
        cv.imshow("Press 'a' key to capture image, 'Esc' to exit", frame)
        key = cv.waitKey(1) & 0xFF
        if key == ord('a'):
            cv.imwrite('image.jpg', frame)
            continue
        if key == 27:
            break
    vc.release()
    cv.destroyAllWindows()
    image_path = 'image.jpg'
    if os.path.isfile(image_path):
        return image_path
    else:
        print('No image made!')
        return -1


if __name__ == '__main__':
    print(make_photo())
