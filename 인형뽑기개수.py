'''
놀이공원에 가면 인형 맞추기 게임이 있다.

한 놀이공원에는 인형에 숫자를 써놓고 인형 맞추기를 한다.

그런데 맞춘 인형의 숫자의 합이 특정한 값이 되는 경우에만 맞춘 인형을 가져 갈 수 있다.

가령 10개의 인형에 쓰여진 숫자가 각각 25 27 3 12 6 15 9 30 21 19이고 숫자의 합이 50이 되는 경우만 인형을 가져갈수 있다면 6 19 25가 쓰여진 인형을 맞춰야 인형을 가져 갈 수 있다.

이때 인형의 갯수와 각각의 숫자와 필요한 합을 입력받으면 맞춰야 하는 인형의 숫자를 출력하는 프로그램을 작성해 보자.

입력 - 첫줄에는 인형의 갯수와 필요한 합, 둘째줄에는 인형 각각에 쓰여진 숫자

예)

10 50

25 27 3 12 6 15 9 30 21 19

출력 - 필요한 합이 되는 인형 각각의 숫자를 오름차순으로 출력

예)

6 19 25
'''


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
           

        



