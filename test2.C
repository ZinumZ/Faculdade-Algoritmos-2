/*faça o algoritmo de uma função real (recursiva) para retornar a média aritmética simples dos valores inteiros de uma lista simples. Return 0 no caso da lista estar vazia*/
#include <stdio.h>
#include <stdlib.h>

float media(float n, float soma) {
    if (n == 0) {
        return 0;
    } else {
        return soma / n;
    }
}

int main() {
    int vetor[5];
    float num, soma = 0;
    int i;

    for (i = 0; i < 5; i++) {
        printf("Digite o valor: ");
        scanf("%d", &vetor[i]);

        soma = soma + vetor[i];
    }

    float numElementos = 5; //Quantas pessoas para fazer a média
    float mediaCalculada = media(numElementos, soma);

    printf("Media: %.2f\n", mediaCalculada);
    return 0;
}
