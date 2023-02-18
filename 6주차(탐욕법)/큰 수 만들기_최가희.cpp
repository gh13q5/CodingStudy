#include <string>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    
    stack<int> number_st;
    int pop_cnt = 0;
    
    for(int i = 0; i < number.length(); i++){
        while(!number_st.empty() && pop_cnt < k && number_st.top() < number[i] - '0'){
            number_st.pop();
            pop_cnt++;
        }
        number_st.push(number[i] - '0');
    }
    
    while(pop_cnt < k){
        number_st.pop();
        pop_cnt++;  // 아직 k만큼 못 없앴으면 맨뒤에서부터 없애줌
    }
    
    while(!number_st.empty()){
        answer += number_st.top() + '0';
        number_st.pop();
    }
    reverse(answer.begin(), answer.end());
    
    return answer;
}
