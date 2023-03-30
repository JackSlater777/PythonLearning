from zipfile import ZipFile

with ZipFile('myzip.zip', 'w') as ziparc:
    ziparc.write('logfile.txt')

# with ZipFile('archive.zip', 'r') as ziparc:
#     for fileinfo in ziparc.filelist:
#         print(fileinfo.filename)

