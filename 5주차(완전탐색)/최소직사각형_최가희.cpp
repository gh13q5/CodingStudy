#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    // 지갑의 가로세로 길이
    int walletW = 0;
    int walletH = 0;
    
    for(int i = 0; i < sizes.size(); i++){
        if(sizes[i][0] < walletW && sizes[i][1] < walletH){
            // 현재 지갑 사이즈에 맞는 경우
            continue;
        }
        if(sizes[i][0] < walletH && sizes[i][1] < walletW){
            // 뒤집었을 때 현재 지갑 사이즈에 맞는 경우
            continue;
        }
        else{
            // 뒤집었을 때와 안 뒤집었을 때, 어느 쪽이 더 지갑 사이즈를 줄일 수 있는지 비교
            int origin = abs(walletW - sizes[i][0]) + abs(walletH - sizes[i][1]);
            int reverse = abs(walletH - sizes[i][0]) + abs(walletW - sizes[i][1]);
            
            if(reverse < origin){
                int temp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = temp;
            }
            
            if(sizes[i][0] > walletW){
                if(sizes[i][1] > walletH){
                    // 현재 지갑보다 가로도 세로도 모두 큰 경우
                    walletH = sizes[i][1];
                }
                walletW = sizes[i][0];
            }
            else if(sizes[i][1] > walletH){
                // 현재 지갑보다 세로만 큰 경우
                walletH = sizes[i][1];
            }
        }
        
    }
    
    answer = walletW * walletH;
    return answer;
}
