#coding:utf-8
import threading
from datetime import datetime
import time,os
import smtplib
#from email.mime.text import MIMEText
from email.MIMEText import MIMEText
#from email.Header import Header
#from log import logger
import logging
import subprocess
import socket,fcntl,struct
def disk_stat():
    hd = {}
    disk = os.statvfs("/data")
    free = (disk.f_bavail * disk.f_frsize)
    total =(disk.f_blocks * disk.f_frsize)
    used  = (disk.f_blocks - disk.f_bfree) * disk.f_frsize
    try:
        percent = (float(used) / total) * 100
    except error:
#        get_log().info('calucate error')
	pass
    return percent
def get_log():
    logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='myapp.log',
    filemode='w')
    logger = logging.getLogger('root')
    return logger
def backup_time():
    now = time.mktime(datetime.now().timetuple())-60*2
    result = time.strftime('%Y%m%d', time.localtime(now))
    backupresult = str(result)
    return backupresult
def send_email(content):
 
    sender = "lgl15984@163.com"
    receiver = ["992975991@qq.com","luoguoling@mokylin.com"]
    host = 'smtp.163.com'
    port = 465
    msg = MIMEText(content)
    msg['From'] = "lgl15984@163.com"
    msg['To'] = "992975991@qq.com"
    msg['Subject'] = "backup check"
 
    try:
    	smtp = smtplib.SMTP()
    	smtp.connect('smtp.163.com:25')
#   smtp.ehlo()
#   smtp.starttls()
#   smtp.ehlo()
    
#        smtp = smtplib.SMTP_SSL(host, port)
        smtp.login(sender, '15984794312')
        smtp.sendmail(sender, receiver, msg.as_string())
#        getlog().info("send email success")
    except Exception, e:
#        get_log().error(e)
        pass
def get_ip(ifname):
    s  = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s',ifname[:15]))[20:24])

def check():
    percent = disk_stat()
#    get_log().info(percent)
    ip = get_ip('eth0')
    if int(percent) > 80:
        result = ip  + "   disusage: " + str(percent)
	print result
    elif int(percent) > 88:
	os.popen('rm -f /data/back/*')
    else:
        result = "false"
    return result
def task():
    while  True:
        result = check()
	if result == "false":
	    pass
	else:
            send_email(result)
    time.sleep(300*60)
def run_monitor():
    monitor = threading.Thread(target=task)
    monitor.start()
def createDaemon():
    #脱离父进程
    try:
        pid = os.fork()
        if pid > 0:
            os._exit(0)
    except OSError,error:
        print "fork #1 failed: %d (%s)" % (error.errno, error.strerror)
        os._exit(1)
    #修改当前的工作目录
    os.chdir('/')
    #脱离终端
    os.setsid()
    #重设文件创建权限
    os.umask(0)
    #第二次创建进程，禁止进程重新打开终端文件
    try:
        pid = os.fork()
        if pid > 0:
            print 'Daemon PID %d' % pid
            os._exit(0)
    except OSError,error:
        print "fork #1 failed: %d (%s)" % (error.errno, error.strerror)
        os._exit(1)
    run_monitor()
if __name__ == "__main__":
    createDaemon()
# if __name__ == "__main__":
#     run_monitor()




