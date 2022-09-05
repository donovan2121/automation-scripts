import os, shutil
from pathlib import Path

default_dir = ('images', 'videos', 'audios', 'documents')
image = ('png', 'jpg', 'gif', 'webp')
video = ('mp4', 'mpeg')
audio = ('mp3', 'flac')
document = ('pdf', 'docx', 'xlsx', 'csv', 'txt')
found_files = []

def check_dir():
    for dir in default_dir:
        path_dir = Path.cwd() / dir
        if path_dir.exists() and path_dir.is_dir():
            print(f'The {dir} exists.')
        else:
            path_dir.mkdir()
            print(f'The {dir} has been created.')

def find_files(path):
    for file_type in (image, video, audio, document):
        for ext in file_type:
            file_list = list(path.glob(f'*.{ext}*'))
            if len(file_list):
                found_files.append(file_list)

# def move_files():
#     shutil.move()

check_dir()
find_files(Path.cwd())
print(found_files)

