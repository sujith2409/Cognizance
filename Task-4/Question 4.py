print("TO CHECK IF THE NUMBER IS A PALINDROME")
n=int(input("Enter a number:"))
n=str(n)
m=n[::-1]
print("The Reversed number is",m)
if n==n[::-1]:
    print("True")
else:
    print("False")
