year=input( "Введите год:")
febraly=28
if float(year) % 4 == 0:
    febraly=29
answer=0
for i in range(0,febraly+1):
    b = list(map(int,str(i)))
    if len(str(i))==1:
        answer+=int(b[0])
    if len(str(i))==2:
        answer+=b[0]+b[1]
febraly=30
answer30=0
for i in range(0,febraly+1):
    b = list(map(int,str(i)))
    if len(str(i))==1:
        answer30+=b[0]
    if len(str(i))==2:
        answer30+=b[0]+b[1]
answer30=answer30*4
answer31=0
febraly=31
for i in range(0,febraly+1):
    b = list(map(int,str(i)))
    if len(str(i))==1:
        answer31+=b[0]
    if len(str(i))==2:
        answer31+=b[0]+b[1]
answer31=answer31*7
answer=answer31+answer30+answer
print(f"Ответ={answer}")