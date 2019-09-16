# coding:utf-8
# jack_xie
# 模拟ssh登录， 获取指定路径下面的文件
import paramiko


# 创建一个链接
def sshClientCMd(hostname, port, username, password, cmd):
    # ssh登录linux 服务器
    paramiko.util.log_to_file("paramikko.log")
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    s.connect(hostname=hostname, port=port, username=username, password=password)
    try:
        stdin, stdout, stderr = s.exec_command(cmd)
        print("\033[21:1m", stdout.read().decode())
    except:
        print('%s Error\n' % hostname)
    s.close()
