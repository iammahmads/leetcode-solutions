type ObjectType = {
  [key: string]: number;
};

function maxDifference(s: string): number {
  let counter: ObjectType = {};
  for (let i = 0; i < s.length; i++) {
    if (counter[s[i]] !== undefined) {
      counter[s[i]] += 1;
    } else {
      counter[s[i]] = 1;
    }
  }

  const evenFreq: number[] = [];
  const oddFreq: number[] = [];
  for (const key in counter) {
    const value = counter[key];
    if (value % 2 == 0) {
      evenFreq.push(value)
    } else {
      oddFreq.push(value)
    }
  }
//   console.log(evenFreq)
//   console.log(oddFreq)

  let maxDiff = -Infinity
  for (const odd of oddFreq){
    for (const even of evenFreq){
        maxDiff = Math.max(maxDiff, odd-even)
    }
  }
  return maxDiff;
}

console.log(maxDifference("aaaaabbc"));
