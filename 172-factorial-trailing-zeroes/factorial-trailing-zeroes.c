int trailingZeroes(int n) {
    int answer=0;
    int term=n/5;
    while(term>0){
        answer+=term;
        term=term/5;
    }
    return answer;
}