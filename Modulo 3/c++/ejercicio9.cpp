#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    vector<string> comidas;
    string comida;

    cout << "Ingresa tus 3 comidas favoritas:" <<endl;

    for (int i = 1; i <= 3; i++) {
        cout << "Comida " << i << ": ";
        getline(cin, comida);
        comidas.push_back(comida);
    }

    cout << "\nTus comidas favoritas son:" << endl;
    for (const string& c : comidas) {
        cout << "- " << c << endl;
    }

    return 0;
}
