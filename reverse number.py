
def reverse_number(number):
    reverse=0
    while(number>0):
      reminder=number%10
      reverse=(reverse*10)+reminder
      number=number//10
    print("reverse number is ",reverse)
reverse_number(9876543210)
reverse_number(123456789)
reverse_number(125)

input()
