from mpmath import zetazero ,re , im

number = int(input("How many first zeroes of Rimeann Zeta function ? "))

accuracy = input("Would you like the answer to be more precise ? [y/n] ").lower()

real_1 = []
imaginary_1 = []

for i in range(1 , number + 1 ):
    r_zero = zetazero(i)
    real_1.append(float(re(r_zero)))
    imaginary_1.append(float(im(r_zero)))

while True :
    if accuracy == 'y':
        print(f"The real parts : {real_1}")
        print(f"The imaginary parts : {imaginary_1}")
        break
    elif accuracy == 'n':
        real_2 = [f'{i:.7g}' for i in real_1]
        imaginary_2 = [f'{i:.7g}'for i in imaginary_1]
        print(f"The real parts : {real_2}")
        print(f"The imaginary parts : {imaginary_2}")
        break
    else:
        accuracy = input("Would you like the answer to be more precise ? [y/n] ").lower()   



