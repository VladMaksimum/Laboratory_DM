def count_drob(k, n):
    a = []

    for i in range(k+1):
        a.append(n//1)

        n = 1 / (n-a[i])
    return a

def pkqk(k, a):
    p = [1, 3]
    q = [1, 2]

    for i in range(2, k+1):
        p.append(a[i] * p[i-1] + p[i-2])
        q.append(a[i] * q[i-1] + q[i-2])
    
    return p, q

k = 11
n = 3**(1/3)
a = count_drob(k, n)

p, q = pkqk(k, a)

print(1/(q[-2]*(q[-2] * q[-1])))