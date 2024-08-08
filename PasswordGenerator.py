#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



print("\t\tWelcome to Password Generator")
nletters=int(input("How many letters do you want:"))
nnumbers=int(input("How many numbers do you want:"))
ssymbols=int(input("How many symbols do you want:"))

passwordlist=[]
for i in range(0,nletters):
    passwordlist.append(random.choice(letters))

for i in range(0,nnumbers):
    passwordlist.append(random.choice(numbers))

for i in range(0,ssymbols):
  passwordlist.append(random.choice(symbols))

random.shuffle(passwordlist)

password=""
for i in passwordlist:
      password+=i
print(f"your password is:{password}")




