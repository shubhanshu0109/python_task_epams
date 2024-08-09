from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    """
    Add your code here or call it from here   
    """


    result = []

    # Iterate through rows from row_start to row_end
    for i in range(row_start, row_end + 1):
        row = []
        # Iterate through columns from column_start to column_end
        for j in range(column_start, column_end + 1):
            # Calculate the product of i and j
            product = i * j
            row.append(product)
        result.append(row)



    return result

