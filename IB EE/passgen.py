import random
import passlib


def passwordgen(scheme="ulns:12-no"):
    schemelist = passlib.parse_scheme(scheme)
    passlist = []
    for schemefrag in schemelist:
        if (len(schemefrag) == 2):
            for i in range(0, int(schemefrag[1])):
                passlist.append(random.choice(
                    passlib.scheme_multilist(schemefrag[0])))
        if (len(schemefrag) == 1):
            random.shuffle(passlist)
    password = "".join(passlist)
    return password
