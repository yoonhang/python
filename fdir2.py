import os
import sys

#딕렉토리 리스트 출력하기
#들여쓰기도 주의(오류남)
def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == ".py":
                    print(full_filename)

    except PermissionError:
        pass

# 슬래쉬 방향 주의할것
search("C:/Users/com71/Downloads/study23")


################################################################
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



