#include <iostream>
using namespace std;

const double PI = 3.14159;

void calcularPerimetro(double radio) {
    double perimetro = 2 * PI * radio;
    cout << "El perímetro del círculo es: " << perimetro << endl;
}

int main() {
    double radio;

    cout << "Ingresa el radio del círculo: ";
    cin >> radio;

    calcularPerimetro(radio);

    return 0;
}
