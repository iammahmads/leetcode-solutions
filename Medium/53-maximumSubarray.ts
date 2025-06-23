function maxSubArray(nums: number[]): number {
  let max = nums[0];
  let currSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    currSum = Math.max(nums[i], currSum + nums[i]);
    max = Math.max(currSum, max);
  }

  return max;
}
