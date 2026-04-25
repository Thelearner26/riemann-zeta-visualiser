# Riemann Zeta Function Visualiser

## What Is This?
A Python project exploring the Riemann Hypothesis — one of the greatest 
unsolved problems in mathematics, worth $1,000,000 from the Clay 
Mathematics Institute.

## The Mathematics
The Riemann Zeta function is defined as:

ζ(s) = 1 + 1/2^s + 1/3^s + 1/4^s...

Euler discovered this equals a product over all primes simultaneously — 
secretly encoding every prime inside the function. Through Riemann's 
explicit formula, each non-trivial zero contributes one term to an infinite 
series that reconstructs the exact distribution of primes. De Moivre's 
theorem converts each complex zero into a real cosine term — meaning 
A level further maths is the precise mechanism powering the deepest 
unsolved problem in mathematics.

The Riemann Hypothesis states all non-trivial zeros lie on the 
critical line Re(s) = 1/2. Over 10 trillion zeros have been verified 
computationally — all sitting perfectly on this line.

Historically, after building the first electronic computer, the first 
thing Alan Turing did was use it to verify zeros of the Riemann zeta 
function — a perfect demonstration that pure mathematics and computer 
science are the same language.

## Versions

### v1 — Print Zeros
Computes and prints the first n non-trivial zeros of the zeta function.
Immediately shows all real parts sitting exactly at 0.5.

### v2 — Extract and Format
Separates real and imaginary parts, formats to 7 significant figures,
includes user input validation.

### v3 — Complex Plane Visualiser
Plots zeros on the complex plane with:
- Critical strip shaded (0 < Re(s) < 1)
- Critical line marked at Re(s) = 0.5
- Hover coordinates showing exact zero values

### v4 — Domain Colouring (cplot)
Visualises the entire zeta function across the critical strip using 
domain colouring — zeros emerge naturally as black points from the 
colour map rather than being placed manually.

## Libraries Used
- mpmath — high precision complex arithmetic and zeta function
- matplotlib — visualisation
- mplcursors — interactive hover coordinates

## What I Learned
- Complex number handling in Python
- mpmath library and arbitrary precision arithmetic
- matplotlib — scatter plots, domain colouring, custom styling
- How De Moivre's theorem connects to the Riemann Hypothesis
- Why zeros of the zeta function control prime distribution

## Resources
- Numberphile — Both the Riemann Hypothesis video
- mpmath documentation — mpmath.org
