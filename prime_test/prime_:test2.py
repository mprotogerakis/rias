import math

N = 77
print(f"N={N}")
g = 8
for i in range(2, 100):
    a = pow(g, i) % N
    print(f"{g}^{i}=>{a}")

