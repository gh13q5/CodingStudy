#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector<int> students(n, 1); // 체육복 없으면 0, 1벌이면 1, 여벌 있으면 2
    
    int lost_idx = 0;
    int reserve_idx = 0;
    for(int i = 0; i < lost.size(); i++)
        students[lost[i] - 1]--;
    for(int i = 0; i < reserve.size(); i++)
        students[reserve[i] - 1]++;
    
    for(int i = 0; i < students.size() - 1; i++){
        if(students[i] == 1)    continue;
        if((students[i] == 2) && (students[i + 1] == 0)){
            students[i]--;
            students[i + 1]++;
        }
        else if((students[i] == 0) && (students[i + 1] == 2)){
            students[i]++;
            students[i + 1]--;
        }
    }
    
    // students에서 1인 애들 세줌
    for(int i = 0; i < students.size(); i++)
        if((students[i] == 1) || (students[i] == 2))    answer++;
    
    return answer;
}
