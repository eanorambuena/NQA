#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef vector <string> vs;

vs read(string name){
    fstream file;
	file.open(name, ios::in);

    vs commands;
    string word;
    
    if (!file.is_open()){
        cout << "Could not open the file - '" << name << "'" << endl;
        return commands;
    }

    while (file >> word){
        commands.push_back(word);
    }

	file.close();
    return commands;
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