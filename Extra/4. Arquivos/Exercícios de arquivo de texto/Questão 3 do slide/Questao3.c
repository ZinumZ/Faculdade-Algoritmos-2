#include <stdio.h>
#include <stdlib.h>

#define delimitador '_'

int main() {
	
	struct  {
		char nome[50];
		int idade;
		float salario;
	} pessoa;
	

	int cont=0; /*vai contar a quantidade de pessoas*/
	
	FILE *arquivo;
		
	arquivo = fopen ("dadosdaspessoas.txt", "w");
	
	while (cont<4){
		
		
		printf ("Pessoa[%d]\n", cont+1);
		printf ("Nome: ");
		scanf ("%s", pessoa.nome); //string não precisa do &
		
		printf ("Idade: ");	
		scanf ("%s", &pessoa.idade); 
		
		printf ("Salario: ");	
		scanf ("%f", &pessoa.salario); 

		fprintf (arquivo, "%s", pessoa.nome);
		fprintf (arquivo, "%c", delimitador);
		fprintf (arquivo, "%d", pessoa.idade);
		fprintf (arquivo, "%c", delimitador);
		fprintf (arquivo, "%.2f", pessoa.salario);
		fprintf (arquivo, "\n"); /*cada linha vai ter dados de uma pessoa*/
		
		cont=cont+1;		
	}
	
	fclose (arquivo);
	 
	
	return 0;
}