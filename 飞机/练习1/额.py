# coding = utd-8
import zipfile


# filename = 'Desktop.zip'
# zipFile = zipfile.ZipFile(filename, "r")

# z = zipfile.ZipFile(filename, 'r')
# # 这里的第二个参数用r表示是读取zip文件，w是创建一个zip文件
# for f in z.namelist():
#     print(f)


# 打开我们的字典表
# passFile = open('zidian.txt')
# for line in passFile.readlines():
#     # 读取每一行数据（每一个密码)
#     password = line.strip('\n')
#     try:
#         zipFile.extractall(pwd=str.encode(password))
#         print('=========密码是:' + password + '\n')
#     # 如果密码正确退出程序
#         exit(0)
#     except Exception as ex:
#         pass

# for i in passFile.readlines():
#     pa = i.strip() #字符
#     print(pa)
#     pa2 = i.split()  #数组
#     print(pa2)


def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=str.encode(password))
        # 如果成功返回密码
        return password
    except:
        return


def main():
    zFile = zipfile.ZipFile("Desktop.zip", "r")
    # 打开我们的字典表
    passFile = open('zidian.txt')
    for line in passFile.readlines():

        # 读取每一行数据（每一个密码)
        password = line.strip('\n')
        guess = extractFile(zFile, password)
        if (guess):
            print("=========密码是：" + password + "\n")
            exit(0)


if __name__ == '__main__':
    main()
