# Libraries

import random
import Functions as f

# Main variables :

intentos = 2
n_num = "Please, type a number from 1 to 15: "
w_num = "The number must be an integer from 1 to 15. Please, try again."
machine_n = int(random.randrange(1, 16))

# START

# Initial message:
print(f"Let's start. Guess the number to win a special prize!.")
print("The machine already chose.")

# Number of attemps that the user have to guess the number:
print(f"You have {intentos + 1} attempts! Good luck")

# We call the function :
winner = f.play(intentos, machine_n)

# Finally, print the final result.
f.final(winner, machine_n)
