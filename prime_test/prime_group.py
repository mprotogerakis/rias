import math

p = 47
q = 59
N = p * q
print(f"N={N}")
r = 1
for j in range(2, 100):
    g = j
    for i in range(2, 100):
        a = pow(g, i) % N
        if a == 1:
            r = i
            break

    gcd_a = math.gcd(pow(g, r // 2) + 1, N)
    gcd_b = math.gcd(pow(g, r // 2) - 1, N)

    if gcd_a != 1 and gcd_b != 1:
        print(f"N%{r}=1")
        print(f"gcd({g}^{r//2}+1,{N})={gcd_a}")
        print(f"gcd({g}^{r//2}-1,{N})={gcd_b}")
        break