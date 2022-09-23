from sqlite3 import IntegrityError
import win32com.client

dm=win32com.client.Dispatch('dm.dmsoft')
dm.setDict(0, 'd:dict.txt')
dm.useDict(0)

intX=0
intY=0
#dm_ret = dm.FindStr(0,0,1000,1000,"登录","f0f0f0-909090",1.0,intX,intY)
#if dm_ret[0]>0:
#    dm.moveto(dm_ret[1],dm_ret[2])
ss = dm.moveto(300,300)
print ("find the word")
