package Forex;

public class Dollars implements CreditCard{
	float Balance;
	public Dollars(float balance) {
		Balance = balance;
	}

	@Override
	public float currentBalance() {
		return Balance;
	}
	
}
