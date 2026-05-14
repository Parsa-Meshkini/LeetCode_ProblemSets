import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>(nums.length * 2);
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            Integer j = seen.get(complement);
            if (j != null) {
                return new int[]{j, i}; 
            }
            seen.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}