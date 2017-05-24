"""核心代码"""
import settings
import paramiko
import threading
import os


class REMOTE_HOST(object):
    #远程操作主机
    def __init__(self, host, port ,username, password, cmd):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.cmd = cmd

    def run(self):
        """起线程连接远程主机后调用"""
        cmd_str = self.cmd.split()[0]
        if hasattr(self, cmd_str):      #反射 eg:调用put方法
            getattr(self, cmd_str)()
        else:
            #setattr(x,'y',v)is  equivalent  to   ``x.y=v''
            setattr(self, cmd_str, self.command)
            getattr(self, cmd_str)()  #调用command方法，执行批量命令处理

    def command(self):
        """批量命令处理"""
        ssh = paramiko.SSHClient()  #创建ssh对象
        #允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.host,port=self.port,username=self.username,password=self.password)
        stdin,stdout,stderr = ssh.exec_command(self.cmd)
        result = stdout.read()
        print("%s".center(50, "-") % self.host)
        print(result.decode())
        ssh.close()

    def put(self):
        """上传文件"""
        filename = self.cmd.split()[1]  #要上传的文件
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(filename, filename)
        print("put sucesss")

        transport.close()


def show_host_list():
    """通过选择分组显示主机名与IP"""
    for index, key in enumerate(settings.msg_dic):
        print(index + 1, key, len(settings.msg_dic[key]))
    while True:
        choose_host_list = input(">>>(eg:group1)").strip()
        host_dic = settings.msg_dic.get(choose_host_list)
        if host_dic:
            #print(host_dic)
            for key in host_dic:
                print(key, host_dic[key]["IP"])
            return host_dic
        else:
            print("NO exit this group!")


def interactive(choose_host_list):
    """根据选择的分组主机起多个线程进行批量交互"""
    thread_list = []
    while True:
        cmd = input(">>>").strip()
        if cmd:
            for key in choose_host_list:
                host, port, username, password = choose_host_list[key]["IP"], choose_host_list[key]["port"], \
                                                 choose_host_list[key]["username"], choose_host_list[key]["password"]
                func = REMOTE_HOST(host, port, username, password, cmd)  # 实例化类
                t = threading.Thread(target=func.run)  # 起线程
                t.start()
                thread_list.append(t)
            for t in thread_list:
                t.join()  # 主线程等待子线程执行完毕
        else:
            continue


def run():
    choose_host_list = show_host_list()
    interactive(choose_host_list)



