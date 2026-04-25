import matplotlib.pyplot as plt
from mpmath import zetazero, re, im

number = int(input("How many first zeroes of Rimeann Zeta function ? "))

real_1 = []
imaginary_1 = []


for i in range(1 , number + 1 ):
    r_zero = zetazero(i)
    real_1.append(float(re(r_zero)))
    imaginary_1.append(float(im(r_zero)))

figure , graph = plt.subplots(figsize = (7 , 10))


figure.patch.set_facecolor('white')
graph.set_facecolor('#00FFFF')


graph.set_xlim(-0.5 , 1.5)
graph.set_ylim(-10 , max(imaginary_1)+5)

graph.axvspan(0 , 1 , alpha = 0.5 , color = "#005EAA")

graph.axvline(x = 0 , color = "#020304" , linewidth = 0.4)
graph.axhline(y = 0 , color = "#020304" , linewidth = 0.4)

graph.scatter(real_1 , imaginary_1 , color = "#020304" , s = 30)

graph.axvline(x = 0.5 , color = "#020304" , linewidth = 0.5)

graph.set_xlabel("Re" , color = "#020304" )
graph.set_ylabel("Im" , color = "#020304" )

graph.set_title("Riemann Zeta Zeroes" , color = "#072A08" )

graph.tick_params(color = "#020304" )

graph.grid(True , color = "#020304" , alpha = 0.2)

plt.show()
