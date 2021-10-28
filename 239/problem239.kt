// priority queue
fun maxSlidingWindow(nums: IntArray, k: Int): IntArray {
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
}

// deque
fun int[] maxSlidingWindow(int[] nums, int k): IntArray {
	List<Integer> list = new ArrayList<>();
	Deque<Integer> dq = new LinkedList<>();
	int count = 0;
	for(int i = 0; i < nums.length; i++){
		count++;
		// If the current element is greater than the last inserted element in the deque
		// then remove the smaller elements in the deque from last
		while(!dq.isEmpty() && nums[i] > nums[dq.peekLast()]){
			dq.removeLast();
		}
		// add the current element to the deque
		dq.add(i);
		// remove the elements from the front if the dont fall under the current window
		while(!dq.isEmpty() && dq.peekFirst() < i-k+1){
			dq.removeFirst();
		}
		if(count == k){    //if the count of iterated elements are same as the window size
			list.add(nums[dq.peekFirst()]);
			count--;
		}
	}
	// convert list to int array
	return list.stream().mapToInt(i -> i).toArray();
}

