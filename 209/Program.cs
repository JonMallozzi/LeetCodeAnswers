int MinSubArrayLen(int target, int[] nums) {
        int left = 0;
        int right = 0;
        int total = 0;
        int answer = Int32.MaxValue;
        
        while (right < nums.Length) {
            if (nums[right] + total < target) {
                total += nums[right];
                right++;
            } else {
                total -= nums[left];
                answer = Math.Min(answer, right - left + 1);
                left++;
            }
        }

        if (answer == Int32.MaxValue) {
            return 0;
        }
        
        return answer;
}

int target = 7;
int[] nums = {2,3,1,2,4,3};
Console.WriteLine(MinSubArrayLen(target, nums));

target = 11;
int[] nums2 = {1,1,1,1,1,1,1,1};
Console.WriteLine(MinSubArrayLen(target, nums2));
