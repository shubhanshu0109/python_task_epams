def get_fractions(a_b: str, c_b: str) -> str:
    """
    Add your code here  
    """
    num_a, denom = map(int, a_b.split('/'))
    num_c = int(c_b.split('/')[0])

    # Calculate sum of numerators
    sum_numerators = num_a + num_c

    # Create the result string
    result = f'{a_b} + {c_b} = {sum_numerators}/{denom}'

    return result