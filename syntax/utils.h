#include <stack>

using namespace std;

void print_zones(stack <pair <int, int>> zones){
    for(int i = 0; i < zones.size(); i++){
        cout << "<" << zones.top().first << ", " << zones.top().second << ">" << endl;
        zones.pop();
    }
}
