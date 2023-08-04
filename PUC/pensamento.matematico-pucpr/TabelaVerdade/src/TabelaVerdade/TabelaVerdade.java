package TabelaVerdade;

public class TabelaVerdade {
	
	String[][] matriz = new String[5][8];
	
	public void atribuicaoValoresTabela() {
		
		
		//TabelaVerdade tabelaVerdade = new TabelaVerdade();
		
		//Scanner scanner = new Scanner(System.in);
			
		
		matriz[0][0] = "p ";
		matriz[1][0] = "V ";
		matriz[2][0] = "V ";
		matriz[3][0] = "F ";
		matriz[4][0] = "F ";
		
		matriz[0][1] = "q";
		matriz[1][1] = "V ";
		matriz[2][1] = "F ";
		matriz[3][1] = "V ";
		matriz[4][1] = "F ";
		
		matriz[0][2] = "~p";
		matriz[1][2] = "F ";
		matriz[2][2] = "F ";
		matriz[3][2] = "V ";
		matriz[4][2] = "V" ;
		
		matriz[0][3] = "~q";
		matriz[1][3] = "F";
		matriz[2][3] = "V";
		matriz[3][3] = "F";
		matriz[4][3] = " V";
		
		
		
		for (int i = 0; i < 5; i++) { //linha
		
			for (int j = 0; j < 4; j++) { //coluna
				System.out.print("  "+ matriz[i][j]+ " ");	 
				}
			System.out.println();		
			}	
	
	}
	public void implicacao() {
		matriz[0][4] = "p -> q";
		matriz[1][4] = "  V";
		matriz[2][4] = "  F";
		matriz[3][4] = "  V";
		matriz[4][4] = "  V";
		
		System.out.println();
		for (int i = 0; i < 5; i++) { //linha
			
			//for (int j = 0; j < 5; j++) { //coluna
				System.out.print(matriz[i][4]);	 
				//}
			System.out.println();}
		System.out.println();
	}
	public void operacaoE() {
		matriz[0][5] = "p ^ q";
		matriz[1][5] = "  V";
		matriz[2][5] = "  F";
		matriz[3][5] = "  F";
		matriz[4][5] = "  F";
		
		System.out.println();
		for (int i = 0; i < 5; i++) { //linha
			
		//	for (int j = 0; j < 6; j++) { //coluna
				System.out.print(matriz[i][5]);	 
			//	}
			System.out.println();}
		System.out.println();
	}
	public void operacaoOU() {
		matriz[0][6] = "p v q";
		matriz[1][6] = "  V";
		matriz[2][6] = "  F";
		matriz[3][6] = "  V";
		matriz[4][6] = "  V";
		
		System.out.println();
		for (int i = 0; i < 5; i++) { //linha
			
			//for (int j = 0; j < 7; j++) { //coluna
				System.out.print(matriz[i][6]);	 
				//}
			System.out.println();}
		System.out.println();
		}
	public void bicondicional() {
		matriz[0][7] = "p <-> q";
		matriz[1][7] = "   V";
		matriz[2][7] = "   F";
		matriz[3][7] = "   F";
		matriz[4][7] = "   V";
		
		System.out.println();
		for (int i = 0; i < 5; i++) { //linha
			
			//for (int j = 0; j < 8; j++) { //coluna
				System.out.print(matriz[i][7]);	 
				//}
			System.out.println();}
		System.out.println();	
		
	}	
}