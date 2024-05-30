'''
question : please display a pymarid with n input
1. boundary: 1~10 (self-defined)
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
    def hollow_triangle(self, n:int):
        
        for i in reversed(range(1,n+1)):
            str1 = ' ' * (i-1)
            str2 = '* ' * (n - (i-1))
            print(str1 + str2)
    

def get_input_value():
    num = input('請輸入一個1到10之間的整數: ')
    #目前自己定義邊界為可以輸入1~10, 如果要修改邊界可以自由調整
    try:
        n = int(num)
        if n < 1 or n > 10:
            raise InputOutOfRangeException('輸入的數字超出範圍!')
    except ValueError:
        raise InputOutOfRangeException('輸入的不是一個有效的整數!')
    s = solution()
    s.hollow_triangle(n)


if __name__ == "__main__":
    get_input_value()
