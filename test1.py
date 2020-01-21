'''import os



os.chdir("..")
for currentdir, dirs, files in os.walk('WEB. Работа с популярными форматами файлов (json, xml)'):
    print(currentdir, dirs, )files)
print(os.path.abspath("test")
'''

#import shutil

#shutil.copy('files/3/Описание.txt', 'files/Копия.txt')   # создает копию файла(1) с заданным именем(2)

#print(shutil.get_archive_formats())   # сообщает более развернутые имена расширений'''

#shutil.make_archive("arhive_1", "zip", root_dir='data')   # создает архив; принимает значеиние имени архива, типа и файлов для добавления в сам архив


'''from zipfile import ZipFile


with ZipFile("arhive_1.zip") as myzip:
    #myzip.printdir()
    info = myzip.infolist()
print(info[0].orig_filename)'''

import shutil


#shutil.make_archive("arhive_5", 'zip', root_dir="data")


'''from zipfile import ZipFile


with ZipFile("arhive_3.zip") as myzip:
    #myzip.printdir()
    info = myzip.infolist()
print(info)'''


'''from zipfile import ZipFile


with ZipFile("arhive_4.zip") as myzip:
    print(myzip.namelist())'''


'''from zipfile import ZipFile


with ZipFile("arhive_4.zip") as myzip:
    with myzip.open('test.txt', "r") as file:
        print(file.read())'''

'''from zipfile import ZipFile


with ZipFile("arhive_5.zip",  'w') as myzip:
    myzip.write('test.txt')
    print(myzip.namelist())'''


from zipfile import ZipFile


with ZipFile("arhive_5.zip", 'a') as myzip:
    myzip.extractall(path='arhive_5/1', members=None, pwd=None)
