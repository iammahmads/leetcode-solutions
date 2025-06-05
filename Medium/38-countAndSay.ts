function countAndSay(n: number): string {

  function recursion(m: number): string {
    if (m === 1) return "1";

    let result = recursion(m - 1);

    let previous = result[0];
    let counter = 1;
    let newString = "";
    for (let i = 1; i < result.length; i++) {
      if (result[i] !== previous) {
        newString += `${counter}${previous}`;
        counter = 0;
        previous = result[i];
      }
      counter += 1;
    }
    newString += `${counter}${previous}`;
    return newString
  }

  const result = recursion(n)
  console.log(result)
  return result
}

countAndSay(4)