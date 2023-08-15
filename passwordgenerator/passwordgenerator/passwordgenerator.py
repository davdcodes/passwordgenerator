import random

print("========================")
print("   Password Generator")
print("========================")
print()

pnum = input("How many passwords would you like to generate? ")
plen = input("How long would you like your password(s) to be? ")

charlist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-!@#$%^&*()_"

print()
print("Recommended Passwords: ")

for i in range(0,int(pnum)):
    currpasslist = ""
    for j in range(0,int(plen)):
        currpasslist += (random.choice(charlist))
    print(currpasslist)

print()
print("Thank you for using the password generator!")
print()
        