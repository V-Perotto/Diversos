package TabelaVerdade;

public class TabelaVerdade {

	public void operacaoE(boolean a, boolean b) {
		if (a == true && b == true) {
			System.out.println("O resultado � VERDADEIRO");
		}
		else {
			System.out.println("O resultado � FALSO");	
		}
	}
	
	public void operacaoOU(boolean a, boolean b) {
		if (a == false && b == false) {
			System.out.println("O resultado � FALSO");
		}
		else {
			System.out.println("O resultado � VERDADEIRO");	
		}
	}
	
	public void operacaoIMP(boolean a, boolean b) {
		if (a == true && b == false) {
			System.out.println("O resultado � FALSO");
		}
		else {
			System.out.println("O resultado � VERDADEIRO");	
		}
	}
	
	public void operacaoBIC(boolean a, boolean b) {
		if ((a == true && b == true) || (a == false && b == false)) {
			System.out.println("O resultado � VERDADEIRO");
		}
		else {
			System.out.println("O resultado � FALSO");	
		}
	}
	
}
