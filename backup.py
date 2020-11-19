# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime
import subprocess as cmd
import numpy
logfile = input("Enter the LogFile name: ")

timelist = np.array(["00","01","02","03","04","05","06","07","08","09"])
addon = np.array([str(i) for i in np.arange(10,24)])

fullhourlist =[i+":00:00" for i in list(np.append(timelist, addon))]
while True:
    clock = str(datetime.datetime.now())[:19]
    if clock[-8:] in fullhourlist:
        try:
            cmd.run('cp ~/documents/customerB/counter/'+logfile+' ~/documents/customerB/counter/LogFile_Copies/'+logfile[:-4]+clock+'.exe')
            cmd.run("git checkout xwork", check=True, shell=True)
            cp = cmd.run("git add .", check=True, shell=True)
            print(cp)
            cmd.run("git commit -m 'Update at"+clock+" '", check=True, shell=True)
            print(cp)
            cmd.run("git push origin xwork", check=True, shell=True)
            print(cp)
        except:
            pass