#include <string>
#include <vector>
#include <cmath>

using namespace std;

int powSum(int num, int count){
    int sum = 0;
    for(int i = 0; i <= count; i++){
        sum += (int)pow(num, i);
    }
    
    return sum;
}

int solution(string word) {    
    int answer = 0;
    
    for(int i = 0; i < word.size(); i++){
        switch (word[i]){
            case 'A':
                answer += 1;
                break;
            case 'E':
                answer += (1 + powSum(5, 4 - i));
                break;
            case 'I':
                answer += (1 + (2 * powSum(5,4 - i)));
                break;
            case 'O':
                answer += (1 + (3 * powSum(5, 4 - i)));
                break;
            case 'U':
                answer += (1 + (4 * powSum(5, 4 - i)));
                break;
        }
    }
    
    return answer;
}
