def absolut(number):
    if number < 0:
        #number = number * -1
        number *= -1 # van olyan is, hogy:+=   -=  /=
        return number
        #a =5 esetén


        # a = 5
        # a /= 2
        # print(a)

a=int(input('Kérek egy számot: '))
# print(type=(a))
a = absolut(a)
print(f'A szám abszolút értáke:{a}')