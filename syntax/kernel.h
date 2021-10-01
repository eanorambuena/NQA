#include <vector>
#include <stack>
#include <queue>
#include <algorithm> // for erase

#include "file.h"
#include "utils.h"
#include "errors.h"

using namespace std;

typedef pair <int, int> ii;
typedef vector <char> vc;
typedef vector <string> vs;
typedef stack <string> ps; // "p" for the Spanish word "pila" in order to use "s" only for strings
typedef stack <ii> pii;
typedef queue <string> qs;

void compile(string name){
    int waiting = 0;
    pii zones;
    string text = "";

    vc words = read(name + ".nqa");
    vs commands = join(words);
    print_list(commands);

    for(int i = 0; i < commands.size(); i++){
        string c = commands[i];
        if(c == "("){
            waiting += 1;
            zones.push({i, i});
        }
        else if(c == ")"){
            waiting += -1;
            zones.top().second = i;
        }
        else if(c == "cpp"){
            text += commands[i + 1];
        }
    }

    if(waiting != 0){
        ZoneError(waiting);
    }

    print_zones(zones);

    write(name + ".cpp", text);
}