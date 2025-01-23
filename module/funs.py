def factorial(n: int) -> int:
    """
    This function computes factorial of n as input
    
    :param n: Number to compute factorial
    :return: n!
    :raises ValueError: If n < 0
    """
    if n < 0:
        raise ValueError

    res = n
    for num in range(2,n):
        res = res * num
    
    return res

def factorial_rec(n: int) -> int:
    """
    This function computes factorial of n recursively
    
    :param n: Number to compute factorial
    :return: n!
    :raises ValueError: If n 
    """
    if n == 1:
        return 1

    return n * factorial_rec(n - 1)