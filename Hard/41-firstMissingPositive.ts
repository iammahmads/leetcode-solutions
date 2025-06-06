function firstMissingPositive(nums: number[]): number {
  nums.sort((a, b) => a - b);
  // console.log(nums)

  let result = 1;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] <= 0) continue; // less than 1
    if (i > 0 && nums[i] === nums[i - 1]) continue; // duplicates

    if (result !== nums[i]) {
      break;
    }
    result += 1;
  }
  return result;
}

console.log(firstMissingPositive([0, 2, 2, 1, 1]));
