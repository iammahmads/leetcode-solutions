function multiply(num1: string, num2: string): string {


    if (num1 === '0' || num2 === '0'){
        return '0'
    }

    const n = num1.length
    const m = num2.length
    let result: number[] = new Array(m+n)
    for (let i=0; i<result.length; i++){
        result[i] = 0
    }

    for (let i=n-1; i>= 0; i--){
        const digit1 = num1.charCodeAt(i) - '0'.charCodeAt(0)
        for(let j=m-1; j>= 0; j--){
            const digit2 = num2.charCodeAt(j) - '0'.charCodeAt(0)

            const multiply = digit1 * digit2
            const index1 = i+j
            const index2 = i+j+1
            const sum = multiply + result[index2]
            result[index2] = sum%10
            result[index1] += Math.floor(sum/10)
        }
    }
    
    return result.length === 0 ? "0": result.join("").replace(/^0+/, '')
};


console.log(multiply("0", "0"))