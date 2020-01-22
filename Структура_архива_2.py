from zipfile import ZipFile
import os
import shutil


shutil.make_archive("test", "zip", root_dir="test")
def human_read_format(size):
    if 0 <= size <= 2 ** 10:
        return f"{round(size)}Б"
    elif 2 ** 10 < size <= 2 ** 20:
        return f"{round(size / 2 ** 10)}КБ"
    elif 2 ** 20 < size <= 2 ** 30:
        return f"{round(size / 2 ** 20)}МБ"
    elif 2 ** 30 < size <= 2 ** 40:
        return f"{round(size / 2 ** 30)}ГБ"
    elif 2 ** 40 < size <= 2 ** 50:
        return f"{round(size / 2 ** 40)}ТБ"
    elif 2 ** 50 < size <= 2 ** 60:
        return f"{round(size / 2 ** 50)}ПБ"
    elif 2 ** 60 < size <= 2 ** 70:
        return f"{round(size / 2 ** 60)}ЭБ"


with ZipFile('test.zip') as myzip:
    files = myzip.namelist()
    for file in files:
        if file[-1] == "/":
            print('  ' * (file.count('/') - 1) + file.split('/')[-2])
        else:
            print('  ' * file.count('/') + file.split('/')[-1]
            + " " + human_read_format(os.stat(os.path.dirname(os.path.abspath(file.split('/')[-1]))).st_size))


