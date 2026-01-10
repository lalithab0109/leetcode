class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int pivot=-1;
        int n=nums.size();
        int rightSum=0;
        int leftSum=0;
        int sum=0;
        for(int i=0;i<n;i++){
            sum+=nums[i];
        }
        rightSum=sum;
        for(int i=0;i<n;i++){
            leftSum=sum-(rightSum);
            rightSum-=nums[i];
            if(leftSum==rightSum){
                pivot=i;
                break;
            }
        }
        return pivot;
    }
};