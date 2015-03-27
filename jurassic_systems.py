from time import sleep
import os

login_attempts = 0
max_attempts = 3
password = "Please"
login_successful = False

print("Welcome to Jurassic Park!")

while login_attempts < max_attempts:
  attemped_password = input("Password: ")
  if attemped_password != password:
    print("Incorrect password.")
    login_attempts += 1
  else:
    login_successful = True
    break

if login_successful == False:
  while True:
    print("Uh uh uh! Didn't say the magic word!")
    sleep(1)
  
else:
  print("Login successful! Welcome to your UNIX system.")
  nix_command = ""
  while True:
    nix_command = input("> ")
    if nix_command != "exit":
      os.system(nix_command)
    else:
      print("Hold on to your butts...")
      break
