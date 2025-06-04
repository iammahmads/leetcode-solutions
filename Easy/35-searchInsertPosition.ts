function searchInsert(nums: number[], target: number): number {

    if(nums.length === 0){
        return 0
    }

    let left = 0
    let right = nums.length - 1
    let result = -1
    let mid = -1
    while (left <= right){
        mid = Math.floor((left+right)/2)
        if (target > nums[mid]){
            left = mid+1
        }
        else if(target < nums[mid]){
            right = mid - 1
        }
        else{
            result = mid
            break
        }
    }

    if (result === -1){
        if (target > nums[mid]){
            result = mid+1
        }
        else{
            result = mid
        }
    }

    return result
};

console.log(searchInsert([1,3,5,6], 0))