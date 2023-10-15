import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCUM = []
DOCX_DOCUM = []
TXT_DOCUM = []
PDF_DOCUM = []
XLSX_DOCUM = []
PPTX_DOCUM = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
ARCHIVES_ZIP = []
ARCHIVES_GZ = []
ARCHIVES_TAR = []
MY_OTHER = []



REGISTER_EXTENSION = {
    "JPEG": JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUM,
    'DOCX': DOCX_DOCUM,
    'TXT': TXT_DOCUM,
    'PDF': PDF_DOCUM,
    'XLSX': XLSX_DOCUM,
    'PPTX': PPTX_DOCUM,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ARCHIVES_ZIP,
    'GZ': ARCHIVES_GZ,
    'TAR': ARCHIVES_TAR,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()

def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()

def scan(folder: Path):
    for item in folder.iterdir():
        #работа с папкой
        if item.is_dir(): #проверяем есть ли объект папка
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        #Работа с файлом

        extension = get_extension(item.name) #берем расширение
        full_name = folder / item.name # берем полный путь к файлу
        if not extension:
            MY_OTHER.append(full_name)
        else:
            try:                                     #проверяем расширения, если его нет в словаре то добавляем в неизвестные и другие
                ext_reg =  REGISTER_EXTENSION[extension]
                ext_reg.append(full_name)  #расфасовали по списку
                EXTENSIONS.add(extension) #добавили неизвестные скрипту расширения
            except KeyError:
                UNKNOWN.add(extension)
                MY_OTHER.append(full_name)

if __name__ == '__main__':
    folder_process = sys.argv[1]
    scan(Path(folder_process))

