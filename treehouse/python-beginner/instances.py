def combiner(list):

    butt_strings = []
    butt_nums = []
    for butt in list:
        if isinstance(butt, str):
            butt_strings.append(butt)
        elif isinstance(butt, int) or isinstance(butt, float):
            butt_nums.append(butt)
    sum_butt_nums = str(sum(butt_nums))
    sum_butt_strings = "".join(butt_strings)
    return sum_butt_strings + sum_butt_nums


# print(combiner(["butt", 13.4, 9, 5]))


def combiner2(args):
    words = []
    nums = []
    for item in args:
        if isinstance(item, str):
            words.append(item)
        if isinstance(item, (int, float)):
            nums += item
    return nums

print(combiner2([12, "apple", 5.2, "dog", 8, 1, 12]))


