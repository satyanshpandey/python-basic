def find_vovel(s):
    l=['a','e','i','o','u']
    for i in s:
        if i in l:
            print("yes ")
        else:
            print("no")
s='god is greate'
find_vovel(s)