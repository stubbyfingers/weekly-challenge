def stats(nums):
    if nums == []:
        return None
    
    smallest = 0
    largest = 0
    sum = 0

    for i in nums:
        sum += i

        if smallest == 0 and largest == 0:
            smallest += i
            largest += i
        if smallest == i and largest == i:
            continue
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
    average = sum/len(nums)
    average = round(average, 2)
    return [smallest, largest, average]
    # print(smallest)
    # print(largest)
    # print(sum)
    # print(average)


print(stats([5]))