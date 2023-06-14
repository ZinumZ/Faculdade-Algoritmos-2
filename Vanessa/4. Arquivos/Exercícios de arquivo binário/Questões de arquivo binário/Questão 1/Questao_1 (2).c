#include <stdio.h>
#include <stdlib.h>

typedef struct TBolsista {
	int codigo;
	char nome[30];
	int tipobolsa;
	char email [30];
} TBolsista;



int main() {

	FILE *arq;
	
	TBolsista bolsista;
	int cont;
	int qtd;
	
	printf ("Qual a quantidade de bolsistas a registrar?\n Quantidade: ");
	scanf ("%d", &qtd);
	
	while (qtd<5){
		printf ("Quantidade inválida! Deve ser no mínimo 5! Digite novamente.\n Quantidade: ");
		scanf ("%d", &qtd);	
	}
	
	arq= fopen ("bolsista1.cad","wb");
	
	if (arq==NULL)
		printf ("Erro ao abrir o arquivo!");
	else {
		// ler e gravar os elementos no arquivo
		for (cont=1; cont<=qtd;cont++){
			//leitura de um elemento por vez
			printf ("Codigo: ");
			scanf ("%d", &bolsista.codigo);
			
			printf ("Nome: ");
			scanf (" %[^\n]s", bolsista.nome);
			
			printf ("Tipo de Bolsa: ");
			scanf ("%d", &bolsista.tipobolsa);

			printf ("E-mail: ");
			scanf (" %[^\n]s", bolsista.email);
			
			
			// vai adaptar o exercicio dois, fazendo com que a ordem seja crescente de acordo com o código do bolsista
			// cria comando de mudar o local do cursos, antes de gravar
			
			fseek (arq, sizeof (struct TBolsista) *(bolsista.codigo-1),SEEK_SET);
			
			
			fwrite (&bolsista, sizeof (struct TBolsista),1,arq);
			
			//vai adaptar o exercicio 4, entao vamos ler o código do bolsista e vamos atualizar o tipo de bolsa
			
			arq= fopen ("blsista1.cad", "rb+");
			int cod;
			
			if (arq!=NULL){
				printf ("Qual o código do bolsista para atualizão? \codigo: ");
				scanf ("%d", %cod);
				//leitura do bolsista da posicao cod
				fseek (arq, sizeof (TBolsista)*(cod-1), SEEK_SET);
				fread (&bolsista, sizeof (TBolsista),1,arq);
				//atualização do tipo de bolsa
				printf ("O bolsista eh do tipo %d. Para qual tipo dseja modificar? ", bolsista.tipobolsa);
				scanf ("%d", &bolsista.tipobolsa);
				// atualização no arquivo
				fseek (arq, sizeof (TBolsista)*(cod-1), SEEK_SET);
				fwrite (&bolsista, sizeof (TBolsista),1,arq);
				fclose (arq);	
			}
			
			
			
							
		}
	fclose(arq);
	}
	
	
	arq=fopen ("bolsista1.cad","rb");
	
	while (!feof(arq))
		if (fread (&bolsista, sizeof(struct TBolsista), 1, arq )) {
			printf ("Código: %d\n", bolsista.codigo);
			printf ("Nome: %s\n", bolsista.nome);
			printf ("Tipo de Bolsa: %d\n", bolsista.tipobolsa);
			printf ("E-mail: %s\n", bolsista.email);
		}
		
	fclose(arq);
	
	
	
	
	
	
	
	return 0;
}