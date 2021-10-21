#include <vector>

#include "errors.h"

using namespace std;

typedef pair <int, int> ii;
typedef vector <ii> vii;

void print(string s){
    cout << s <<endl;
}

ii next_zone(int position, vii zones){
    ii zone = {0, 0};
    for(int i = 0; i < zones.size(); i++){
        zone = zones[i];
        if(position < zone.first && position < zone.second){
            break;
        }
    }
    if(zone.first != position + 1){
        MissingZoneError(position + 1);
    }
    return zone;
}

void print_zones(vii zones){
    for(int i = 0; i < zones.size(); i++){
        cout << "<" << zones[i].first << ", " << zones[i].second << ">" << endl;
    }
}
