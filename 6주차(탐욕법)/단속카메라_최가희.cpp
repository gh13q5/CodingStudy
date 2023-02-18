#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> routes) {
    int answer = 1;
    
    sort(routes.begin(), routes.end());
    
    int last_car = routes[0][1];
    for(int i = 1; i < routes.size(); i++){
        if(routes[i][0] > last_car){
            answer++;
            last_car = routes[i][1];
        }
        if(routes[i][1] <= last_car)    last_car = routes[i][1];
    }
    
    return answer;
}
