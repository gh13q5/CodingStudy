#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int solution(string numbers) {
    int answer = 0;
    vector<int> numbers_v;  // numbers 문자열을 vector로
    vector<int> numbers_p;  // 순열로 조합한 숫자들
    
    for(int i = 0; i < numbers.length(); i++)
        numbers_v.push_back(numbers[i] - '0');
    sort(numbers_v.begin(), numbers_v.end());
    
    for(int i = 1; i <= numbers_v.size(); i++){
        do{
            int p = 0;
            for(int j = 0; j < i; j++){
                p *= 10;
                p += numbers_v[j];
            }
            numbers_p.push_back(p);
        
            reverse(numbers_v.begin() + i, numbers_v.end());
	    }while(next_permutation(numbers_v.begin(), numbers_v.end()));  
    }
    
    sort(numbers_p.begin(), numbers_p.end());
    numbers_p.erase(unique(numbers_p.begin(), numbers_p.end()), numbers_p.end());
    
    for(int i = 0; i < numbers_p.size(); i++){
        if(numbers_p[i] == 2 || numbers_p[i] == 3){
            answer++;
            continue;
        }
        for(int j = 2; j <= sqrt(numbers_p[i]); j++){
            if(numbers_p[i] % j == 0) break;
            if((j + 1) > sqrt(numbers_p[i]))
                answer++;
        }
    }
    
    return answer;
}

/*
    1) vector 로 저장
    2) 순열로 조합 구함 (중복값 제거)
    3) 만든 조합들이 소수인지 확인
*/
