def get_unique_num(arr):
    result=0
    if len(arr) == 0 or 0 not in arr:
        result = 0
    else:
        arr.sort()
        more1 = [i for i in arr if i+1< len(arr) and arr[i+1] - i>1]
        if len(more1) == 0:
            result = max(arr) + 1
        else:
            result = min(more1) + 1
    return result

def get_middle_charator(data):
    length = len(data)
    odd_len = int((length+1)/2) -1
    even_len = int(length/2) -1
    result = data[odd_len] if length%2==1 else data[(even_len-1):(even_len+1)]
    return result

if __name__ == "__main__":
    arr = [0,1,2,3]
    result = get_unique_num(arr)
    middle_result = get_middle_charator(arr)
    print(result)
    print(middle_result)


