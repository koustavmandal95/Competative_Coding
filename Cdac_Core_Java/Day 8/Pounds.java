package Forex;

public class Pounds implements CreditCard {
	float Balance;

	public Pounds(float balance) {
		Balance = balance;
	}

	@Override
	public float currentBalance() {
		return Balance;
	}
	
}
