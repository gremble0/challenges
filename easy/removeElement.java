import java.util.Arrays;

class Solution {
    public int removeElement(int[] nums, int val) {
        return Arrays.stream(nums).filter(n -> n != val).toArray();
    }
}
