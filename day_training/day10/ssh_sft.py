import paramiko
transport = paramiko.Transport(('192.168.179.133', 22))
transport.connect(username='root', password='zcl')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/from_windows.py
#sftp.put('test', '/tmp/test_from_windows')
# 将remove_path 下载到本地 local_path
sftp.get('/root/install.log', 'fromlinux.txt')

transport.close()