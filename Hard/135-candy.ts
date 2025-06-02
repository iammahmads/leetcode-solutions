function candy(ratings: number[]): number {
    const n = ratings.length
    const candies: number[] = new Array()
    for (let i=0; i<n; i++){
        candies.push(1)
    }

    for (let i=1; i<ratings.length; i++){
        if (ratings[i] > ratings[i-1]){
            candies[i] = candies[i-1] + 1
        }
    }

    for (let i=n-1; i>-1; i--){
        if (ratings[i] > ratings[i+1]){
            candies[i] = Math.max(candies[i], candies[i+1] + 1)
        }
    }

    return candies.reduce((a, b) => a + b, 0)
};

console.log(candy([1,2,1]))