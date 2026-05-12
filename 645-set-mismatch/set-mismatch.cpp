class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        int x = nums[0];
        int y = 1;
        for (int i = 1; i < n; i++) {
            x = x ^ nums[i];
            y = y ^ (i + 1);
        }
        int z = x ^ y;
        int k = z & (~(z - 1));
        int a = 0;
        int b = 0;
        for (int i = 0; i < n; i++) {
            if ((nums[i] & k) != 0)
                a = a ^ nums[i];
            else
                b = b ^ nums[i];
        }
        for (int i = 1; i <= n; i++) {
            if ((i & k) != 0)
                a = a ^ i;
            else
                b = b ^ i;
        }
        for (int i = 0; i < n; i++) {
            if (a == nums[i])
                return {a, b};
        }
        return {b, a};
    }
};