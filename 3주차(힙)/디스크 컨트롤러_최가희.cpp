#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>

using namespace std;

bool cmp(vector<int> a, vector<int> b){
    if(a[0] == b[0])
        return a[1] < b[1];
	return a[0] < b[0];
}

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    int idx = 0;
    int time = 0;
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> ready_pq; // pair<작업시간, 요청시간>
    
    // 요청시간 순으로 정렬
    sort(jobs.begin(), jobs.end(), cmp);
    
    while(true){
        if((idx >= jobs.size()) && (ready_pq.empty()))  break;
        
        while((idx < jobs.size()) && (jobs[idx][0] <= time)){
            ready_pq.push(make_pair(jobs[idx][1], jobs[idx][0]));
            idx++;
        }
        
        // 전체 작업이 아직 안 끝났는데, 현재 당장 작업할 수 있는 게 없을 때
        if(ready_pq.empty()){
            time = jobs[idx][0];
            continue;
        }
        
        time += ready_pq.top().first;
        answer += (time - ready_pq.top().second);
        
        ready_pq.pop();
    }
    
    return answer / jobs.size();
}
