import passlib

def cracker(scheme="ulns:12"):
    schemelist = passlib.parse_scheme(scheme)
    passfrags = [passlib.IterableLCP([passlib.scheme_multilist(
        schemefrag[0])], repeat=schemefrag[1]) for schemefrag in schemelist]
    guesses = passlib.IterableLCP(passfrags)
    return guesses


guesses = cracker("uls:8-n:4")
