int diagonalSum(int** mat, int matSize, int* matColSize) {
    int s1=0;
    int s2=0;
    for(int i=0;i<matSize;i++){
        s1+=mat[i][i];
        s2+=mat[i][matSize-i-1];
    }
    if(matSize%2==0){
        return s1+s2;
    }
    else{
        return s1+s2-mat[(matSize-1)/2][(matSize-1)/2];
    }
    return 0;
    
}