#include <string>
#include <vector>
#include <queue>

using namespace std;

struct cmp{
    bool operator()(string a, string b){
        return a + b < b + a;
    }
};

string solution(vector<int> numbers) {
    string answer = "";
    priority_queue<string, vector<string>, cmp> numbers_s;  // numbers를 string으로 변환한 후 사전 내림차순 정렬
    
    for(int i = 0; i < numbers.size(); i++)
        numbers_s.push(to_string(numbers[i]));
    
    int zero_cnt = 0;
    for(int i = 0; i < numbers.size(); i++){
        if(numbers_s.top() == "0")  zero_cnt++;
        answer += numbers_s.top();
        numbers_s.pop();
    }
    
    if(zero_cnt == numbers.size())  answer = "0"; // 모두 0이면 answer도 0으로
    
    return answer;
}
