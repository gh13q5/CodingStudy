#include <string>
#include <vector>

#define MAX 8

using namespace std;

bool visit[8];
int maxCount = -1;

void findDungeons(int k, int count, vector<vector<int>> dungeons){
    // DFS
    if(count > maxCount){
        maxCount = count;
    }
    
    for(int i = 0; i < dungeons.size(); i++){
        if(visit[i] == false && k >= dungeons[i][0]){
            visit[i] = true;
            findDungeons(k - dungeons[i][1], count + 1, dungeons);
            visit[i] = false;
        }
    }
}

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    
    for(int i = 0; i < MAX; i++){
        visit[i] = false;
    }
    
    findDungeons(k, 0, dungeons);
    
    answer = maxCount;
    return answer;
}
