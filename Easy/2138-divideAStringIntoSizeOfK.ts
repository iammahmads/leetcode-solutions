function divideString(s: string, k: number, fill: string): string[] {
    const remaining_value = s.length % k;
    let iterator = 0;
    let lastValue = s.substring(s.length-remaining_value, s.length)
    if(remaining_value !== 0){
        for (let i=remaining_value; i<k; i++){
        lastValue += fill;
        }
    }
    const result: string[] = []
    while(iterator < s.length - remaining_value){
        result.push(s.substring(iterator, iterator+k))
        iterator += k
    }
    if (lastValue != ""){
        result.push(lastValue)
    }
    return result;
};