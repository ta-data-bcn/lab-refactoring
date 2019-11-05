
# coding: utf-8

# In[ ]:


import random
#variables 

attempts = 3
intentos = 2
n_num = "Please, type a number from 1 to 15: "
w_num = "The number must be an integer from 1 to 15. Please, try again."
winer = ''

#START

#initial message:
print(f"Let's start. Guess the number to win a special prize!. ")

machine_n=int(random.randrange(1,16))
print("The machine already chose.")

print(f"You have {attempts} attempts! Good luck")

def right_int():
    n_num = "Please, type a number from 1 to 15: "
    w_num= "The number must be an integer from 1 to 15. Please, try again."
    n_user=input(n_num)
   
    while not n_user.isdigit() or int(n_user) not in range(1,16):
        n_user = input(w_num)
        
    return int(n_user)

while intentos >= 0:
    n_user=right_int()
    print(n_user)
    if n_user > machine_n:
        print('The number is higher than the one the machine chose.')
        intentos-=1
        print(f'You have {intentos + 1} attempts left.')
        
    elif n_user < machine_n:
        print('The number is lower than the one the machine chose.')
        intentos-=1
        print(f'You have {intentos + 1} left.')
            
    elif n_user == machine_n:
        winer=True
        break
    

        
if winer:
    print("Congatulations, YOU WON!!")
else:
    print(f"the number chosed by the machine was: {machine_n}")
    print("GAME OVER")

