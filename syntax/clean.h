#include <iostream>
#include <vector>
#include <queue>

using namespace std;

typedef vector <string> vs;
typedef queue <string> qs;

vs split(string str, char pattern) {
    
    int posInit = 0;
    int posFound = 0;
    string splitted;
    vs results;
    
    while(posFound >= 0){
        posFound = str.find(pattern, posInit);
        splitted = str.substr(posInit, posFound - posInit);
        posInit = posFound + 1;
        results.push_back(splitted);
    }
    
    return results;
}

qs comment(vs commands){
    qs instructions;
    bool commenting = false;
    string word;
    vs words;
    for(int i = 0; i < commands.size(); i++){
        word = commands[i];
        words =  split(word, '~');
        if(!commenting){
            instructions.push(word);
        }
    }
    return instructions;
}
