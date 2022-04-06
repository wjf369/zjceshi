# coding = utd-8
import zipfile
from itertools import product


# filename = 'Desktop.zip'
# zipFile = zipfile.ZipFile(filename, "r")

# z = zipfile.ZipFile(filename, 'r')
# 这里的第二个参数用r表示是读取zip文件，w是创建一个zip文件
# for f in z.namelist():
#     print(f)


def bru(q):
    try:
        z = zipfile.ZipFile(filename, 'r')
    except FileNotFoundError:
        print('zip不存在')
        return
    global length
    passwords = product(chars, repeat=length)
    for passwd in passwords:
        passwd = ''.join(passwd)

        try:
            z.extractall(pwd=passwd.encode())
            print('密码为', passwd)
            return
        except Exception as e:
            print('错误密码', passwd)


filename = 'Desktop.zip'
zipFile1 = zipfile.ZipFile(filename, "r")

chars = "1234567890"

length = 6
bru(zipFile1)
