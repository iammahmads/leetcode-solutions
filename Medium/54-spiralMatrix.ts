function spiralOrder(matrix: number[][]): number[] {
  const m = matrix.length;
  const n = matrix[0].length;

  let result: number[] = [];
  if (matrix.length === 0 || matrix[0].length === 0) return result;

  let top = 0;
  let left = 0;
  let bottom = m - 1;
  let right = n - 1;

  while (top <= bottom && left <= right) {
    // right
    for (let col = left; col <= right; col++) {
      result.push(matrix[top][col]);
    }
    top += 1;

    // down
    for (let row = top; row <= bottom; row++) {
      result.push(matrix[row][right]);
    }
    right -= 1;

    // left
    if (top <= bottom) {
      for (let col = right; col >= left; col--) {
        result.push(matrix[bottom][col]);
      }
      bottom -= 1;
    }

    // up
    if (left <= right) {
      for (let row = bottom; row >= top; row--) {
        result.push(matrix[row][left]);
      }
      left += 1;
    }
  }

  return result;
}
