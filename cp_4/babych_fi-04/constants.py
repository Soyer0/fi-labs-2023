from scipy.stats import norm

#n1 = 25
#beta1 = 1 / (2 ** n1)
#alpha1 = 0.01
#t_a1 = norm.ppf(1 - alpha1, loc=0, scale=1)
#t_b1 = norm.ppf(1 - beta1, loc=0, scale=1)
#print(beta1)
#print(alpha1)
#print(t_a1)
#print(t_b1)
# system of equations
#t_b1 = (N / 2 - C) / sqrt(N / 4)
#C = N / 4 + t_a1 * sqrt(3N / 16)
C1 = 71
N1 = 222

n2 = 26
beta2 = 1 / (2 ** n2)
alpha2 = 0.01
t_a2 = norm.ppf(1 - alpha2, loc=0, scale=1)
t_b2 = norm.ppf(1 - beta2, loc=0, scale=1)
print(beta2)
print(alpha2)
print(t_a2)
print(t_b2)
#system of equations
# t_b2 = (N / 2 - C) / sqrt(N / 4)
# C = N / 4 + t_a2 * sqrt(3N / 16)
C2 = 73
N2 = 229
