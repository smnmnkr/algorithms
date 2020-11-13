import math, random

from sorts import bubblesort, heapsort, insertionsort, quicksort, mergesort


for n in (4, 10, 100, 500):

    for t in [
        [n] + [x for x in range(1, n)],
        [x for x in range(2, n + 1)] + [1],
        [x for x in range(1, n + 1)],
        [1 for _ in range(1, n + 1)],
        [random.randint(1, n) for i in range(n)],
    ]:

        print("[--")
        print("[-- input:", [t[0], t[1], "...", t[-2], t[-1]])
        print(
            "[-- O(n) = {:02}, O(n * log2(n)) = {:02}, O(n^2) = {:02}".format(
                len(t),
                math.ceil(len(t) * math.log2(len(t))),
                len(t) ** 2,
            )
        )
        print("[--")

        for sort in [
            bubblesort,
            heapsort,
            insertionsort,
            quicksort,
            mergesort,
        ]:

            result, metric = sort(t)
            print(
                "[-- @{:14} success: {:1}, total:{:8}, compares:{:8}, swaps:{:8}".format(
                    sort.__name__,
                    result == sorted(t),
                    metric.get("total"),
                    metric.get("compares"),
                    metric.get("swaps"),
                )
            )

        print("[--\n")
