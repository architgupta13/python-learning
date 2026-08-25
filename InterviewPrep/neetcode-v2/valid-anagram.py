def isAnagram(s: str, t: str) -> bool:
    char_counts = [0] * 26

    for ch in s:
        char_counts[ord(ch) - ord("a")] += 1

    for ch in t:
        char_counts[ord(ch) - ord("a")] -= 1

    for occurence in char_counts:
        if occurence != 0:
            return False

    return True


if __name__ == "__main__":
    inputs = [{"s": "anagram", "t": "nagaram"}, {"s": "rat", "t": "cat"}, {"s": "a", "t": "ab"}]

    for i, input in enumerate(inputs):
        print(f"\n***** Test #{i+1} *****")
        print("Input:", input)
        output = isAnagram(input["s"], input["t"])
        print("Output:", output)
