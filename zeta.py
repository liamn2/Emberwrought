def zeta_partial_sum(s, N):
    """
    Computes the Nth partial sum of the Riemann Zeta function at s.

    Args:
        s: The complex or real number at which to evaluate the function.
        N: The number of terms to include in the partial sum.

    Returns:
        The Nth partial sum of the Riemann Zeta function.
    """
    if N < 1:
        raise ValueError("N must be a positive integer.")
    
    terms = [1 / (n**s) for n in range(1, N + 1)]
    partial_sum = sum(terms)
    return partial_sum

# Example usage:
s_value = 2
num_terms = 1000
result = zeta_partial_sum(s_value, num_terms)
print(f"The partial sum of zeta({s_value}) with {num_terms} terms is: {result}")

# For comparison, zeta(2) is known to be pi^2 / 6
import math
print(f"Known value of zeta(2) (pi^2 / 6): {math.pi**2 / 6}")
