var binarySearch = function(sortedArr, target) {
    let left = 0;
    let right = sortedArr.length - 1;
  
    while (left <= right) {
      const middle = Math.floor((left + right) / 2);
  
      if (sortedArr[middle] === target) {
        return middle;
      } else if (sortedArr[middle] < target) {
        left = middle + 1;
      } else {
        right = middle - 1;
      }
    }
  
    return -1;
  }
  
  const arr = [10, 20, 30];
  const target = 30;
  const result = binarySearch(arr, target);
  console.log(result);
  