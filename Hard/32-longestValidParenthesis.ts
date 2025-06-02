function longestValidParentheses(s: string): number {
  const brackets: number[] = [-1];
  let result = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] == "(") {
      brackets.push(i);
      continue;
    }

    if (s[i] == ")") {
        brackets.pop()
        if (brackets.length === 0){
            brackets.push(i)
        }
        else{
            result = Math.max(result, i - brackets[brackets.length - 1])
        }
    }
  }

  return result;
}

console.log(longestValidParentheses("(()"));
