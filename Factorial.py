def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
num=int(input('enter number:'))
print('the factorial is:',factorial(num))
# output:=>
#               enter number:5
#               the factorial is: 120
