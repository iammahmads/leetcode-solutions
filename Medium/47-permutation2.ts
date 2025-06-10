function permuteUnique(nums: number[]): number[][] {
  const result: number[][] = new Array();
  nums.sort((a, b) => a - b);
  const used: boolean[] = new Array(nums.length);
  for (let i = 0; i < nums.length; i++) {
    used[i] = false;
  }

  function backtrack(current: number[]) {
    if (current.length === nums.length) {
      result.push([...current]);
      return;
    }

    for (let i = 0; i < nums.length; i++) {
      if (used[i] === true) continue;

      // skip duplicates
      if (i > 0 && nums[i] === nums[i - 1] && used[i - 1] === false) continue;

      used[i] = true
      current.push(nums[i])
      backtrack(current)
      current.pop()
      used[i] = false
    }
  }

  backtrack([])

  return result;
}

console.log(permuteUnique([1,2,1]))
