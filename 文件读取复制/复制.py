# file_r = open("21.txt", 'r', encoding='utf-8')
# file_w = open("21附件.txt", 'w', encoding='utf-8')
#
# txt = file_r.read()
# file_w.write(txt)
#
# file_r.close()
# file_w.close()

file_r = open("21.txt", 'r', encoding='utf-8')
file_w = open("21附件.txt", 'w', encoding='utf-8')


while True:
    txt = file_r.readline()
    if not txt:
        break
    file_w.write(txt)


file_r.close()
file_w.close()
