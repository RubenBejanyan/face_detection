import os
from photo_maker import make_photo


def image_rename(image_path, new_name):
    if image_path == -1:
        return -1
    # crate directory 'photos' in our directory, if it already exist it's ok
    photos_directory_path = os.path.join('.', 'photos')
    os.makedirs(photos_directory_path, exist_ok=True)
    new_image_path = os.path.join(photos_directory_path, f'{new_name}.jpg')
    os.rename(image_path, new_image_path)
    return new_image_path


if __name__ == '__main__':
    image = make_photo()
    image_name = input('Please input image name: ')
    print(image_rename(image, image_name))
