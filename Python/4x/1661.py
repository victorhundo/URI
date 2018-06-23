while True:
    n = int(input())
    if(n == 0): break

    entrada = input()
    nums = [int(n) for n in entrada.split()]

    count = 0
    for i in range(1,n):
        if(nums[i - 1] < 0):
            count += abs(nums[i - 1])
        else:
            count += nums[i - 1]

        nums[i] = nums[i] + nums[i - 1]

    print(count)
        
