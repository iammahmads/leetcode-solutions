function search(nums: number[], target: number): number {
  if (nums.length == 0) {
    return -1;
  }

  let pivot = 0;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] < nums[i - 1]) {
      pivot = i-1;
      break;
    }
  }

  let left = 0;
  let right = 0;
  if (target >= nums[pivot+1] && target <= nums[nums.length - 1]) {
    left = pivot+1;
    right = nums.length - 1;
  } else {
    right = pivot;
  }

  let result = -1;
  while (left <= right) {
    // console.log(left, right)
    if (target == nums[left]) {
      result = left;
      break;
    }
    if (target == nums[right]) {
      result = right;
      break;
    }

    const mid = (left + right) / 2;
    if (target <= nums[mid]) {
      left += 1;
      right = mid;
    } else if (target > nums[mid]) {
      left = mid;
      right -= 1;
    } else {
      left += 1;
      right -= 1;
    }
  }

  //   console.log(pivot);
  return result;
}

console.log(search([0], 0));
