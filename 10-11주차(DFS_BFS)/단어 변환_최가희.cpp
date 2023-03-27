#include <string>
#include <vector>
#include <queue>

using namespace std;

bool is_one_diff(string a, string b){
    int cnt = 0;
    for(int i = 0; i < a.length(); i++)
        if(a[i] != b[i])    cnt++;
    
    if(cnt == 1)    return true;
    return false;
}

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    queue<string> words_q;
    
    words_q.push(begin);
    while(!words_q.empty()){
        int q_size = words_q.size();
        for(int i = 0; i < q_size; i++){
            string cur = words_q.front();
            words_q.pop();
            
            if(cur == target)   return answer;
            
            for(int j = 0; j < words.size(); j++){
                if(words[j] == "v") continue;
                if(is_one_diff(cur, words[j])){
                    words_q.push(words[j]);
                    words[j] = "v";     // visited 방문처리
                }
            }
        }
        answer++;
    }
    
    return 0;
}

// bfs
