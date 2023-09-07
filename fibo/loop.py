def fibo(n: int) -> int:
    assert n > 0
    if n <= 2:
        return 1
    return __fibo(n - 3, 1, 1)


def __fibo(rest: int, prev_prev: int, prev: int) -> int:
    now = prev_prev + prev
    return now if rest == 0 else __fibo(rest - 1, prev, now)


if __name__ == "__main__":
    import datetime as dt

    start = dt.datetime.now()

    for i in range(1, 41):
        print(f"fibo({i}): {fibo(i)}")

    end = dt.datetime.now()
    print(f"elapsed: {end - start}")
