#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double num1, num2;

    cout << "Introduce el primer número: ";
    cin >> num1;
    cout << "Introduce el segundo número: ";
    cin >> num2;

    cout << "Suma: " << num1 + num2 << endl;
    cout << "Resta: " << num1 - num2 << endl;
    cout << "Multiplicación: " << num1 * num2 << endl;
    cout << "División: " << num1 / num2 << endl;

    cout << "Potencia: " << pow(num1, num2) << endl;
    cout << "Raíz cuadrada del primer número: " << sqrt(num1) << endl;

    return 0;
}
