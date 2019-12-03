from random import shuffle as smoosh

def the_stuff():
    a = 10
    y = []
    m = 4
    t = 6

    while a > 3:
        a = a - 2
        y = y + [m - a * 2]
        t = 2 + t + 1

    the_other_stuff = set([18 - t for x in [1, 2, 10]])
    for g in y:
        the_other_stuff.add(int(g / ((1 + 4 + 2 - 3 + 1 + 5) / 5)))
        the_other_stuff.add(g)

    return  (the_other_stuff | {-a}) | {was // 2 for was in (the_other_stuff | {-a})}

def oh_my(b, a, c):
    return {((cricket ** 2) // 5) for cricket in {b + a + c * 2, b + a // 3 + c * 2, 10 // b + a // 3 + c * 2} if True or False}

def howdy(a):
    return int(sum(ord(c) for c in a)) % 100 // 5

a = (the_stuff() | oh_my( 1,  2, 0) | oh_my(-2, 2, -2))
wer = a | set([55 // 11]) | {howdy('sick dudesfsd'), howdy('a') ** 2, howdy('10234'), howdy('m')}

def probably_okay():
    return set(map(lambda x: int(abs(howdy(str(x))) ** (1 / 2)) % (howdy('m') * 2), the_stuff()))

x = {g % ((howdy('4') + 3) * 2) for g in (wer | {howdy('4') + 5} | {howdy('4') * 2 - 3} | {19, 21} | probably_okay() | {13} | oh_my(1, 2, 10) | oh_my(-2, 5, -2) | {11, 2, 4, 6, 8, 9})}

j = list(x)
smoosh(j)

print(''.join(chr(ord(chr(97)) + j[i]) for i in j))

