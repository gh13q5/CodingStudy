#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

bool cmp_total_plays(pair<string, int> a, pair<string, int> b) {
	return a.second > b.second;
}

bool cmp_musics(pair<string, pair<int, int>> a, pair<string, pair<int, int>> b) {
    if(a.first == b.first)
        return a.second.second > b.second.second;
    return a.first > b.first;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    map<string, int> total_plays;   // 장르 이름, 총 재생수
    multimap<string, pair<int, int>> musics; // 장르 이름, <장르 번호, 재생수>
    
    for(int i = 0; i < genres.size(); i++){
        musics.insert({genres[i], make_pair(i, plays[i])});
        total_plays[genres[i]] += plays[i];
    }
    
    // total_plays 총재생수로 정렬
    vector<pair<string, int>> total_plays_v(total_plays.begin(), total_plays.end());
    sort(total_plays_v.begin(), total_plays_v.end(), cmp_total_plays);
    
    // musics 재생수 -> 장르 이름으로 정렬
    vector<pair<string, pair<int, int>>> musics_v(musics.begin(), musics.end());
    sort(musics_v.begin(), musics_v.end(), cmp_musics);
    
    for(int i = 0; i < total_plays_v.size(); i++){
        int count = 0;
        for(int j = 0; j < musics_v.size(); j++){
            if(total_plays_v[i].first == musics_v[j].first){
                answer.push_back(musics_v[j].second.first);
                if(++count >= 2)    break;
            }
        }
    }
    
    return answer;
}
