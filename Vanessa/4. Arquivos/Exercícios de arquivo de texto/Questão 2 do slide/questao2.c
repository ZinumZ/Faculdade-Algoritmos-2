#include <stdio.h>
#include <stdlib.h>

int main() {
	
	FILE *arquivo1, *arquivo_novo;
	char caracter;
	
	arquivo1 = fopen ("documento1.txt", "r"); //leitura
	arquivo_novo = fopen ("documentonovo.txt", "w"); // escrita
	
	
	
	if ((arquivo1 == NULL) || (arquivo_novo == NULL))
		printf ("ERRO DURANTE A ABERTURA DO ARQUIVO");
	else {
		while (fscanf(arquivo1,"%c",&caracter)!=EOF){
			if ( (caracter>='a' && caracter<='z') || (caracter>='A' && caracter<='Z') )  // verificar se o caractere é uma letra
				fprintf (arquivo_novo,"%c", caracter);
		
		}	
		
	}
	
		
	fclose (arquivo1);
	fclose (arquivo_novo);
	return 0;
}