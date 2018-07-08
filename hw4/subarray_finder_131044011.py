import sys

# http://web.cs.ucdavis.edu/~bai/ECS122A/Maxsubarray.pdf
# https://en.wikipedia.org/wiki/Maximum_subarray_problem#Algorithm_2:_Divide_and_Conquer
# I used the algorithm in the link above and alter it in order to put it work for minimum sub array
# and return the minimum sub array as an array
# To do this, I first multiply all the element of the array by -1. Now we can simply use the algorithm
# I divide the array into 2 arrays recursively
# Each of the


def min_subarray_finder(inpArr):
    # if the array has only one element
    if len(inpArr) == 0:
        return 0
    begin = 0
    end = len(inpArr) - 1

    # Multiple all indexed by -1
    for i in range(len(inpArr)):
        inpArr[i] *= -1

    # Store minimum contiguous array
    outArr = []
    result = -1 * min_sub_array(inpArr, begin, end, outArr, 0)
    print("result:", result)
    outArr.reverse()
    return outArr


def min_sub_array(inpArr, start, finish, outArr, counter):
    if start == finish:
        return inpArr[start]

    mid = (start + finish) // 2
    # print("mid: ", mid)
    # print("(",start, mid, finish, ")")
    left_sub_array = min_sub_array(inpArr, start, mid, outArr, counter + 1)
    right_sub_array = min_sub_array(inpArr, mid + 1, finish, outArr, counter + 1)

    if finish % 2 == 1:
        right_sum = find_subarray_sum(inpArr, mid, finish, "right", outArr, counter)
        left_sum = find_subarray_sum(inpArr, start, mid, "left", outArr, counter)
    else:
        left_sum = find_subarray_sum(inpArr, start, mid, "left", outArr, counter)
        right_sum = find_subarray_sum(inpArr, mid, finish, "right", outArr, counter)


    total_sum = left_sum + right_sum
    #print("total sum:", total_sum, "left:", left_sum, "right:", right_sum)

    if left_sub_array < right_sub_array:
        if total_sum < right_sub_array:
            return right_sub_array
        else:
            return total_sum
    else:
        if total_sum < left_sub_array:
            return left_sub_array
        else:
            return total_sum


def find_subarray_sum(inpArr, start, finish, side, outArr, counter):
    #print(side, start, finish)
    #print("counter:", counter)
    if side == "left":
        sum_side = 0
        result = 0
        for i in range(finish, start, -1):
            sum_side += inpArr[i]
            if sum_side > result:
                if counter == 0:
                    print(i)
                    outArr.append(-1 * inpArr[i])
                #print(inpArr[i])
                result = sum_side
        #print("res:", result)
    else:
        sum_side = 0
        result = 0
        for i in range(start + 1, finish + 1):
            sum_side += inpArr[i]
            if sum_side > result:
                if counter == 0:
                    print(i)
                    outArr.append(-1 * inpArr[i])
                result = sum_side
        #print("res:", result)
    #print("*********************")
    return result


inpArr = [-1, -2, -3, -4]

msa = min_subarray_finder(inpArr)
print(msa)
#Output: [-4, -7, 5, -13]
print(sum(msa))


