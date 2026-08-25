def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = {}

    for s in strs:
        sorted_s = "".join(sorted(s))
        if s in anagrams or sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]

    return list(anagrams.values())


if __name__ == "__main__":
    inputs = [
        dict(strs=["eat", "tea", "tan", "ate", "nat", "bat"]),
        dict(strs=[""]),
        dict(strs=["a"]),
    ]
    for i, input in enumerate(inputs):
        print(f"\n***** Test #{i} *****")
        print("Input:", input)
        output = groupAnagrams(input["strs"])
        print("Output:", output)
