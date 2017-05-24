
import os

print(os.getcwd())    #获取当前的工作目录
#C:\Users\Administrator\PycharmProjects\laonanhai\day9

# os.chdir("C:\\Users\\Administrator")  #切换目录
# print(os.getcwd())   #C:\Users\Administrator

#print(os.curdir)  #返回当前目录: ('.')
#print(os.pardir)  #获取当前目录的父目录字符串名：('..')

#os.makedirs(r"F:\a\b\c\d")   #递归创建目录
#FileExistsError: [WinError 183] 当文件已存在时，
# 无法创建该文件。: 'F:\\a\\b\\c\\d'

#os.removedirs(r"F:\a\b\c\d")
# 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推

#os.mkdir(r"D:\a")  #生成单级目录
#os.rmdir(r"D:\a")  #删除单级空目录，若目录不为空则无法删除，报错

#print(os.listdir("."))
#列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# C:\Users\Administrator\PycharmProjects\laonanhai\day9
# ['client_ssh.py', 'lib', 'os_modu.py', 'server_ssh.py',
#  'test_aa.py', '__init__.py']

#os.rename("test_aa.py", "test_bb.py")
#("oldname","newname")  重命名文件/目录


#print(os.sep)   #\
#输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"


#print(os.stat(r"."))
#获取文件/目录信息


#print(os.linesep)
#行终止符，win下为"\t\n",Linux下为"\n"


print(os.pathsep)
#输出用于分割文件路径的字符串;