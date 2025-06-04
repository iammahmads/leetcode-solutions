function solveSudoku(board: string[][]): void {
  const n = 9;

  function isValid(row: number, col: number, ch: string): boolean {
    for (let i = 0; i < n; i++) {
      // Check row
      if (board[row][i] === ch) return false;

      // Check column
      if (board[i][col] === ch) return false;

      // Check 3x3 sub-box
      const boxRow = 3 * Math.floor(row / 3) + Math.floor(i / 3);
      const boxCol = 3 * Math.floor(col / 3) + (i % 3);
      if (board[boxRow][boxCol] === ch) return false;
    }
    return true;
  }

  function backtrack(): boolean {
    for (let row = 0; row < n; row++) {
      for (let col = 0; col < n; col++) {
        if (board[row][col] === ".") {
          for (let digit = 1; digit <= 9; digit++) {
            const ch = digit.toString();
            if (isValid(row, col, ch)) {
              board[row][col] = ch;

              if (backtrack()) return true;

              board[row][col] = ".";
            }
          }
          return false;
        }
      }
    }
    return true;
  }

  backtrack();
//   console.log(board)
}

solveSudoku([
  ["5", "3", ".", ".", "7", ".", ".", ".", "."],
  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
  [".", "9", "8", ".", ".", ".", ".", "6", "."],
  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
  [".", "6", ".", ".", ".", ".", "2", "8", "."],
  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
  [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]);
