"""
This module provides a function to generate a fibonacci number,
which is simply calculated according to the definition.
"""


def fibo(n: int) -> int:
    """
    Calculate a n-th fibonacci number according to the definition.

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
    return __fibo(n)


def __fibo(n: int) -> int:
    return 1 if n <= 2 else __fibo(n - 1) + __fibo(n - 2)


if __name__ == "__main__":
    import datetime as dt

    start = dt.datetime.now()

    for i in range(1, 41):
        print(f"fibo({i}): {fibo(i)}")

    end = dt.datetime.now()
    print(f"elapsed: {end - start}")
