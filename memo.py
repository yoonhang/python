import os
import sys

# gugu
def gugu(n):
    result = []
            result.append(n*1)
            result.append(n*2)
            result.append(n*3)
            result.append(n*4)
            result.append(n*5)
            result.append(n*6)
            result.append(n*7)
            result.append(n*8)
            result.append(n*9)

gugu(n)







################################################################
''' 메모장 만들기
option = sys.argv[1]
memo = sys.argv[2]

print(option)
print(memo)

if option == '-a':
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)

space_content = tab_content.replace("\t", " "*4)    
'''



