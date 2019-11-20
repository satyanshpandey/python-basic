def palindrome(num):
    n=num
    rev=0
    while num!=0:
        rev=rev*10
        rev=rev+int(num%10)
        num=int(num//10)
    if n==rev:
        print(n,'is palindrome number')
    else:
        print(n,'is not palindrome')
palindrome(5597955)
input()
