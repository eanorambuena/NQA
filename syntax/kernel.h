#include <vector>
#include <stack>
#include <queue>

#include "file.h"
#include "clean.h"

using namespace std;

typedef vector <string> vs;
typedef stack <string> ps; // "p" for the Spanish word "pila" in order to use "s" only for strings
typedef queue <string> qs;

void compile(string name){
    ps zones, waiting;
    vs words = read(name);
    print_list(words);
    qs commands = comment(words);
    cout << "fin" << endl;
}