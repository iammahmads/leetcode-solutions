function lengthOfLastWord(s: string): number {
    s = s.trim();
    return s.split(" ").at(-1)!.length
};