#include <vector>
#include <queue>

using namespace std;

int dx[4] = {0, 1, 0, -1};     // 상-우-하-좌 (시계방향)
int dy[4] = {-1, 0, 1, 0};

int solution(vector<vector<int>> maps){
    int distance = 1;
    queue<pair<int, int>> next_q;
    
    next_q.push(make_pair(0, 0));
    while(!next_q.empty()){
        int q_size = next_q.size();
        for(int i = 0; i < q_size; i++){
            int cur_y = next_q.front().first;
            int cur_x = next_q.front().second;
            next_q.pop();
            
            for(int j = 0; j < 4; j++){
                int next_y = cur_y + dy[j];
                int next_x = cur_x + dx[j];
                
                if(next_y < 0 || next_y >= maps.size() || next_x < 0 || next_x >= maps[0].size()
                   || maps[next_y][next_x] == 0)    continue;
                if(next_y == maps.size() - 1 && next_x == maps[0].size() - 1)   return distance + 1;
                
                maps[next_y][next_x] = 0;   // visit 처리
                next_q.push(make_pair(next_y, next_x));
            }
        }
        distance++;
    }
    
    return -1;
}
