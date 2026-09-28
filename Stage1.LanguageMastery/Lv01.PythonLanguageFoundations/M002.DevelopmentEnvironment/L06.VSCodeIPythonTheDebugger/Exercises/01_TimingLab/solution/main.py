import timeit


def time_per_call(func, number=1000):
    return timeit.timeit(func, number=number) / number


def fastest(candidates, number=1000):
    times = {name: time_per_call(func, number) for name, func in candidates.items()}
    return min(times, key=times.get)


def build_with_plus(n):
    text = ""
    for i in range(n):
        text += ("," if i else "") + str(i)
    return text


def build_with_join(n):
    return ",".join(str(i) for i in range(n))


# Why join usually wins: strings are immutable, so `text += piece` may create a brand-new,
# ever-longer string each time (O(n²) copying in the worst case). join computes the final
# size once and copies each piece once. (CPython sometimes optimises += in place, which is
# exactly why you MEASURE instead of assuming.)
