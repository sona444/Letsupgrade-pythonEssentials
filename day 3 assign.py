print("question1")
altitude=int(input("Enter the altitude of plane in ft"))
if(altitude==1000):
    print("safe to land")
elif(altitude<5000):
    print("Bring down to 1000")
else:
    print("Turn Around")

print("\nquestion2")
flag=0
for item in range(1,200):
    for x in range(2,item):
        if item%x==0:
            break
    else:
        print(item)
   
