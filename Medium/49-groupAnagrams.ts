function groupAnagrams(strs: string[]): string[][] {

    const map = new Map<string, string[]>()
    /**
     * ANAGRAMS
     * An anagram is a word or phrase formed by rearranging the letters
     * of a different word or phrase, using all the original letters exactly once.
     */

    for (const str of strs){
        const key = str.split("").sort().join('');
        if (!map.has(key)){
            map.set(key, [])
        }
        map.get(key)!.push(str)
    }
    
    return Array.from(map.values());
};