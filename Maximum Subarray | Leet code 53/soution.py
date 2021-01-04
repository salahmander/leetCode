def maxSubArray(nums):
    max_counter = sum(nums)
    if len(nums) == 1:
        return nums[0]
    for i in range(len(nums)):
        temp_counter = sum(nums)
        for j in range(0, i+1):
            temp_counter = max(temp_counter, sum(nums[j:i+1]))

        max_counter = max(max_counter, temp_counter)

    return max_counter


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # answer  = 6
print(maxSubArray([-2, 1]))  # answer  = 1
print(maxSubArray([-2, -1]))  # answer  = -1
print(maxSubArray([1]))  # answer  = 1


def maxSubArray2(nums):
    max_sum = float("-inf")
    for i in range(0, len(nums)):
        running_sum = 0
        for j in range(i, len(nums)):
            running_sum += nums[j]
            max_sum = max(max_sum, running_sum)

    return max_sum


print(maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # answer  = 6
print(maxSubArray2([-2, 1]))  # answer  = 1
print(maxSubArray2([-2, -1]))  # answer  = -1
print(maxSubArray2([1]))  # answer  = 1


def maxSubArray3(nums):
    max_so_far = nums[0]
    max_ending_here = nums[0]

    for i in range(1, len(nums)):
        max_ending_here = max(max_ending_here + nums[i], nums[i])
        max_so_far = max(max_ending_here, max_so_far)

    return max_so_far

print(maxSubArray3([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # answer  = 6
print(maxSubArray3([-2, 1]))  # answer  = 1
print(maxSubArray3([-2, -1]))  # answer  = -1
print(maxSubArray3([1]))  # answer  = 1