
from itertools import combinations

items = [x for x in input("인형 각각에 쓰여진 숫자를 입력 : ").split()]
num = int(input("인형의 필요한 합 : "))

for i in range(1,len(items)+1):
    a = list(combinations(items,i))  # 조합으로 판단
    for j in a:
        total = 0
        for k in j:
            total+=int(k)
        if total == num:  
            r=[]
            for w in j:  # 오름차순 
                r.append(int(w))
                r.sort()
            print(r)
           

        



