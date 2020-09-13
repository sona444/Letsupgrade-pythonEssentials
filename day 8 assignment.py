print("question1")
def func1(func3):
    def func2():
        print("ENTER TWO NUMBERS")
        a=int(input("Enter ur 1st input :"))
        b=int(input("Enter ur 2nd input :"))
        func3(a,b)
    return func2
@func1
def func3(a,b):
    print(*[i for i in range(a,b) if i%2==0])
func3()

print("question2")
try:
    a=open("file1.txt","r")
    a.write("Thank you")
except:
    print("WARNING: Do not update file in read mode!")
finally:
    a.close()
k=open("file1.txt","r")
print(k.read())
