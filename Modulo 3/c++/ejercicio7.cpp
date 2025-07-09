#include <iostream>
using namespace std;

float calcularAreaRectangulo(float base, float altura);

int main() {
    float base, altura;

    cout << "Ingresa la base del rectángulo: "<< endl;
    cin >> base;

    cout << "Ingresa la altura del rectángulo: "<< endl;
    cin >> altura;

    float area = calcularAreaRectangulo(base, altura);

    cout << "El área del rectángulo es: " << area << endl;

    return 0;
}

float calcularAreaRectangulo(float base, float altura) {
    return base * altura;
}
