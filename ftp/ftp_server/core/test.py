
import os

s = b'\xe5\xae\xa2\xe6\x88\xb7\xe7\xab\xaf\xe5\xb7\xb2\xe5\x87\x86\xe5\xa4\x87\xe5\xa5\xbd\xe4\xb8\x8b\xe8\xbd\xbd'
print(type(s))
s1 = str(s,encoding="utf-8")
print(s1)

ss = "客户端已准备好下载"
b = bytes(ss, encoding="utf-8")
print(b)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME_PATH = os.path.join(BASE_DIR,"home")
print(HOME_PATH)

r = os.popen("dir %s" % BASE_DIR)
print(r.read(),type(r.read()))
message = r.read()
print("%s:message" % message)

print(message)

dir = BASE_DIR + "\\aa\\bb"
print(dir)

file_size1 = os.stat(r"C:\Users\Administrator\PycharmProjects\laonanhai\ftp\ftp_server\core").st_size
file_size2 = os.path.getsize(r"C:\Users\Administrator\PycharmProjects\laonanhai\ftp\ftp_server\core")
print(file_size1)
print(file_size2)


print("AA")

import os



def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    return size


size = getdirsize(r'C:\Users\Administrator\PycharmProjects\laonanhai\ftp\ftp_server')
print("There are %s" % size)




# Open a file
fo = open("foo", "r", encoding="utf-8")
print("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

line = fo.readline()
print("Read Line: %s" % (line))

# Get the current position of the file.
pos = fo.tell()
print("Current Position: %d" % (pos))

# Close opend file
fo.close()


