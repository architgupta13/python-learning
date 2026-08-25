import heapq


def topKFrequent(nums: list[int], k: int) -> list[int]:
    ### Method 2: Bucket sort ###
    frequencies = {}
    for num in nums:
        frequencies[num] = frequencies.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in frequencies.items():
        # consider count as index in buckets array
        buckets[count].append(num)

    frequent_elements = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            frequent_elements.append(num)

            if len(frequent_elements) == k:
                return frequent_elements

    return frequent_elements

    ### Method 1: Min-heap ###
    # frequencies = {}
    # for num in nums:
    #     frequencies[num] = frequencies.get(num, 0) + 1

    # if k > len(frequencies):
    #     k = len(frequencies)

    # min_heap = []
    # for key, value in frequencies.items():
    #     heapq.heappush(min_heap, (value * -1, key))

    # frequent_elements = []
    # for _ in range(k):
    #     frequent_elements.append(heapq.heappop(min_heap)[-1])

    # return frequent_elements


if __name__ == "__main__":
    inputs = [
        dict(nums=[1, 1, 1, 2, 2, 3], k=2),
        dict(nums=[1], k=1),
        dict(nums=[1, 2, 1, 2, 1, 2, 3, 1, 3, 2], k=2),
        dict(nums=[4, 1, -1, 2, -1, 2, 3], k=2),
    ]
    for i, input in enumerate(inputs):
        print(f"\n***** Test #{i} *****")
        print("Input:", input)
        output = topKFrequent(input["nums"], input["k"])
        print("Output:", output)
