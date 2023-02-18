#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int all_grid = brown + yellow;  // 전체 격자 수
    
    for(int row = 3; row < all_grid; row++){
        if(all_grid % row != 0) continue;
        
        int col = all_grid / row;
        if(row < col)   continue;
        
        if((row * 2) + ((col - 2) * 2) == brown){
            answer.push_back(row);
            answer.push_back(col);
            break;
        }
    }
    
    return answer;
}
