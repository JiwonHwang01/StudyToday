#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> sequence, int k) {
    vector<int> answer;
    int l = sequence.size();
    int s = 0, e = 0;
    vector<int> p_sum = {0};
    
    
    for (int i=1;i<=l;i++){
        p_sum.insert(p_sum.end(),p_sum[i-1]+sequence[i-1]);
    }
    cout << endl ;
    while(true){
        if (s > e || e == l+1){
            break;
        }
        int tmp = p_sum[e] - p_sum[s];
        if (tmp > k){
            s += 1;
        }
        else if (tmp == k){
            if(answer.size()==0){
                answer = {s,e-1};
            }
            if((answer[1]-answer[0]) > (e-1-s)){
                answer = {s,e-1};
            }
            s += 1;
        }
        else{
            e+=1;
        }
    }
    
    return answer;
}