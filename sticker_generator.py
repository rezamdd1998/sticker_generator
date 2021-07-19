import os
from os import listdir
from os.path import isfile, join,exists
from PIL import Image

def percent_scale(x):
    return 512 / x

source_path = './media'
if not exists(source_path):
    print('The source path doesnt exist. Please make sure your source path sets correctly.')
    exit(0)
destination_path = './sticker'
if not exists(destination_path):
    print('The Destination path has been created.')
    os.mkdir(destination_path)
exts = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')
files = [file for file in listdir(source_path) if isfile(join(source_path, file)) and file.lower().endswith(exts)]

for file in files:
    image = Image.open(source_path+'/'+file)
    file_name = '.'.join(file.split('.')[:-1])
    h = image.height
    w = image.width
    if h >= w:
        percent = percent_scale(h)
        new_image = image.resize((int(w*percent), 512))
    else:
        percent = percent_scale(w)
        new_image = image.resize((512, int(h * percent)))
    new_image.save(f'{destination_path}/{file_name}.png')
    print(destination_path + '/' + file_name + '.png has been created!')
