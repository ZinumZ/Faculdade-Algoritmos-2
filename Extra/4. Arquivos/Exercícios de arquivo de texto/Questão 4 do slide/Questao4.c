#include <stdio.h>
#include <stdlib.h>



	
#define delimitador '_'

typedef struct {
	char nome[50];
	int idade;
	float salario;
} Tpessoa;

int main() {
	
	Tpessoa pessoa[4];
	FILE *arquivo;
	int cont=0;
	float mediasal=0;
	
	arquivo = fopen ("dadosdaspessoas.txt", "r");
	
	while (cont<4){
		fscanf (arquivo, "%[^_]s", pessoa[cont].nome);
		fscanf (arquivo, "_%d", &pessoa[cont].idade);
		fscanf (arquivo, "_%f", &pessoa[cont].salario);
	
		mediasal+= pessoa[cont].salario;
		cont++;
	
	}
	fclose (arquivo);
	mediasal/=4;
	printf ("A media salarial eh %.2f", mediasal);
	
	return 0;
}