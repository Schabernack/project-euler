fibs = [1,2]


while True:
    x = fibs[len(fibs)-1] + fibs[len(fibs)-2]

    if x<4000000:
        fibs.append(x)
    else:
        break

print(sum([i for i in fibs if i%2==0]))
