function isValidSudoku(board: string[][]): boolean {
  let result = true;

  const n = 9;

  function hasDuplicates(arr: string[]): boolean {
    const seen: Record<string, boolean> = {};
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] in seen) {
        return true;
      }
      seen[arr[i]] = true;
    }
    return false;
  }

  for (let i = 0; i < n; i++) {
    // duplicate check in colum
    const colElement: string[] = [];
    for (let row = 0; row < n; row++) {
      if (board[i][row] != ".") {
        colElement.push(board[i][row]);
      }
    }
    if (hasDuplicates(colElement) === true) {
      result = false;
      break;
    }

    // duplicate in rows
    const rowElement: string[] = [];
    for (let col = 0; col < n; col++) {
      if (board[col][i] != ".") {
        rowElement.push(board[col][i]);
      }
    }
    if (hasDuplicates(rowElement) === true) {
      result = false;
      break;
    }
  }

  // duplicates in 3x3
  for (let i = 0; i < 9; i += 3) {
    for (let j = 0; j < 9; j += 3) {
    //   console.log(i, j)
      const elements: string[] = [];
      for (let row = i; row < i + 3; row++) {
        for (let col = j; col < j + 3; col++) {
          if (board[row][col] != ".") {
            elements.push(board[row][col]);
          }
        }
      }
    //   console.log(elements);
      if (hasDuplicates(elements) === true) {
        result = false;
        break;
      }
    }
    if (result == false){
        break
    }
  }

  return result;
}

console.log(
  isValidSudoku([
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
  ])
);
