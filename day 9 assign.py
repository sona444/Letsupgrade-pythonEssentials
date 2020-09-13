print("question1")
! pip install pylint
! pip install unittest2

%%writefile check_prime_number.py
def prime(num):
    '''
    This is the main function which check out the given number is even or odd.
    '''
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            return print("It is a Prime Number")
    return print("It is not a Prime Number")
n = int(input("enter the number :"))
prime(n)
! pylint "check_prime_number.py"

%%writefile test.py
def capText(string_To_Cap):
    return string_To_Cap.title()
import unittest
import capitalizeText

class testPrimeNumber(unittest.TestCase):
    def testOne(self):
        result = capitalizeText.capText("anmol noor")
        self.assertEqual(result,"Anmol Noor") 
    def testSecond(self):
        result = capitalizeText.capText("this is a text string to test the unittest on a file")
        self.assertEqual(result,"This Is A Text String To Test The Unittest On A File")

print("question2")        
if __name__ == "__main__":
    unittest.main()
lst = list(range(1,1000+1))
def armstrong(lst):    
    for num in lst:
        order=len(str(num))
        s = 0
        temp = num
        while temp > 0:
            d = temp % 10
            s += d ** order
            temp //= 10
        if num == s:
            yield num
print(list(armstrong(lst)))
