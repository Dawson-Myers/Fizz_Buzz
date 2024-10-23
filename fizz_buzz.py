import random
import fizz_buzz_art

print(fizz_buzz_art.logo)
print("The fizz buzz input generator. You will enter any whole number and you will see a list printed containing the fizz buz results.")

n = int(input("Enter Number: "))
list_num = []
for n in range (1, n+1):
    if n % 3 == 0 and n % 5 != 0:
        list_num.append("Fizz")
    elif n % 5 == 0 and n % 3 != 0:
        list_num.append("Buzz")
    elif n % 5 == 0 and n % 3 == 0:
        list_num.append("Fizz Buzz")
    else:
        list_num.append(str(n))
print(list_num)