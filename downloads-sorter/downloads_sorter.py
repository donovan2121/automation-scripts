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
            print(f'The {dir} folder exists.')
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

def move_files(found_files, path):
    if len(found_files):
        for dir_name, files in found_files.items():
            for file in files:
                try:
                    shutil.move(str(file), str(path / dir_name / file.name))
                    print(f'Copying {file.name} to {dir_name}')
                except shutil.Error:
                    print(f'{file} already exists in destination path')

                

check_dir()
find_files(Path.cwd())
move_files(found_files, Path.cwd())


