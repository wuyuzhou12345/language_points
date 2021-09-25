#计算某个文件中的注释行数
note_line = 0
with open('./list_reverse.py','r') as file:
    while True:
        content = file.readline()
        print(content)
        if not content:
            break
        if content.count('#') > 0:
            note_line+=1

print(note_line)
