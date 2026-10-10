def miniMaxSum(arr):
    
    sum1 = 0
    sum2 = 0
    for i in arr:
        sum1 += i
    sum1 -= max(arr)
    for k in arr:
        sum2 += k
    sum2 -= min(arr)
    print(sum1 , sum2)
