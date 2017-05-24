

"""
客户端配置
"""

LOGIN_STATE = {
    "auth_True":"200",   #认证成功
    "auth_False":"400",  #认证失败
    "file_exit":"202",   #文件存在
    "file_no_exit":"402", #文件不存在
    "cmd_right":"201",  #命令正确
    "cmd_error":"401",  #命令错误
    "dir_exit":"203",   #目录已存在
    "dir_no_eixt":"403", #目录不存在
    "cmd_success": "204",  # 命令成功执行
    "cmd_fail": "404",  # 命令执行失败
    "size_enough": "205",  # 磁盘空间足够
    "size_empty": "405",  # 磁盘空间不足
}
