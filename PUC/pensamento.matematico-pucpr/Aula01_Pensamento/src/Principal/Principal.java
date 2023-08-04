package Principal;

import java.util.Scanner;

import TabelaVerdade.TabelaVerdade;

public class Principal {

	public static void main(String[] args) {
		Scanner sc = new Scanner (System.in); // Scanner é uma classe que faz leitura do teclado
		TabelaVerdade tv = new TabelaVerdade(); // vrum vrum instanciado vrum
		
		int opcao, esc;
		
		do {
			do {
				System.out.println("Escolha uma operação: 1 - E; 2 - OU; 3 - IMPLICAÇÃO; 4 - BICONDICIONAL;");
				opcao = sc.nextInt(); // armazena variavel
			} while ((opcao != 1) && (opcao != 2) && (opcao != 3) && (opcao != 4));
			
			System.out.println("Digite true or false pra A: ");
			boolean a = sc.nextBoolean();
			
			System.out.println("Digite true or false pra B: ");
			boolean b = sc.nextBoolean();
			
			switch (opcao) {
				case 1:
					tv.operacaoE(a, b);
					break;

				case 2:
					tv.operacaoOU(a, b);
					break;

				case 3:
					tv.operacaoIMP(a, b);
					break;

				case 4:
					tv.operacaoBIC(a, b);
					break;

				default:
					System.out.println("ALERTA: Você colocou número errado");
					break;
				}
			System.out.println("Continuar: SIM: [1] - NÃO: [0]");
			esc = sc.nextInt();
			
		} while (esc == 1);
		if (esc == 0) {
			System.out.println("Tchauzinho");
		}
			
				
	}

}
