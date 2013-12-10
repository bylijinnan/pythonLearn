def checkio(fraction):
    numerator, denominator = fraction
    if numerator < 0 or denominator < 0:
        raise argparse.ArgumentTypeError("invalid input, must be positive integer")

    q, r = divmod(numerator, denominator)
    quotient = [q]
    remainder = [r]
    while r:
        r *= 10
        q, r = divmod(r, denominator)
        quotient.append(q)
        remainder.append(r)

        #repeated
        if isRepeated(remainder):
            break
    result = myFormat(quotient, remainder)
    print result
    return result


def myFormat(quotient, remainder):
    if isRepeated(remainder):
        fromIndex = remainder.index(remainder[-1])
        quotient.insert(fromIndex + 1, "(")
        quotient.append(")")
    if len(quotient) > 1:
        quotient.insert(1, ".")
    return "".join([str(x) for x in quotient])

def isRepeated(remainder):
    lastRemainder = remainder[-1]
    firstIndex = remainder.index(lastRemainder)
    lastIndex = len(remainder) -1
    return firstIndex != lastIndex

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #assert checkio([58,2]) == "29", "no remainder"
    assert checkio([58,23]) == "2.(5217391304347826086956)", "mind zero"
    #assert checkio([5, 3]) == "1.(6)", "5/3 The same, but bigger"
    #assert checkio([3, 8]) == "0.375", "3/8 without repeating part"
    #assert checkio([7, 11]) == "0.(63)", "7/11 prime/prime"
    #assert checkio([29, 12]) == "2.41(6)", "29/12 not and repeating part"
    #assert checkio([11, 7]) == "1.(571428)", "11/7 six digits"
