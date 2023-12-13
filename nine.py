import read_file

input = list(map(int, read_file.read_file('nine.input')))

sums = []
nums = input[:25]

for x in range(25):
    for y in range(25-x):
        if x != x+y:
            sums.append(nums[x]+nums[x+y])

def a():
    for i in range(len(input)-25):
        x = input[i+25]
        if x not in sums:
            return x
        r = nums.pop(0)
        for n in nums:
            sums.remove(n+r)
            sums.append(x+n)
        nums.append(x)

result_a = a()
print(result_a)

def b():
    start_index = 0
    end_index = 0
    r_sum = 0
    while True:
        if r_sum > result_a:
            r_sum -= input[start_index]
            start_index += 1
            continue
        if r_sum == result_a:
            print(start_index, end_index)
            a = input[start_index:end_index]
            a.sort()
            return a[0] + a[-1]
        r_sum += input[end_index]
        end_index += 1

print(b())
