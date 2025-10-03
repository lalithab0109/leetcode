class Solution {
public:
    int search(vector<int>& nums, int target) {
        int len= nums.size();
        int start=0;
        int end=len-1;
        while(end>=start){
            int mid=((start+end)/2);
            if(target==nums[mid]){
                return mid;
            }
            else if(target<nums[mid]){
                end=mid-1;
            }
            else if(target>nums[mid]){
                start=mid+1;
            }
        }
        return -1;
    }
};