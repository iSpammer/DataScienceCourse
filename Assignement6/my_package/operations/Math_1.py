def get_average():
    str_arr = input().split(' ')
    arr = [int(num) for num in str_arr]
    average_num = sum(arr) / len(arr)
    return print("the average is ",average_num)
