from zipfile import ZipFile
import os


'''with ZipFile('input.zip') as myzip:
    files = myzip.namelist()
    for file in files:
        if file[-1] == "/":
            print('  ' * (file.count('/') - 1) + file.split('/')[-2])
        else:
            print('  ' * file.count('/') + file.split('/')[-1])'''


def get_files_sizes():
    for curr_dir, dirs, files in os.walk("test"):
        print(curr_dir, dirs, files)
    print()
    for curr_dir, dirs, files in os.walk("test"):
        for di_r in dirs:
            print(files)
    print()
    print(os.listdir())


get_files_sizes()
