def sint(binary_string):
    """Converts a two's complement binary string to a decimal integer."""
    
    n = len(binary_string)
    unsigned_int = int(binary_string, 2)
    
    # The MSB is 1 if the unsigned value is greater than or equal to 2^(N-1)
    if unsigned_int >= 2**(n - 1):
        # If the MSB is 1, the number is negative.
        # Subtract 2^N to get the correct negative value (two's complement conversion).
        return unsigned_int - 2**n
    else:
        # If the MSB is 0, the number is positive.
        return unsigned_int

