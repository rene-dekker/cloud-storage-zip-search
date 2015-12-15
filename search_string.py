import StringIO
import zipfile
import os
"""
Hoi Bart, om een string te zoeken in de contents van de zipfiles,
moet je het volgende doen.
Plaats dit script in een folder en creeer nog een folder met de 
naam ../objects/

Vervolgens: 
open terminal en doe: 
$ gsutil -m cp -R gs://<bucketname>/<folder>/*201506* objects/
(bovenstaande matcht op alle files met 201506 in de naam en 
    kopieert deze naar de /objects/ folder)

Wacht tot alle files zijn gekopieerd. Daarna pas in dit script 
STRING_WE_ARE_LOOKING_FOR aan naar de string die je zoekt.

daarna run de python file (python 2.x):
$ python search_string.py

NB. Er zijn ook wel cli manieren om dit te doen zonder python.
Echter, je kunt dit scriptje eenvoudig aanpassen. 
.readlines() is een in-memory methode. Als files te groot zijn,
wil je het misschien aanpassen naar een buffered reader oid.
"""
STRING_WE_ARE_LOOKING_FOR = "bart"

for subdir, dirs, files in os.walk(os.getcwd()+'/objects/'):
    for file in files:
        print file
        archive = os.path.join(subdir, file)
        if '.zip' in archive:
            filehandle = open(archive, 'rb')
            zfile = zipfile.ZipFile(filehandle)
            for filename in zfile.namelist():
                textfile = zfile.open(filename).readlines()
                for line in textfile:
                    if STRING_WE_ARE_LOOKING_FOR in line:
                        print "\nString " + STRING_WE_ARE_LOOKING_FOR + " has been found in: " + archive
                        print "\tThe line looks like this: " + line
            zfile = zipfile.ZipFile(filehandle)
            filehandle.close()

