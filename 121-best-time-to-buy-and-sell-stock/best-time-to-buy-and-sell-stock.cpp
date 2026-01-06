class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n=prices.size();
        vector<int> sell(n);
        sell[n-1]=prices[n-1];
        int max_profit=0;
        for(int i=n-2;i>=0;i--){
            sell[i]=max(sell[i+1],prices[i+1]);
        }
        for(int i=0;i<n;i++){
            max_profit=max((sell[i]-prices[i]),max_profit);
        }
        return max_profit;
        
    }
};