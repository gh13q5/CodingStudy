#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    // 우선순위 큐에서 오름차순으로 정렬
    priority_queue<int, vector<int>, greater<int>> scoville_pq(scoville.begin(),scoville.end());
    
    int mix_scoville;
    while((!scoville_pq.empty()) && (scoville_pq.top() < K)){
        if(scoville_pq.size() <= 1) return answer = -1;
        
        mix_scoville = scoville_pq.top();
        scoville_pq.pop();
        mix_scoville += (scoville_pq.top() * 2);
        scoville_pq.pop();
        
        scoville_pq.push(mix_scoville);
        answer++;
    }
    
    return answer;
}
