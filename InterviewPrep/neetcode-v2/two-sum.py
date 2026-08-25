def twoSum(nums: list[int], target: int) -> list[int]:
    complements = {}

    for i in range(len(nums)):
        if target - nums[i] in complements:
            return [complements[target - nums[i]], i]
        complements[nums[i]] = i

    return [-1, -1]


if __name__ == "__main__":
    inputs = [{"nums": [2, 7, 11, 15], "target": 9}, {"nums": [3, 2, 4], "target": 6}, {"nums": [3, 3], "target": 6}]

    for i, input in enumerate(inputs):
        print(f"\n***** Test {i+1} *****")
        print("Input:", input)
        output = twoSum(input["nums"], input["target"])
        print("Output:", output)
