def gcd(bigger, smaller):

    r = bigger % smaller
    if r == 0:
        return smaller
    else:
        bigger = smaller
        smaller = r
        return gcd(bigger, smaller)


def lcm(first, second):
    number = first * second/gcd(first, second)
    number = int(number)
    return number


def addFrac(frac1, frac2):

    denominator = lcm(frac1[1],frac2[1])
    numerator = (frac1[0]*frac2[1])+(frac2[0]*frac1[1])
    fracAns = (numerator, denominator)

    return fracAns


def subFrac(frac1, frac2):

    denominator = lcm(frac1[1],frac2[1])
    numerator = (frac1[0]*frac2[1])-(frac2[0]*frac1[1])
    fracAns = (numerator, denominator)

    return fracAns


def reduce(frac):

    gcdNum = gcd(frac[0],frac[1])
    numerator = frac[0]/gcdNum
    denominator = frac[1]/gcdNum
    reducedFrac = (numerator, denominator)

    return reducedFrac


sampleTuple1 = (5, 46)
sampleTuple2 = (6, 24)
sampleTuple3 = (100,5)


print("GCD = ",gcd(*sampleTuple1))
print("LCM = ",lcm(*sampleTuple1))
print("Added Fraction = ",addFrac(sampleTuple1, sampleTuple2))
print("Subtracted Fraction = ",subFrac(sampleTuple1, sampleTuple2))
print("Simplified = ",reduce(sampleTuple3))
