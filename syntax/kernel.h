#include <vector>
#include <stack>
#include <queue>
#include <algorithm> // for erase

#include "file.h"
#include "utils.h"

using namespace std;

typedef pair <int, int> ii;
typedef vector <char> vc;
typedef vector <string> vs;
typedef stack <string> ps; // "p" for the Spanish word "pila" in order to use "s" only for strings
typedef vector <ii> vii;
typedef queue <string> qs;

void compile(string name){
    int waiting = 0;
    vii zones;
    ii zone;
    string text = "";

    vc words = read(name + ".nqa");
    vs commands = join(words);
    print_list(commands);

    for(int i = 0; i < commands.size(); i++){
        string c = commands[i];
        if(c == "["){
            waiting += 1;
            zone = {i, 0};
        }
        else if(c == "]"){
            waiting += -1;
            zone.second = i;
            zones.push_back(zone);
        }
    }

    for(int i = 0; i < commands.size(); i++){
        string c = commands[i];
        if(c == "cpp"){
            ii zone = next_zone(i, zones);
            for(int j = zone.first + 1; j < zone.second ; j++){
                text += commands[j] + " "; 
            }
        }
        
        else if(c == "include"){
            ii zone = next_zone(i, zones);
            string file = "";
            for(int j = zone.first + 1; j < zone.second ; j++){
                file += commands[j];
            }
            vc content = read(file);
            for(int j = 0; j < content.size(); j++){
                text += content[j];
            }
            text += "\n";
        }
    }

    if(waiting != 0){
        ZoneError(waiting);
    }

    print_zones(zones);

    write(name + ".cpp", text);
}