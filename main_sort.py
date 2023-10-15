from pathlib import Path
import shutil
import sys
import hw6
from sort import normilize

def handle_media(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)  # создаем папку
    new_file_name = target_folder / (normilize(file_name.stem) + file_name.suffix)
    file_name.replace(new_file_name)

def handle_audio(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)  # создаем папку
    new_file_name = target_folder / (normilize(file_name.stem) + file_name.suffix)
    file_name.replace(new_file_name)

def handle_video(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)  # создаем папку
    new_file_name = target_folder / (normilize(file_name.stem) + file_name.suffix)
    file_name.replace(new_file_name)

def handle_documents(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)  # создаем папку
    new_file_name = target_folder / (normilize(file_name.stem) + file_name.suffix)
    file_name.replace(new_file_name)

def handle_archive(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)  # создаем папку
    folder_for_file = target_folder / normilize(file_name.stem)
    folder_for_file.mkdir(exist_ok=True)
    try:
        shutil.unpack_archive(str(file_name.absolute()), str(folder_for_file.absolute()))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return
    file_name.unlink()

def handle_folder(folder: Path):
    try:
        folder.rmdir
    except OSError:
        print('Error during remove folder {folder}')

   
def main(folder: Path):
    hw6.scan(folder)
    for file in hw6.JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in hw6.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG') 
    for file in hw6.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in hw6.SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')

    for file in hw6.AVI_VIDEO:
        handle_video(file, folder / 'video' / 'AVI')
    for file in hw6.MP4_VIDEO:
        handle_video(file, folder / 'video' / 'MP4')
    for file in hw6.MOV_VIDEO:
        handle_video(file, folder / 'video' / 'MOV')
    for file in hw6.MKV_VIDEO:
        handle_video(file, folder / 'video' / 'MKV')

    for file in hw6.DOC_DOCUM:
        handle_documents(file, folder / 'documents' / 'DOC')
    for file in hw6.DOCX_DOCUM:
        handle_documents(file, folder / 'documents' / 'DOCX')
    for file in hw6.TXT_DOCUM:
        handle_documents(file, folder / 'documents' / 'TXT')
    for file in hw6.PDF_DOCUM:
        handle_documents(file, folder / 'documents' / 'PDF')
    for file in hw6.XLSX_DOCUM:
        handle_documents(file, folder / 'documents' / 'XLSX')
    for file in hw6.PPTX_DOCUM:
        handle_documents(file, folder / 'documents' / 'PPTX')

    for file in hw6.MP3_AUDIO:
        handle_audio(file, folder / 'audio' / 'MP3')
    for file in hw6.OGG_AUDIO:
        handle_audio(file, folder / 'audio' / 'OGG')
    for file in hw6.WAV_AUDIO:
        handle_audio(file, folder / 'audio' / 'WAV')
    for file in hw6.AMR_AUDIO:
        handle_audio(file, folder / 'audio' / 'AMR')
        
    for file in hw6.ARCHIVES_ZIP:
        handle_archive(file, folder / 'archives' / 'ZIP')
    for file in hw6.ARCHIVES_GZ:
        handle_archive(file, folder / 'archives' / 'GZ')
    for file in hw6.ARCHIVES_TAR:
        handle_archive(file, folder / 'archives' / 'TAR')
    
    for file in hw6.MY_OTHER:
        handle_media(file, folder / 'MY_OTHER')



    for folder in hw6.FOLDERS[::-1]:     #удаляем пустые папки после сортировки
        try:
            folder.name.replace(folder.name, normilize(folder.name))
            folder.rmdir()
        except OSError:
            print('Error during remove folder {folder}')  

if __name__ == "__main__":
    folder_process = Path(sys.argv[1])
    main(folder_process.resolve())