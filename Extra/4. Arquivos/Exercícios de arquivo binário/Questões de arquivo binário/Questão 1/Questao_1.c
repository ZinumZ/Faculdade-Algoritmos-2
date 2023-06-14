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
			
			fwrite (&bolsista, sizeof (struct TBolsista),1,arq);
			
									
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