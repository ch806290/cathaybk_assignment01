'''
question : please display a pymarid with n input
1. boundary: 1~10 (max)
2. catch exception
3. implement:
    a. create 2 loop, 1 for row, the other for column
    b. row: n
    c. column : 
    n =4, i =1, str1 = ' '*(i-1), str2 = '* '*(n - (i-1)). print(str1+str2)
    n =4, i =2, str1 = ' '*(i-1), str2 = '* '*(n - (i-1)). print(str1+str2)

    n =3, i =1, str1 = ' '*(i-1), str2 = '* '*(n - (i-1)). print(str1+str2)
    n =3, i =2, str1 = ' '*(i-1), str2 = '* '*(n - (i-1)). print(str1+str2)

example: 

input(1)
*

input(2)
 *
* *

input(3)
  *
 * *
* * *

input(4)
   *
  * * 
 * * *
* * * *
'''

class InputOutOfRangeException(Exception):
    pass

class solution:
    def pymarid_display(self, n:int):
        
        for i in reversed(range(1,n+1)):
            str1 = ' ' * (i-1)
            str2 = '* ' * (n - (i-1))
            print(str1 + str2)
    

def get_input_value():
    n = int(input('Please input a value for pymarid which you would like to display: '))
    if n < 1 or n > 100:
        raise InputOutOfRangeException('It is not a valid input, please try again!!!')
    s = solution()
    s.pymarid_display(n)


if __name__ == "__main__":
    get_input_value()
