int MissingNumber(int[] nums) {
    return Enumerable.Range(0, nums.Length + 1).ToArray().Sum() - nums.Sum();
}

int[] nums = {9,6,4,2,3,5,7,0,1};
Console.WriteLine(MissingNumber(nums));