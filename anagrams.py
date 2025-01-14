def groupAnagrams(strs):
    #Dictionary to store sorted string as key 
    #and list of anagrams as value
    anagram_groups = {}

    for s in strs:
        #sort the current string to get the key
        sorted_str = ''.join(sorted(s))

        #adding string to its anagram group
        if sorted_str in anagram_groups:
            anagram_groups[sorted_str].append(s)
        else:
            anagram_groups[sorted_str] = [s]
    return list(anagram_groups.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))