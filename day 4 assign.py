#armstrong number code day 4
i=1042000
while i<=702648265:
    temp=i
    summ=0
    while temp!=0:
        digit=temp%10
        summ=summ+digit**3
        temp=temp//10
    if i==summ:
        print("The first armstrong number is",i)
        break
    else:
         i=i+1
         continue
##it took a lot of time but it will print The first armstrong number is 1741725
