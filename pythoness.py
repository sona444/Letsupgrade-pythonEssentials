##Question 1
print("Question 1\n")
x=[1,2,3]
print(x)
x.append(4)     ##appending
print(x)    
x.pop()         ##poping last element from the list
print(x)
x.reverse()     ##reversing order of elements in the list
print(x) 
x.sort()        ##sorting elements of the list
print(x)


##Question 2
print("Question 2\n")
dic={'a':1,'b':2,'c':3}
print(dic.items())          ##displays all item of dictionary
print(dic.keys())           ##displays all keys of the dictionary
print(dic.values())         ##displays all values of the dict 
dic.update({'d':4})         ##adds new element to the dict   
print(dic)
dic.clear()                 ##removes all elements of dictionary
print(dic)


##Question 3
print("Question 3\n")
se={"red","orange","blue",}
se.add("pink")              ##adds element to the set
print(se)
se.update(["1", "2"])       ##adds multiple items to the set
print(se)
print(len(se))              ##returns length of set
x=se.pop()                  ##deletes topmost element of the set
print(x)
se2={"3","4"}             
se3=se.union(se2)           ##joins to sets
print(se3)


##Question 4
print("Question 4\n")
tupp=("red","orange","purple")      
tupp2=(1,2,3)
print(len(tupp))            ##returns length of tupple
tupp3=tupp+tupp2            ##concatinate two tupples
print(tupp3)
print(tupp[2])              ##indexing in tupple
print(tupp.index('orange')) ##returns index of element in the tupple
print(tupp.count("red"))    ##counts how many times the element exist in typple


##Question 5
print("Question 5\n")
stri="   Hello. How are you?    "
print(stri)
print(stri.strip())         ##removes whitespaces from both sides
print(stri.upper())         ##converts all the letters to uppercase
print(stri.lower())         ##converts all letters to lowercase
print(stri.replace("H","S"))##replace parameter1 with parameter2 in string
print(stri[2:8])            ##string slicing
