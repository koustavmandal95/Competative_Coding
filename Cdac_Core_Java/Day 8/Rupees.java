package Forex;

public class Rupees implements CreditCard {
	float Balance;
	Rupees(){
		
	}
	public Rupees(float balance) {
		Balance = balance;
	}

	@Override
	public float currentBalance() {
		return Balance;
	}
}
