def quick_sort(arr):
    if len(arr) <= 1:  
        return arr  

    pivot = arr[0]  
    smaller = []  
    bigger = []   

    for x in arr[1:]:  
        if x < pivot:
            smaller.append(x)  
        else:
            bigger.append(x)   

    return quick_sort(smaller) + [pivot] + quick_sort(bigger)  


arr = [10, 5, 1, 8, 2, 6]
sorted_arr = quick_sort(arr)
print("Sorted Array:", sorted_arr)