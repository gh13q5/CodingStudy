#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    
    vector<vector<int>> answer_rules{{1, 2, 3, 4, 5}, {2, 1, 2, 3, 2, 4, 2, 5}, {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}};
    vector<int> answer_cnt(3, 0);   // 맞춘 정답 수
    
    for(int i = 0; i < answers.size(); i++){
        for(int j = 0; j < answer_cnt.size(); j++)
            if(answers[i] == answer_rules[j][i % answer_rules[j].size()])   answer_cnt[j]++;
    }
    
    int max_cnt = *max_element(answer_cnt.begin(), answer_cnt.end());
    for(int i = 0; i < answer_cnt.size(); i++)
        if(answer_cnt[i] == max_cnt)   answer.push_back(i + 1);
    
    return answer;
}
