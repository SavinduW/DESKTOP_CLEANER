import os
import collections
from pprint import pprint
import time

#--------------------------------------------------------------------SAVINDU--------------------------------------------------------------------------------------------
while True:
    time.sleep(1)
    EXT_AUDIO = ['mp3', 'wav', 'raw', 'wma', 'mid', 'midi']
    EXT_VIDEO = ['mp4', 'mpg', 'mpeg', 'avi', 'mov', 'flv', 'mkv', 'mwv', 'm4v', 'h264']
    EXT_IMGS  = ['png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'psd', 'svg', 'tiff', 'tif']
    EXT_COMPR = ['zip', 'z', '7z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb']
    EXT_DOCS  = ['txt', 'ods', 'odt', 'tex', 'log']
    EXT_PDF = ['pdf', 'ppt', 'pptx']
    EXT_EXEL = ['csv', 'xls', 'xlsx']
    EXT_WORD = [ 'doc', 'docx']
    EXT_PY = ['py',]
    EXT_INO = ['ino']
    EXT_HTML = ['html'] 
    EXT_INSTL = ['dmg']
    EXT_ISO = ['iso']
    EXT_EXE = ['exe']    
    EXT_JAR = ['jar']
    EXT_INK = ['lnk']

    # Step 1 - (Optional) Create directories where we want to store the files
    BASE_PATH = os.path.expanduser('~')
    DEST_DIRS = ['Music', 'Movies', 'Pictures', 'Documents', 'Applications', 'Other']

    for d in DEST_DIRS:
        dir_path = os.path.join(BASE_PATH, d)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)

    # Step 2 - Map files from Downloads folder based on their file extension
    DOWNLOADS_PATH = os.path.join(BASE_PATH, 'Desktop/ClEAN')
    files_mapping = collections.defaultdict(list)
    files_list = os.listdir(DOWNLOADS_PATH)

    for file_name in files_list:
        if file_name[0] != '.':
            file_ext = file_name.split('.')[-1]
            files_mapping[file_ext].append(file_name)

    pprint(files_mapping)

# Step 3 - Move all files given a file extension to a target directory
    for f_ext, f_list in files_mapping.items():

        if f_ext in EXT_INSTL:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Desktop/ALL/Applications/OTHER', file))
                
        elif f_ext in EXT_EXE:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Desktop/ALL/Applications/EXE', file))

        elif f_ext in EXT_ISO:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Desktop/ALL/Applications/ISO', file))

        elif f_ext in EXT_AUDIO:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Desktop/ALL/Music', file))

        elif f_ext in EXT_VIDEO:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Desktop/ALL/Movies', file))

        elif f_ext in EXT_IMGS:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Desktop/ALL/Pictures', file))
            
        elif f_ext in EXT_COMPR:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Desktop/ALL/Compressed', file))

        elif f_ext in EXT_JAR:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Desktop/ALL/Other/MODS', file))

        elif f_ext in EXT_PY:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Desktop/ALL/CODE/PYTHON', file))

        elif f_ext in EXT_INO:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Desktop/ALL/CODE/ARDUINO', file))

        elif f_ext in EXT_DOCS:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Desktop/ALL/Documents/OTHER', file))

        elif f_ext in EXT_PDF:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Desktop/ALL/Documents/PDF', file))

        elif f_ext in EXT_WORD:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Desktop/ALL/Documents/WORD', file))

        elif f_ext in EXT_EXEL:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Desktop/ALL/Documents/EXEL', file))

        elif f_ext in EXT_HTML:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Desktop/ALL/Documents/HTML', file))

        elif f_ext in EXT_INK:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Desktop/ALL/Shortcut', file))

        else:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Desktop/ALL/Other/OTHER', file))


















