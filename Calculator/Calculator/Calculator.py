sum=0


while(True): 
    print('정수:', end=' ')
    a = input()
    if not a.isnumeric():
        print(a, '은 정수가 아닙니다.')
        continue  
   
    a = int(a)
    break

while(True): 
    print('연산자:', end=' ')
    b = input()
    break
    
while(True): 
    print('정수:', end=' ')
    d = input()
    if not d.isnumeric():
        print(d, '는 정수가 아닙니다.')
        continue  
   
    d = int(d)
    break

if b=="+":

    sum=a+d

if b=="-":

    sum=a-d

if b=="*":

    sum=a*d

if b=="/":

    sum=a/d


print(sum)


print('엔터 후 c를 입력하면 다시 입력 e를 입력하면 계산기가 종료:', end=' ')
sum2 = input()


while sum2=="c":

   while(True): 
    print('정수:', end=' ')
    q = input()
    if not q.isnumeric():
        print(q, '은 정수가 아닙니다.')
        continue  
   
    q = int(q)
    break 
   while(True): 
    print('연산자:', end=' ')
    w = input()
    break
   while(True): 
    print('정수:', end=' ')
    r = input()
    if not r.isnumeric():
        print(r, '는 정수가 아닙니다.')
        continue  
   
    r = int(r)
    break
   if w=="+":
    sum3=q+r
    if w=="-":
        sum3=q-r
    if w=="*":
        sum3=q*r
    if w=="/":
        sum3=q/r

    print(sum3)
    sum2=0
sum2=input("입력:")


if sum2=="e":
 print('end')




