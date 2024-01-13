import sys
sys.stdin = open('CodeForces/input.txt', 'r')
sys.stdout = open('CodeForces/output.txt', 'w')

def getInput():
    N = int(input())
    ranges = []
    for i in range(N):
        ranges.append([int(x) for x in input().split()])
    
    Q = int(input())
    queries = [int(x) for x in input().split()]
    return (ranges, queries)

def bin_search(arr, k):
    l = 0; h = len(arr)-1
    while l <= h:
        mid = (l+h)//2
        if arr[mid] == k:
            return mid
        elif (mid == 0 or arr[mid-1] < k)and arr[mid] > k:
            return mid
        elif mid == len(arr)-1 and arr[mid] < k:
            return -1
        elif arr[mid] > k:
            h = mid - 1
        else:
            l = mid + 1

    return -1

def f():
    ranges, queries = getInput()
    ranges.sort()
    output = []
    final_range = [ranges[0]]
    cumulative_count_eles = [ranges[0][1]-ranges[0][0]+1]
    for i in range(1, len(ranges)):
        if final_range[-1][1] >= ranges[i][0]:
            final_range[-1][1] = max(final_range[-1][1], ranges[i][1])
            cumulative_count_eles[-1] = final_range[-1][1]-final_range[-1][0]+1
        else:
            final_range.append(ranges[i])
            cumulative_count_eles.append(ranges[i][1]-ranges[i][0]+1+cumulative_count_eles[-1])
    
    print(cumulative_count_eles)
    print('Final range', final_range)
    for i in queries:
        # flag_element_present = False
        ans = bin_search(cumulative_count_eles, i)
        if ans == -1:
            output.append(-1)
        else:
            if ans == 0:
                output.append(final_range[0][0]+i-1)
            else:
                output.append(final_range[ans][0]+i-cumulative_count_eles[ans-1]-1)
        # temp = i
        # k = 0
        # while k < len(final_range):
        #     if final_range[k][1]-final_range[k][0]+1 >= temp:
        #         output.append(final_range[k][0]+temp-1)
        #         flag_element_present = True
        #         break
        #     else:
        #         temp -= final_range[k][1]-final_range[k][0]+1
        #     k += 1

        # if not flag_element_present:
        #     output.append(-1)
    
    print(output)




f()