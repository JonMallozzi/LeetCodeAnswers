// 34. Find First and Last Position of Element in Sorted Array

/*
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
*/

/*
example:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
*/

// small problems/ steps
// do not search if it doesn't contain the target
// binary search for the target and loop up until the end

pub fn binary_search(nums: &Vec<i32>, target: i32, left: bool) -> i32 {
    
    let mut low = 0;
    let mut high = nums.len();

    while low < high {
        let mid = ( low + high ) / 2;
        if nums[mid] as i32 > target || (left && target == nums[mid] as i32) {
            high = mid;
        } else  {
            low = mid + 1;
        }
    }

    return low as i32;

}

pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
    
    let mut answer: Vec<i32> = vec![-1,-1];

    let left_index = binary_search(&nums, target, true);

     // assert that `leftIdx` is within the array bounds and that `target`
     // is actually in `nums`.
     if left_index == nums.len() as i32 || nums[left_index as usize] as i32 != target {
        return answer;
     }

     answer[0] = left_index;
     answer[1] = binary_search(&nums, target, false) -1;

     return answer;
}

fn main() {
    println!("{:?}",search_range(vec![5,7,7,8,8,10], 8));
}