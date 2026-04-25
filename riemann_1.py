from mpmath import zetazero

number = int(input("How many first zeroes of Rimeann Zeta function ? "))

for i in range(1,number + 1):
    print (f"Zero {i} , {zetazero(i)}")