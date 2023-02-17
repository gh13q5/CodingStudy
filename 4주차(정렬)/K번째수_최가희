#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for(int i = 0; i < commands.size(); i++){
        // 배열 복사한 후, i만큼 앞의 원소들 삭제 -> j까지 잘랐을 때의 크기로 배열 resize
        vector<int> short_arr = array;
        for(int j = 0; j < commands[i][0] - 1; j++)
            short_arr.erase(short_arr.begin());
        short_arr.resize(commands[i][1] - commands[i][0] + 1);
        
        sort(short_arr.begin(), short_arr.end());
        answer.push_back(short_arr[commands[i][2] - 1]);
    }
    
    return answer;
}
