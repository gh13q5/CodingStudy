#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> time_q;
    
    // queue에 개발까지 걸리는 일수 집어넣음
    for(int i = 0; i < progresses.size(); i++){
        int time = 100 - progresses[i];
        if(time % speeds[i] != 0)
            time = (time / speeds[i]) + 1;
        else
            time = time / speeds[i];
        time_q.push(time);
    }
    
    // 뽑음
    int count = 0;
    int first_data = -1;
    while(!time_q.empty()){
        count++;
        if(time_q.front() > first_data)
            first_data = time_q.front();
        time_q.pop();
        
        if((time_q.size() == 0) || (first_data < time_q.front())){
            answer.push_back(count);
            count = 0;
        }
    }
    
    return answer;
}
