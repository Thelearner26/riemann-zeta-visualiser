from mpmath import cplot , zetazero , zeta , im 

number = int(input("How many first zeroes of Rimeann Zeta function ? "))

if number > 15 :
    print(" WARNING , this could take a while !!")

max_y = float(im(zetazero(number))) + 1

cplot(zeta , [-5 , 6] ,  [-max_y , max_y])
