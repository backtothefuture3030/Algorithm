import re
def Slump(a):
    while True:
        if re.search('^EF',a) and a[-1]=='G' :
            a=a[2:]
            while True:
                if a[0]=='F':
                    a=a[1:]
                else:
                    break
        elif re.search('^DF',a) and a[-1]=='G' :
            a=a[2:]
            while True:
                if a[0]=='F':
                    a=a[1:]
                else:
                    break
        elif a=='G':
            return True
        else:
            return False
            
def Slimp(a):
    while True:
        if len(a)==2 and a[0]=='A' and a[1]=='H':
            return True
        elif len(a)>2 and a[0]=='A' and a[-1]=='C':
            if a[1]=='B':
                a = a[2:-1]
            else:
                a=a[1:-1]
                if Slump(a)==True:
                    return True
                break
        else:
            return False
           
def Slurpy(count):
    i=0
    print("SLURPYS OUTPUT")
    while i<count:
        a = input("판단할 단어를 입력하세요 : ")
        idx = a.rfind('C')
        b = a[:idx+1]
        c = a[idx+1:]
        if a[0]=='A' and a[1]=='H':
            a=a[2:]
            if Slump(a):
                print("YES")
            else:
                print("NO")
                
        elif Slimp(b) and Slump(c):
            print("YES")
        else:
            print("NO")
        i+=1
    print("END OF OUTPUT")

Slurpy(int(input("횟수 : ")))