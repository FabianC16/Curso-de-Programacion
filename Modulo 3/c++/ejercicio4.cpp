#include <iostream>
#define LIMITE 10

int main() {
    int numero;
    std::cout << "Introduce un número: ";
    std::cin >> numero;

    std::cout << "Tabla de multiplicar del " << numero << ":\n";
    for (int i = 1; i <= LIMITE; ++i) {
        std::cout << numero << " x " << i << " = " << numero * i << std::endl;
    }

    return 0;
}
