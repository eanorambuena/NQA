#include <iostream>

using namespace std;

void ZoneError(int w){
    cout << "ZoneError: Wrong number of parenthesis" << endl;
    cout << w << endl;
}

void MissingZoneError(int position){
    cout << "MissingZoneError: Missing parenthesis in position " << position << endl;
}

void IncludeError(string file){
    cout << "IncludeError: Could not include " << file << endl;
}