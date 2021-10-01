#include <iostream>
#include <fstream>
#include <vector>
#include <ctype.h> // for isalnum function

using namespace std;

typedef vector <char> vc;
typedef vector <string> vs;

vc read(string name){
    fstream file;
    vc commands;
    string line;
    bool commenting = false;
    
    file.open(name, ios::in);

    if (!file.is_open()){
        cout << "Could not open the file - '" << name << "'" << endl;
        return commands;
    }

    while (getline(file, line)){
        for(int i = 0; i < line.size(); i++){
            char ch = line[i];

            if(ch == '~'){
                commenting = !commenting;
            }
            else if(!commenting){
                commands.push_back(ch);
            }
            
            if(i == line.size() - 1){
                commands.push_back(' ');
            }
        }
    }

	file.close();
    return commands;
}

vs join(vc commands){
    string word = "";
    vs words;
    for(int i = 0; i < commands.size(); i++){
        char ch = commands[i];
        if(ch == ' '){
            if(word != ""){
                words.push_back(word);
            }
            word = "";
        }
        else{
            if(!isalnum(ch)){
                if(word != ""){
                    words.push_back(word);
                }
                word = "";
                word.push_back(ch);
                words.push_back(word);
                word = "";
            }
            else{
                word.push_back(ch);
            }
        }
    }
    return words;
}

void write(string file_name, string text){
    fstream file;
	file.open(file_name, ios::out);
    file << text;
	file.close();
}

template <typename list> // vector, stack, queue, string, array
void print_list(list l){
    for (const auto &i : l){
        cout << i << endl;
    }
}