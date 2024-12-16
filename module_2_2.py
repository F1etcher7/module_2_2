first = int(input())
second = int(input())
third = int(input())
if first == second == third :
    print (3)
if first == second != third or first == third != second or second == third != first :
    print (2)
elif first != second != third :
    print (0)