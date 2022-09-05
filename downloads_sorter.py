import os, shutil
from pathlib import Path

dir_file_dict = {'images': ('png', 'jpg', 'gif', 'webp'), 'videos': ('mp4', 'mpeg'), 
'audios': ('mp3', 'flac'), 'documents': ('pdf', 'docx', 'xlsx', 'csv', 'txt')}
# images = ('png', 'jpg', 'gif', 'webp')
# videos = ('mp4', 'mpeg')
# audios = ('mp3', 'flac')
# documents = ('pdf', 'docx', 'xlsx', 'csv', 'txt')
found_files = {}

def check_dir():
    for dir in dir_file_dict.keys():
        path_dir = Path.cwd() / dir
        if path_dir.exists() and path_dir.is_dir():
            print(f'The {dir} exists.')
        else:
            path_dir.mkdir()
            print(f'The {dir} has been created.')

def find_files(path):
    for dir_name, file_type in dir_file_dict.items():
        for ext in file_type:
            file_list = list(path.glob(f'*.{ext}*'))
            if len(file_list):
                # create a dict type with keys image,video,audio,
                found_files.setdefault(path / dir_name, file_list)

# def move_files(found_files):
#     if len(found_files):
#         for file_type in found_files:
#             for file in file_type:
#                 shutil.move()

check_dir()
find_files(Path.cwd())
print(found_files)

