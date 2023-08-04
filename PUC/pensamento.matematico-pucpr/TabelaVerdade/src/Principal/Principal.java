package Principal;
import java.util.Scanner;
import TabelaVerdade.TabelaVerdade;

public class Principal {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		TabelaVerdade tv = new TabelaVerdade();

		System.out.print("\n---Tabela Verdade---\n");
		
		String E = "^";
		String OU = "v";
		int X = 1;
		
		tv.atribuicaoValoresTabela();
		
		while (X==1) {
			System.out.println("Digite uma sentença: "); 
			String stringLida = sc.nextLine();
			
			String a = stringLida.substring (0,1);
			String operacao = stringLida.substring (1,2);
			String b = stringLida.substring (2,3);
			
			if (stringLida.length() == 3) {
				
				switch(operacao) 
				{
					case "^":
						tv.operacaoE();
						break;
					case "v":
						tv.operacaoOU();
						break;
				}
			}
			
			else if (stringLida.length() == 4) {	
				tv.implicacao();	
			}
			
			else if (stringLida.length() == 5) {
				tv.bicondicional();
			}
		
	    }
	}
		
}

