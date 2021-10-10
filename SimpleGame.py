import random
import time
import sys
import os
clear = lambda:os.system('cls')

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

delay_print("\n===Game Gunting Batu Kertas===\n")
print("1.gunting\n2.batu\n3.kertas")
Hand = input("Pilih Gunting, batu atau kertas : ")
if Hand == '1':
    delay_print("Anda memilih gunting\n")
elif Hand == '2':
    delay_print("Anda memilih batu\n")
elif Hand == '3':
    delay_print("Anda memilih kertas")
bot = random.choice(['gunting', 'batu', 'kertas'])
'''
print("Bot memilih : ",bot)
'''
delay_print("Bot memilih : ") 
delay_print(bot)

print("\n================================")

if Hand == "1" and  bot == "batu":
    print("Anda kalah")
elif Hand == "1" and  bot == "kertas":
    print("Anda menang")
elif Hand == "1" and  bot == "gunting":
    print("Seri")

elif Hand == "2" and  bot == "gunting":
    print("Anda kalah")
elif Hand == "2" and  bot == "kertas":
    print("Anda menang")
elif Hand == "2" and  bot == "batu":
    print("Seri")

elif Hand == "3" and  bot == "gunting":
    print("Anda kalah")
elif Hand == "3" and  bot == "batu":
    print("Anda menang")
elif Hand == "3" and  bot == "kertas":
    print("Seri")
else:
    clear()
    print("MASUKAN SALAH !!!\nHarap Hanya Memasukan angka 1,2 dan 3")