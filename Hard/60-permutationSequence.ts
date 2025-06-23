function getPermutation(n: number, k: number): string {
  let used: boolean[] = new Array(n).fill(false);
  let allPermutations: number[][] = [];
  let current: number[] = [];

  let iterator = 0;
  function generatePermutations() {
    if (current.length === n) {
      allPermutations.push([...current]);
      iterator += 1;
      return;
    }

    for (let i = 1; i <= n; i++) {
      if (used[i-1] === true) continue;

      used[i-1] = true;
      current.push(i);
      generatePermutations();
      if (iterator === k){
        return;
      }
      current.pop();
      used[i-1] = false;
    }
  }
  generatePermutations()
  return allPermutations[k-1].join("");
}
