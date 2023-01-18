#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    priority_queue<int> prio_q;
    queue<pair<int, int>> ready_q;   // pair<프린트번호, 우선순위>
    
    // queue 생성
    for(int i = 0; i < priorities.size(); i++){
        prio_q.push(priorities[i]);
        ready_q.push(make_pair(i, priorities[i]));
    }
    
    while(!ready_q.empty()){
        if(ready_q.front().second == prio_q.top()){
            answer++;
            prio_q.pop();
            if(ready_q.front().first == location)
                break;
        }
        else
            ready_q.push(ready_q.front());
        ready_q.pop();
    }
    
    return answer;
}
