def quickSortHoare(arr):
    return arr

# http://homepages.math.uic.edu/~leon/cs-mcs401-s08/handouts/quicksort.pdf
# and in the course book, both pseudo codes can be found
# Implemented from the pseudo code and algorithm above
def quickSortLomuto(arr):
    start = 0
    finish = len(arr) - 1
    main_qsl(arr, start, finish)
    helper_qsl(arr, start, finish)
    return arr


def main_qsl(arr, start, finish):
    if start < finish:
        temp_start, temp_finish = helper_qsl(arr, start, finish)
        main_qsl(arr, start, temp_finish)
        main_qsl(arr, temp_start, finish)


def helper_qsl(arr, start, finish):
    # Picking the element in the middle as pivot
    pivot_index = (start + finish) // 2
    pivot = arr[pivot_index]

    temp_start = start
    temp_finish = finish
    go_on = True

    while go_on:
        temp_start, temp_finish = temp_value_finder_for_qsl(pivot, temp_start, temp_finish)
        #print("ts:", temp_start, "tf", temp_finish)
        if temp_start <= temp_finish:
            #print("swapping -> ", "ts:", temp_start, "tf", temp_finish)
            temp = arr[temp_start]
            arr[temp_start] = arr[temp_finish]
            arr[temp_finish] = temp
            temp_start += 1
            temp_finish -= 1
            if temp_start <= temp_finish:
                go_on = False
        else:
            temp = arr[start]
            arr[start] = arr[temp_finish]
            arr[temp_finish] = temp
            break

    return temp_start, temp_finish


def temp_value_finder_for_qsl(pivot, temp_start, temp_finish):
    for i in range(temp_start, len(arr)):
        if pivot > arr[i]:
            temp_start += 1
        else:
            break
    for i in range(temp_finish, 0, -1):
        if pivot < arr[i]:
            temp_finish -= 1
        else:
            break
    return temp_start, temp_finish

arr = [15,4,68,24,75,16,42]

qsh = quickSortHoare(arr)
print(qsh)
qsl = quickSortLomuto(arr)
print(qsl)

