from zipfile import ZipFile


with ZipFile('input.zip') as myzip:
    files = myzip.namelist()
    for file in files:
        if file[-1] == "/":
            print('  ' * (file.count('/') - 1) + file.split('/')[-2])
        else:
            print('  ' * file.count('/') + file.split('/')[-1])
