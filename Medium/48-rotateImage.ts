/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(matrix: number[][]): void {
  const n = matrix.length;

  for (let i = 0; i < n; i++) {
    for (let j = i+1; j < n; j++) {
      [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
    }
  }
  matrix.forEach((row) => row.reverse())
//   console.log(matrix);
}

rotate([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]);
