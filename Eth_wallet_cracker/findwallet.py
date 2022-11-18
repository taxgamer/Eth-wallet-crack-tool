import web3
from web3 import Web3,HTTPProvider
import random
import math
import json
from tkinter import *
import time as t
import threading as tr
import os
lg = os.getlogin()
path = os.getcwd()+'\\'
global is_pressed
is_pressed = False
def find_wallet():
    global is_pressed
    is_pressed = not is_pressed
    print(is_pressed)
    t.sleep(1.1)
    is_pressed = not is_pressed
    print(is_pressed)
    try:
        sp = int(speed.get())
        if sp in range(1,11):
            flag3 = False
            global succ
            global text
            inside = []
            temp_index = 0
            provider = Web3(Web3.HTTPProvider('https://rpc.ankr.com/eth'))
            words = json.load(open(f'C:\\Users\\{lg}\\Desktop\\tradin_bot\\words.json'))
            tries = 0
            fl2 = False
            succ = []
            flag = False
            zero = False
            while not flag and not is_pressed:
                
                y = ''
                for x in range(0,11):
                    rn = random.randint(0,len(words)-1)
                    
                    y += words[rn].replace('\n','') + ' '
                rn = random.randint(0,len(words)-1)
                y += words[rn].replace('\n','')
                
                with open(f'C:\\Users\\{lg}\\Desktop\\tradin_bot\\adrr.txt','w') as w:
                    w.write(y)
                web3.Account.enable_unaudited_hdwallet_features()
                try:
                    
                    acc = provider.eth.account.from_mnemonic(y)
                    if provider.eth.get_balance(acc.address) == 0 :
                        zero = True
                        
                        extra = 'Fail'
                    else:
                        fl2 = True
                        print('gotcha!')
                        succ.append(y)
                        extra = 'success'
                except Exception as e:
                    extra = 'Fail'
                l = f"\n{y}: {extra}"
                inside.append(l)
                
                if tries > 10:
                    inside.pop(0)
                else:
                    print(tries)
                cont = ''
                for ph in inside:
                    if ph.split(":")[1].replace(' ', '') == 'Fail':
                        if len(f'''Failed try:{ph}''')<200:
                            rem = 200 - len(f'''Failed try:{ph}''')
                            end_txt= f'''Failed try:{ph}'''
                            
                            for j in range(0,rem):
                                end_txt += ' '
                        else:
                            end_txt = f'''Failed try: {ph}'''
                        cont+= end_txt +'\n'

                    else:
                        if len(f'''Successful try: {ph}''')<200:
                            rem = 200 - len(f'''Successful try: {ph} with address:{acc.address}''')
                            end_txt= f'''Successful try: {ph}  with address:{acc.address}'''
                            root.config(background='green')
                            fl.config(background='green')
                            sp_lbl.config(background='green')
                            flag = not flag
                            for j in range(0,rem):
                                end_txt += ' '
                            if fl2:
                                fl2 = False
                                end_txt+='\nBut it has 0 ETH'
                        else:
                            
                            flag = not flag
                            root.config(background='green')
                            fl.config(background='green')
                            sp_lbl.config(background='green')
                            end_txt = f'''Successful try: {ph} with addy:{acc.address}'''
                            
                            if fl2:
                                fl2 = False
                                end_txt+='\nBut it has 0 ETH'
                        cont+= end_txt +'\n'
                te = f'''Tries: {tries}\n{cont}'''
                with open(f'C:\\Users\\{lg}\\Desktop\\tradin_bot\\x.txt','w') as T:
                    T.write(te)
                with open(f'C:\\Users\\{lg}\\Desktop\\tradin_bot\\x.txt','r') as T:
                    x = T.read()
                tries += 1
                if not flag3:
                    flag3 = not flag3
                    date = str(t.asctime()).replace(' ','_').replace(':',"_")
                text.set(x)
                
                if not os.path.exists(f'{path}logs'):
                    os.mkdir(f'{path}logs')

                if not os.path.exists(f'{path}logs\\log_{date}'):
                    
                    open(f'{path}logs\\log_{date}.log','a').close()
                
                with open(f'{path}logs\\log_{date}.log','r') as logdoc:
                    readd = logdoc.read()
                    
                    with open(f'{path}logs\\log_{date}.log','w') as logdoc:
                        if flag:
                            readd += f'Successful try: {ph}  with address:{acc.address}\n'
                            if fl2:
                                readd += 'But is has 0 ETH\n'
                        else:
                            readd += f'Failed try: {ph}\n'
                        logdoc.write(readd)
                        
                        
                t.sleep(1/sp)
        else:
            text.set('Speed should be a number between 1 and 10')
    except Exception as e:        
        text.set('Speed should be a number between 1 and 10')
        print(e)
        
def timer_find_wallet():
    tr.Thread(target=find_wallet).start()

global succ
global text


root = Tk()
root.configure(bg='red')
root.title('ETH wallet cracker')
root.geometry('1310x600')
root.grid_propagate(False)

fb = Button(root,text='Start',command=timer_find_wallet,bg='white')
fb.place(y=560,x=600)

text = Variable(root,'Press start')

fl = Label(root,textvariable=text,width=1000,font=('comic sans', 14),anchor='w',justify='left')
fl.configure(bg='red')
fl.place(x=0,y=0)

sp_lbl = Label(root,text='Choose the speed of the requests (1-10):',bg='red',font=('arial',12,'bold'))
sp_lbl.place(y=560,x=0)


speed = Entry(root,bg='white',width=4)
speed.place(y=562,x=310)
speed.insert(0,'5')


root.attributes()
root.mainloop()
try:
    if succ != []:
        print('Successful tries:')
        for s in succ:
            print(s)
    else:
        
        print('No successes')
except:
    print('No successes')