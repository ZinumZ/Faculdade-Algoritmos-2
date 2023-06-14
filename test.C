#include <stdio.h>

int soma(int a, int b) {
    return a + b;
}

int subtracao(int a, int b) {
    return a - b;
}

int multiplicacao(int a, int b) {
    return a * b;
}

int divisao(int a, int b) {
    return a / b;
}

int main() {
    int a = 10;
    int b = 5;

    printf("Soma: %d\n", soma(a, b));
    printf("Subtração: %d\n", subtracao(a, b));
    printf("Multiplicação: %d\n", multiplicacao(a, b));
    printf("Divisão: %d\n", divisao(a, b));

    return 0;
}





