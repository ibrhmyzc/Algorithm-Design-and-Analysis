# I kept dividing the two sorted arrays by 2 . After each step, I compared both of their middle points
# in order to find what sides of which array should be eliminated. So there are two binary searches to find kth
# element, the complexity is O(logm + logn) where m=len(m) n=len(n)
# Worst Case Scenario happens when the index is the first or the last element


def find_kth_book_1(m, n, k):
    start_m = 0
    start_n = 0
    finish_m = len(m)
    finish_n = len(n)

    k = k - 1
    if len(m) > len(n):
        result = kth_book(m, n, start_m, start_n, finish_m, finish_n, k)
    else:
        result = kth_book(n, m, start_n, start_m, finish_n, finish_m, k)

    return result


def kth_book(m, n, start_m, start_n, finish_m, finish_n, k):
    # print("--------------------------------------------")
    # print("START: (", start_m, "-", finish_m, "),(", start_n, "-", finish_n, ")", "k =", k)
    # print(finish_m - start_m, ",", finish_n - start_n, "k =", k)

    if k > len(m) + len(n):
        return "invalid k"

    if start_m == finish_m:
        # print("return n", finish_n - 1)
        return n[start_n + k]
    elif start_n == finish_n:
        # print("return m", finish_m - k)
        return m[start_m + k]

    mid_point_m = (finish_m - start_m) // 2
    mid_point_n = (finish_n - start_n) // 2
    # print(mid_point_m, mid_point_n, k)
    # print(mid_point_m+mid_point_n, m[mid_point_m + start_m], n[mid_point_n+start_n])
    condition = mid_point_m + mid_point_n
    real_mid_point_m = mid_point_m + start_m
    real_mid_point_n = mid_point_n + start_n
    # print(real_mid_point_m, real_mid_point_n)
    if condition >= k:
        if m[real_mid_point_m] > n[real_mid_point_n]:
            # decrease m's finish position
            if finish_m % 2 == 1:
                finish_m -= 1
            finish_m -= mid_point_m
            # print("3(", start_m, "-", finish_m, "),(", start_n, "-", finish_n, ")", "k =", k)
            return kth_book(m, n, start_m, start_n, finish_m, finish_n, k)
        else:
            # decrease n's finish position(for shorter array)
            if finish_n % 2 == 1:
                finish_n -= 1
            if mid_point_n == 0:
                finish_n -= 1
            else:
                finish_n -= mid_point_n
            # print("4(", start_m, "-", finish_m, "),(", start_n, "-", finish_n, ")", "k =", k)
            return kth_book(m, n, start_m, start_n, finish_m, finish_n, k)
    else:
        if m[real_mid_point_m] > n[real_mid_point_n]:
            # increase n's start position by mid_point_n
            k = k - mid_point_n - 1
            start_n += mid_point_n + 1
            # print("1(", start_m, "-", finish_m, "),(", start_n, "-", finish_n, ")", "k =", k)
            return kth_book(m, n, start_m, start_n, finish_m, finish_n, k)
        else:
            # increase m's start position by mid_point_m
            k = k - mid_point_m - 1
            start_m += mid_point_m + 1
            # print("2(", start_m, "-", finish_m, "),(", start_n, "-", finish_n, ")", "k =", k)
            return kth_book(m, n, start_m, start_n, finish_m, finish_n, k)


m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming","oop"]

book = find_kth_book_1(m,n,4)
print(book)
book = find_kth_book_1(m,n,6)
print(book)


# for i in range(len(m) + len(n)):
#     book = find_kth_book_1(m,n,i+1)
#     print(i+1,"-", book)


