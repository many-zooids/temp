#! python3
# opera backup

from pathlib import Path
from datetime import datetime
import os, shutil

p = Path('D:/Files/Documents/Opera Backup')
po = Path('C:/Program Files/Opera') #check this ofc


#usuwa najstarszy folder z backupem jeśli jest ich więcej niż 5
folders = os.listdir(str(p))
if len(folders) >= 5:
    shutil.rmtree(Path(folders[0]))
    del folders[0]

######## ~~ PAMIĘTAJ ~~ ########
## Foldery muszą być nazywane ##
## w taki sposób, żeby pierw- ##
## szy alfabetycznie był naj- ##   <<< rozważ czy nie lepiej
## starszy - zawsze!!!        ##       wypróbować sobie moduł
################################       send2trash

#tworzy backup folder i backupuje
    
bckp = 'backup ' + str(datetime.now())
shutil.copytree(po / 'Opera', p / bckp)