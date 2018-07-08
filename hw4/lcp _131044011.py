# First we find the string with minimum length
# I divide the list of strings into two parts and recursively keep doing it till It can not be divided by 2
# Then I compare their postfixes and return them to find the longest common postfix
# Then I compare these postfixes to the words I did not check yet


def longest_common_postfix(inpString):
    if len(inpString) == 1:
        return inpString[0]

    start = 0
    finish = len(inpString) - 1
    result = lcs(inpString, start, finish)

    # https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
    str_result = "".join(result)
    return str_result


def lcs(inpString, start, finish):
    #print("Start:", start, "Finish:", finish)
    if start == finish:
        return inpString[start]
    else:
        mid = (start + finish) // 2
        # group and compare words by dividing them into 2 groups
        left = lcs(inpString, start, mid)
        right = lcs(inpString, mid + 1, finish)
        post_fix = find_postfix(left, right)
        if len(post_fix) == 0:
            return ""
        else:
            return post_fix


def find_postfix(left, right):
    #print("left:", left,  "<=> right:", right)
    common_char = []

    if len(left) < len(right):
        max_char = len(left)
    else:
        max_char = len(right)

    for i in range(max_char):
        if left[len(left) - i - 1] == right[len(right) - i - 1]:
            #print("POS:", left[len(left) - i - 1], "-", right[len(right) - i - 1])
            common_char.insert(0, left[len(left) - i - 1])
        else:
            #print("NEG:", left[len(left) - i - 1], "-", right[len(right) - i - 1])
            break
    #print("Common char:", common_char)
    return common_char


inpStrings = ["absorptivity", "circularity", "electricity", "importunity", "humanity"]
lcp = longest_common_postfix(inpStrings)
print(lcp)
