import os
from datetime import datetime
import subprocess
import pandas as pd

command = "nmap "
flags = "-sn -oX "
dir_path = os.path.dirname(os.path.realpath(__file__))
outputfnpath = '"' + dir_path + "/data/"
outputfnprefix = 'scanresults__'
targetfn = dir_path + "/Target.csv"
targetdf = pd.read_csv(targetfn)
targetIPv4 =targetdf['Target network IPv4'][0]
targetlist = list(targetIPv4)
targetlist[len(targetlist) - 1] = '*'
targetIPv4 = "".join(targetlist)
target = " " + str(targetIPv4)

now = datetime.now()
time_stamp = now.strftime("%d-%m-%Y_%H-%M-%S")
outputfn = outputfnprefix + time_stamp + '.xml"'

shell_command = command + flags + outputfnpath + outputfn + target

os.system(shell_command)

