def containsDuplicate(nums: list[int]) -> bool:
    uniq_nums = set(nums)
    return sorted(list(uniq_nums)) != sorted(nums)


if __name__ == "__main__":

    inputs = [
        dict(nums=[1, 2, 3, 1]),
        dict(nums=[1, 2, 3, 4]),
        dict(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]),
        dict(nums=[3, 1]),
    ]

    for i, input in enumerate(inputs):
        print(f"\n***** Test #{i+1} *****")
        print("Input:", input)
        output = containsDuplicate(input["nums"])
        print("Output:", output)
