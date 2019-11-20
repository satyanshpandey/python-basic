#the if-elif conditions:-

#Q no.1
#write a program for your driving license...!
#if your age is less_then_18 then you are not elegible for drive the car.
#if your age is 18 then you have to give the test.
#if your age is above 18+ then you are elegible for drive the car.

print("the if_else and elif conditions")
print("")
age=int(input('Enter your age: '))
if age<18 or age>85:
    print("you are not elegible for drive the car \n Sorry!")
elif age==18:
    print("we can't decide that you are elegible or not \n you have to give physical test \n Thank You")
else:
    print("you are elegible for drive the car \nCongratulations \n Thanks Python...!")



print("Thanks Python...!")
input()
