

def interactive(self):
    """
    本模块用于客户端与服务端的交互
    """
    while True:
        cmd = input(">>>:").strip()
        if len(cmd) == 0:
            continue
        cmd_str = cmd.split()[0]  # 指令
        if hasattr(self, "cmd_%s" % cmd_str):  # 反射
            func = getattr(self, "cmd_%s" % cmd_str) #获得方法对应的内存地址
            func(cmd)
        else:
            self.help()