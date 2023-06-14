#include <stdio.h>
#include <stdlib.h>



int main() {
	
	//declarar o arquivo e as variaveis
	
	FILE *arquivo; 
	char caracter;
	int cont=0;
	
	// abrir o arquivo
	
	arquivo = fopen("documento1.txt", "r") ;
	/* se o arquivo nao estiver no mesmo diretório do arquivo em C, é necessário colocar o caminho todo*/
	
	if (arquivo == NULL)
		printf ("ERRO DURANTE A ABERTURA DO ARQUIVO.");
	else {
		while (fscanf (arquivo, "%c", &caracter) !=EOF)
			cont ++;
	
	fclose (arquivo);
	printf ("Foram encontrados %d caracteres", cont);	
	}
	
	
	
	
	return 0;
}