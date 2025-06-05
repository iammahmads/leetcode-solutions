function combinationSum(candidates: number[], target: number): number[][] {
    let result:number[][] = new Array()


    function backtrack(start:number, current: number[], total:number){
        if (total === target){
            // console.log(current)
            result.push([...current])
            return
        }

        if (total > target) return

        for (let i=start; i<candidates.length; i++){
            current.push(candidates[i])
            backtrack(i, current, total+candidates[i])
            current.pop()
        }
    }
    backtrack(0, [], 0)
    return result
};

console.log(combinationSum([2,3,6,7], 7))