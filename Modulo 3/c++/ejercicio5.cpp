#include <iostream>

int main() {
    int numeroSecreto = 42;
    int intento;

    std::cout << "¡Adivina el número secreto!\n";

    while (true) {
        std::cout << "Ingresa tu adivinanza: ";
        std::cin >> intento;

        if (intento == numeroSecreto) {
            std::cout << "¡Correcto! Has adivinado el número.\n";
            break;
        } else if (intento < numeroSecreto) {
            std::cout << "Más alto...\n";
        } else {
            std::cout << "Más bajo...\n";
        }
    }

    return 0;
}
