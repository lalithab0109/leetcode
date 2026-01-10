class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n=nums.size();
        vector<int> prod_left(n);
        vector<int> prod_right(n);
        vector<int> prod(n);
        prod_left[0]=1;
        for(int i=1;i<n;i++){
            prod_left[i]=prod_left[i-1]*nums[i-1];
        }
        prod_right[n-1]=1;
        for(int i=n-2;i>=0;i--){
            prod_right[i]=prod_right[i+1]*nums[i+1];
        }
        for(int i=0;i<n;i++){
            prod[i]=prod_left[i]*prod_right[i];
        }
        return prod;
    }
};