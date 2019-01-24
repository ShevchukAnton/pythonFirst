import Chapter8.CountFromBy as counter

res = counter.CountFromBy(step=2)

for i in range(10):
    res.increment()
    print(res)
