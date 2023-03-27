#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

int solution(vector<int> numbers, int target) {
    int answer = 0;
    vector<int> result;
    
    result.push_back(numbers[0]);   // 첫번째 숫자가 +인 경우랑 -인 경우가 대칭적이라 한쪽만 봐도 ok
    for(int i = 1; i < numbers.size(); i++){
        int result_size = result.size();
        for(int j = 0; j < result_size; j++){
            result.push_back(result[j] - numbers[i]);
            result[j] += numbers[i];
        }
    }
    
    for(int i = 0; i < result.size(); i++)
        if(abs(result[i]) == target)    answer++;
    
    return answer;
}
