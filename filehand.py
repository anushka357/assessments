#txt file - user input para in text file.
lines = []
print("Type 'END' on a new line to finish")
while True:
    line = input()
    if line.strip().upper() == 'END':
        break
    lines.append(line)
    para = '\n'.join(lines)
    
f = open(r'c:/Users/AnushkaShukla/Ffolder/Python Tutorial/user_para.txt', 'w+')
f.write(para)

with open(r'c:/Users/AnushkaShukla/Ffolder/Python Tutorial/user_para.txt') as f:
    print(f.read())

f.close()
