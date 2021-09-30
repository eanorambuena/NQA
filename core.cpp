#include <iostream>
#include <conio.h>
#include <fstream>
#include <vector>
#include <stack>

#include "syntax/kernel.h"

using namespace std;

typedef vector <string> vs;

int main(int argc, char *argv[]){
    if(argc < 2){
        cout << "Error" <<endl;
        return -1;
    }

    string command = argv[1];

    if(command == "compile"){
        string name = argv[2];
        compile(name);
    }
    
    getch();
    return 0;
}