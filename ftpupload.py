import ftplib
import os
import time
from os.path import basename
from zipfile import ZipFile
from pathlib import Path
import ftputil

ftp = ftplib.FTP('gethestia.ir', 'gethesti', 'POno7Vpv[7+9H0')

ftp.cwd('hestia')

# print(ftp.dir())
fname = f'tobeuploaded-{time.time()}.zip'
with ZipFile(fname, 'w') as zipObj:
    # Iterate over all the files in directory
    for folderName, subfolders, filenames in os.walk(os.getcwd()):
        for filename in filenames:
            # create complete filepath of file in directory
            filePath = os.path.join(folderName, filename)
            print(filePath)
            # Add file to zip
            if '.zip' not in filename:
                zipObj.write(os.path.relpath(filePath, Path(os.getcwd()).absolute()))

file = open(fname, 'rb')
ftp.storbinary(fname, file)
