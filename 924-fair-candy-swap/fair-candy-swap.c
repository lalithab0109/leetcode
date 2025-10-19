/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* fairCandySwap(int* aliceSizes, int aliceSizesSize, int* bobSizes, int bobSizesSize, int* returnSize) {
    int sumA=0;
    int sumB=0;
    int *ans=(int*)(malloc(2*sizeof(int)));
    for(int i=0;i<aliceSizesSize;i++){
        sumA+=aliceSizes[i];
    }
    for(int i=0;i<bobSizesSize;i++){
        sumB+=bobSizes[i];
    }

    for(int i=0;i<aliceSizesSize;i++){
        for(int j=0;j<bobSizesSize;j++){
            if(sumA-aliceSizes[i]+bobSizes[j]==sumB-bobSizes[j]+aliceSizes[i]){
                ans[0]=aliceSizes[i];
                ans[1]=bobSizes[j];
                *returnSize=2;
                return ans;
            }
        }

    }
    *returnSize=0;
    return ans;
}