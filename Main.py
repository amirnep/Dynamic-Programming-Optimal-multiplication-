#Algorithm Design: Dr. Pira
#Chapter2 Project by Amir Nematpour - 981830281
#Shahid Madani University

import Class as c

n = int(input("How many matrix do yo want: ")) #Input some numbers
#i = int(input("Enter i: "))
#j = int(input("Enter j: "))

if __name__ == '__main__': #Run Program.
    a = c.algorithm(n)
    a.print_m()
    a.print_p()
    #a.print_order()

print()
quit = input("Please Press Enter To Exit.")
