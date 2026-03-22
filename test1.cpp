#include <iostream>
using namespace std;

int* crearVector(int tamaño) {
    int vector[100]; // ❌ ERROR: memoria local (stack)

    for (int i = 0; i < tamaño; i++) {
        vector[i] = i * 2;
    }

    return vector; // ❌ ERROR GRAVE: devuelve dirección de memoria inválida
}

int main() {
    int* v;
    v = crearVector(5);

    for (int i = 0; i < 5; i++) {
        cout << v[i] << endl; // ⚠️ comportamiento indefinido
    }

    return 0;
}