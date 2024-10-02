function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    const mergedArray = [...nums1, ...nums2].sort((a, b) => a - b);
    const length = mergedArray.length;
    if (length % 2 !== 0) {
        return mergedArray[Math.floor(length / 2)];
    }
    else{
        return (mergedArray[length / 2 - 1] + mergedArray[length / 2]) / 2;
    }
};