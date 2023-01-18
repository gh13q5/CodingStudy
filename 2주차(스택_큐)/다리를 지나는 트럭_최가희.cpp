#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    
    int idx = 0;
    int q_weight = 0;
    queue<int> bridge_q;
    
    while(true){
        answer++;
        
        if(bridge_q.size() == bridge_length){
            q_weight -= bridge_q.front();
            bridge_q.pop();
        }
        
        if(q_weight + truck_weights[idx] <= weight){
            q_weight += truck_weights[idx];
            bridge_q.push(truck_weights[idx++]);
            
            if(idx == truck_weights.size()) break;
        }
        else
            bridge_q.push(0);
    }
    
    return answer + bridge_length;
}
