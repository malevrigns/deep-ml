def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    ans = []
    j = 0
    for i in range(len(a[0])):
        temp = []
        for j in range(len(a)):
            temp.append(a[j][i])
        ans.append(temp)
    return ans