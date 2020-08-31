def binary_search(a, lo, hi, diff):
    ans1 = diff
    while hi >= lo:

        mid = lo + (hi - lo) // 2
        min_diff = diff - a[mid]
        if abs(min_diff) <= abs(ans1):
            ans1 = min_diff

        if min_diff == 0:
            return ans1
        elif min_diff > 0:
            hi = mid - 1
        else:
            lo = mid + 1

    if diff == ans1:
        return ans1
    else:
        a.remove(diff - ans1)
        return binary_search(a, 0, len(a) - 1, ans1)


n = int(input())
m = int(input())
array = list(map(int, input().split()))

add = sum(array)
mean = add // n

if mean != add:
    array = sorted(array)[::-1]
    if array[0] >= mean:
        print(add - array[0])
    else:
        least_diff = binary_search(array[1:], 0, m-2, mean-array[0])
        if least_diff < 0:
            print(add - (mean - least_diff))
        else:
            print(mean - least_diff)
else:
    print(add)

