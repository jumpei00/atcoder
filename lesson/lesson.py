import datetime


def timestamp():
    return datetime.datetime.now()


def bubble(nums):
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(len_nums - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def quick(nums):
    def _quick(nums, first, last):
        if first >= last:
            return

        pivot = nums[last]
        i = first - 1

        for j in range(first, last):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        i += 1
        nums[i], nums[last] = nums[last], nums[i]

        _quick(nums, first, i - 1)
        _quick(nums, i + 1, last)

        return nums

    return _quick(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    import random
    nums_bubble = [random.randint(0, 1000) for _ in range(10000)]
    nums_quick = [random.randint(0, 1000) for _ in range(10000)]

    start = timestamp()
    bubble(nums_bubble)
    print(timestamp() - start)

    start = timestamp()
    quick(nums_quick)
    print(timestamp() - start)
