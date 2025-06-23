function generateMatrix(n: number): number[][] {
  let result: number[][] = [];
  if (n === 0) return result;

  for (let row = 0; row < n; row++) {
    result[row] = []
    for (let col = 0; col < n; col++) {
      result[row][col] = 0;
    }
  }

  let top = 0;
  let left = 0;
  let bottom = n - 1;
  let right = n - 1;
  let start = 1;

  while (top <= bottom && left <= right) {
    // right
    for (let col = left; col <= right; col++) {
      result[top][col] = start;
      start += 1
    }
    top += 1;

    // down
    for (let row = top; row <= bottom; row++) {
      result[row][right] = start;
      start += 1
    }
    right -= 1;

    // left
    if (top <= bottom) {
      for (let col = right; col >= left; col--) {
        result[bottom][col] = start;
        start += 1
      }
      bottom -= 1;
    }

    // up
    if (left <= right) {
      for (let row = bottom; row >= top; row--) {
        result[row][left] = start;
        start += 1
      }
      left += 1;
    }
  }

  return result;
}
