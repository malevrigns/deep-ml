def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # 1. 检查维度是否匹配：如果矩阵的列数不等于向量的长度，返回 -1
    if len(a[0]) != len(b):
        return -1
        
    ans = []
    
    # 2. 遍历计算点积
    for i in range(len(a)):
        row_sum = 0
        for j in range(len(b)):
            row_sum += a[i][j] * b[j]
        ans.append(row_sum)
        
    return ans