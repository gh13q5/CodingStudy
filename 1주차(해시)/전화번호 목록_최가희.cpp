#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    size_t idx = -1;
    
    sort(phone_book.begin(), phone_book.end());
    
    for(int i = 0; i < phone_book.size() - 1; i++){
        if(phone_book[i].front() == phone_book[i + 1].front()){
            if(phone_book[i].length() < phone_book[i + 1].length()){
                idx = phone_book[i + 1].find(phone_book[i]);
            }
            else{
                idx = phone_book[i].find(phone_book[i + 1]);
            }
            
            if(idx == 0){
                answer = false;
                break;
            }
        }
    }
    
    return answer;
}
