import os,sys
import stat
import urllib
url = '#https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-8.20.0-x64.bin'
os.chdir("/home/yaniv/Desktop")

pwd = os.system('pwd')
print(pwd)

####url####
#wget = os.system('wget https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-8.20.0-x64.bin')
os.system('ls -l')

os.chmod('atlassian-jira-software-8.20.0-x64.bin',stat.S_IEXEC)
os.system('ls -l')

#https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-8.20.0-x64.bin

#import wget
import subprocess



#filename = wget.download(url)
#os.mkdir('exmple')

#subprocess.run(["sudo -i"])



