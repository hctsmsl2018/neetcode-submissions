class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    binarySearch(nums: number[], target: number, start: number, end: number): number {
        if (start == end) {
            return nums[start] == target ? start : -1;
        } else if (start + 1 == end) {
            return nums[start] == target ? start : nums[end] == target ? end : -1;
        }

        const mid = Math.round((start + end) / 2);

        if (nums[mid] == target) {
            return mid;
        } else if (nums[start] < nums[mid] && nums[mid] < nums[end]) {
            if (nums[mid] > target) {
                return this.binarySearch(nums, target, start, mid);
            } else {
                return this.binarySearch(nums, target, mid, end);
            }
        } else if (nums[mid] < nums[start] && nums[mid] < nums[end]) {
            if (nums[mid] < target && target <= nums[end]) {
                return this.binarySearch(nums, target, mid, end);
            } else {
                return this.binarySearch(nums, target, start, mid);
            }
        } else if (nums[start] < nums[mid] && nums[end] < nums[start]) {
            if (nums[start] <= target && target < nums[mid]) {
                return this.binarySearch(nums, target, start, mid);
            } else {
                return this.binarySearch(nums, target, mid, end);
            }
        }
    }

    search(nums: number[], target: number): number {
        return this.binarySearch(nums, target, 0, nums.length - 1);
    };
}
