def first_task(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return
    res = 0
    for i in range(1, 4):
        j = i
        count = 1
        while True:
            j += 3
            if j > n:
                break
            count += 1
        res += 2 ** (n - i) - 1
    return res + 1


def second_task(n, num_of_ways_to_attend):
    return str(num_of_ways_to_attend - first_task(n - 1)) + '/' + str(num_of_ways_to_attend)


def main():
    n = int(input())
    num_of_ways_to_attend = first_task(n)
    probability_to_miss_grad_cer = second_task(n, num_of_ways_to_attend)
    print("Answer of (1) = {}".format(num_of_ways_to_attend))
    print("Answer of (2) = {}".format(probability_to_miss_grad_cer))


if __name__ == "__main__":
    main()
