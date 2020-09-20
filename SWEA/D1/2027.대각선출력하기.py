arr = ['#', '+', '+', '+', '+']

print(''.join(map(str, arr)))

for i in range(len(arr)-1):
    arr[i], arr[i+1] = arr[i+1], arr[i]
    
    print(''.join(map(str, arr)))