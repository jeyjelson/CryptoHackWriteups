# modular multiplicative inverse = (e×d)modϕ(N)=1

e = 65537
p = 857504083339712752489993810777
q = 1029224947942998075080348647219


#eulers totient of 'N'
N = (p-1) * (q-1)
# we are told that d≡e−1modϕ(N)d≡e−1modϕ(N)
d = pow(e, -1, N)

print(d)