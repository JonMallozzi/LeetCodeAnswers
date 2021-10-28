"""
Problem: 239. Sliding Window Maximum

You are given an array of integers nums,
there is a sliding window of size k which is moving from the very
left of the array to the very right. You can only see the k numbers
in the window. Each time the sliding window
moves right by one position.

Return the max sliding window.
"""

"""
Exmaples:
Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

 Example 2:

Input: nums = [1], k = 1
Output: [1]

Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]

Example 4:

Input: nums = [9,11], k = 2
Output: [11]
"""

defmodule Solutions do
  def PriorityQueue(a, b) do
    a + b
  end

  def Deque(a,b) do
    a + b
end

IO.puts(Solutions.PriorityQueue(1,2))
IO.puts(Solutions.Deque(1,2))

# converting to elixir
val result = IntArray(nums.size - k + 1) { -1 }
        var windowStart = 0
        var windowEnd = k - 1
        var max = Integer.MIN_VALUE
        val windowQueue = PriorityQueue<Pair<Int, Int>>(object: Comparator<Pair<Int, Int>> {
            override fun compare(a: Pair<Int, Int>, b: Pair<Int, Int>) = b.first - a.first
        })
        nums.take(k).forEachIndexed { idx, it->
            windowQueue.add(it to idx)
            max = Math.max(max, it)
        }
        var count = 0
        result[count++] = max
        while (windowEnd < nums.size) {
            windowStart++
            while (windowQueue.isNotEmpty() && windowQueue.peek().second < windowStart) windowQueue.poll()
            if (++windowEnd < nums.size) {
                windowQueue.add(nums[windowEnd] to windowEnd)
                max = windowQueue.peek().first
                result[count++] = max
            }
        }
        return result
