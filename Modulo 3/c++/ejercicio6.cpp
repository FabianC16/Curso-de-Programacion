#include <iostream>
using namespace std;

int main() {
    int opcion;

    
    do {
        cout << "\n MENU " << endl;
        cout << "1.Saludar" << endl;
        cout << "2.Despedirse" << endl;
        cout << "3.Salir" << endl;
        cout << "Elige una opcion: ";
        cin >> opcion;

        switch (opcion) {
            case 1:
                cout <<"Hola Que tengas un buen dia"<< endl;
                break; 
            case 2:
                cout <<"Adios Vuelve pronto"<< endl;
                break;
            case 3:
                cout <<"Saliendo del programa"<< endl;
                break;
            default: 
                cout <<"Opcion no valida Por favor, intenta de nuevo"<< endl;
                break;
        }

    } while (opcion != 3); 

    return 0;
}
