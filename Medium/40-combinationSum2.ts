function combinationSum2(candidates: number[], target: number): number[][] {
    let result:number[][] = new Array()
    candidates.sort((a, b) => a-b)

    function backtrack(start:number, current: number[], total:number){
        if (total === target){
            // console.log(current)
            result.push([...current])
            return
        }

        if (total > target){
            return
        }

        for (let i=start; i<candidates.length; i++){
            if(candidates[i] > target){
                break
            }
            if (i > start && candidates[i] === candidates[i-1]) continue;

            current.push(candidates[i])
            backtrack(i+1, current, total+candidates[i])
            current.pop()
        }
    }
    backtrack(0, [], 0)

    return result
};

console.log(combinationSum2([10,1,2,7,6,1,5], 5))