#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    vector<int> round_cnt(n, 0);
    vector<vector<bool>> is_win(n, vector<bool>(n, false));
    
    for(int i = 0; i < results.size(); i++)
        is_win[results[i][0] - 1][results[i][1] - 1] = true;
    
    for(int v= 0; v < n; v++){
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                if(is_win[i][v] && is_win[v][j])    is_win[i][j] = true;
    }
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < is_win[0].size(); j++)
            if(is_win[i][j]){
                round_cnt[i]++;
                round_cnt[j]++;
            }
    }
        
    for(int i = 0; i < n; i++)
        if(round_cnt[i] == n - 1)   answer++;   
        
    return answer;
}

// 1) 첨엔 단순 삼중for문으로 행렬탐색함.... 근데 뒷번호에서 앞번호 경로 탐색하게 될 때 오류 발생..
// 2) 플로이드 와샬 알고리즘 사용
