#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

bool cmp(vector<string> &v1, vector<string> &v2){
    if(v1[1] == v2[1])
        return v1[0] < v2[0];
    else
        return v1[1] < v2[1];
}

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    map<string, int> clothes_map;
    
    sort(clothes.begin(), clothes.end(), cmp);
    
    int count = 0;
    for(int i = 0; i < clothes.size(); i++){
        count++;
        if((i == clothes.size() - 1) || (clothes[i][1] != clothes[i + 1][1])){
            clothes_map.insert({clothes[i][1], count});
            count = 0;
        }
    }
    
    for (auto iter : clothes_map) {
        answer *= (iter.second + 1);
    }
    
    return answer - 1;
}
