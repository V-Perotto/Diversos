package TabelaVerdade;

public class TabelaVerdade {

	public void operacaoE(boolean a, boolean b) {
		if (a == true && b == true) {
			System.out.println("O resultado é VERDADEIRO");
		}
		else {
			System.out.println("O resultado é FALSO");	
		}
	}
	
	public void operacaoOU(boolean a, boolean b) {
		if (a == false && b == false) {
			System.out.println("O resultado é FALSO");
		}
		else {
			System.out.println("O resultado é VERDADEIRO");	
		}
	}
	
	public void operacaoIMP(boolean a, boolean b) {
		if (a == true && b == false) {
			System.out.println("O resultado é FALSO");
		}
		else {
			System.out.println("O resultado é VERDADEIRO");	
		}
	}
	
	public void operacaoBIC(boolean a, boolean b) {
		if ((a == true && b == true) || (a == false && b == false)) {
			System.out.println("O resultado é VERDADEIRO");
		}
		else {
			System.out.println("O resultado é FALSO");	
		}
	}
	
}
