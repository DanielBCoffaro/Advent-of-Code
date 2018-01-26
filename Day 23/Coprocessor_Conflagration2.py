def theloop(b):
    for d in range(2,b+1):
        for e in range(2,b+1):
            if d*e==b:
                f=0
                return f

a=1
b=105700
c=122700
h=0
print(b)
print(c)
while True:
    # print("loop it")

    f=1
    #is b a prime number
    for i in range(2,b):
        if (b % i) == 0:
            f=0
            break
    # f=theloop(b)
    if  f==0:
        h=h+1

    if b==c:
        print(h)
        wait = input("PRESS ENTER TO CONTINUE.")
    b=b+17


# set b 57
# set c b
# jnz a 2
# jnz 1 5
# mul b 100
# sub b -100000
# set c b
# sub c -17000
# set f 1
# set d 2
# set e 2
# set g d
# mul g e
# sub g b
# jnz g 2
# set f 0
# sub e -1
# set g e
# sub g b
# jnz g -8
# sub d -1
# set g d
# sub g b
# jnz g -13
# jnz f 2
# sub h -1
# set g b
# sub g c
# jnz g 2
# jnz 1 3
# sub b -17
# jnz 1 -23
