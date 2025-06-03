function searchRange(nums, target) {
    var result = [-1, -1];
    var left = 0;
    var right = nums.length - 1;
    while (left <= right) {
        var mid = Math.floor((left + right) / 2);
        if (target == nums[mid]) {
            result = [mid, mid];
            for (var i = mid - 1; i >= 0; i--) {
                if (nums[i] == target) {
                    result[0] = i;
                }
                else if (nums[i] != target) {
                    break;
                }
            }
            for (var i = mid + 1; i < nums.length; i++) {
                if (nums[i] == target) {
                    result[1] = i;
                }
                else if (nums[i] != target) {
                    break;
                }
            }
            break;
        }
        else if (target > nums[mid]) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    return result;
}
console.log(searchRange([5, 5], 5));
