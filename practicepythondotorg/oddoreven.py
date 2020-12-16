def is_divisible(numerator, denominator):
    if numerator % denominator == 0:
        return True
    else:
        return False


user_num = int(input("Give me a number: "))
user_denom = int(input("Give me a number to divide your number by: "))
remainder = user_num % user_denom
if is_divisible(user_num, user_denom):
    print("Yes, {}, is divisible by {}.".format(user_num, user_denom))
else:
    print("No, {} is not divisible by {}. The remainder is {}".format(user_num, user_denom,
                                                                      remainder))

