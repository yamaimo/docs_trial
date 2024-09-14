"""
This module provides a function to generate a fibonacci number by loop,
which is derived by tail recursion.
"""


def fibo(n: int) -> int:
    """
    Calculate a n-th fibonacci number by tail recursion loop.

    Parameters
    ----------
    n : int
        Specify the n-th.

    Returns
    -------
    int
        The n-th fibonacci number.

    Raises
    ------
    AssertionError
        When non-positive n is specified.
    """
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
