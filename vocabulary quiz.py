#randint 함수 불러오기
from random import randint
# 파일불러오기 및 안내문
file = open('vocabulary.txt','r', encoding='utf-8')
print('프로그램을 종료하시려면, q를 입력하세요.')
# dict 만들기
dict = {}
for i in file:
    data = i.strip().split(': ')
    Korean_word = data[0]
    English_word = data[1]
    dict[Korean_word] = English_word

#key를 list로 만들기
list_keys = list(dict.keys())


#randint 함수를 이용하여 list_keys의 항목들을 임의로 배치시키는 list를 만든다.
length = int(len(list_keys))
new_list = []
temp = length + 2
temp_list = []
for i in range(0, length):
    random = randint(0, length-1)
    #중복검사
    while random in temp_list:
        random = randint(0, length - 1)
    new_list.append(list_keys[random])
    temp = random
    temp_list.append(temp)

#dict의 keys 입력 질문하기 및 정답 출력
for i in new_list:
    ans = input('%s: ' % i)
    if ans == dict[i]:
        print('맞았습니다!')
    elif ans == 'q':
        break
    else:
        print('틀렸습니다. 정답은 %s입니다.' % dict[i])

#파일 닫기
file.close()
