import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A = np.array(A)
    rows = A.shape[0]   # 2
    cols = A.shape[1]   # 3

    # Output has flipped size: cols × rows → 3 × 2
    output_matrix = np.zeros((cols, rows), dtype=int)
    
    for i in range(rows):
        for j in range(cols):
            output_matrix[j][i] = A[i][j]
        
    return output_matrix
             


    
    pass
