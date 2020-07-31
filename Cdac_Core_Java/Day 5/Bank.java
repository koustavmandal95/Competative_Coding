class BankAccount {
		int accountNumber;
		float totalBalance;
		public BankAccount(int accountNumber, float totalBalance) {
			this.accountNumber = accountNumber;
			this.totalBalance = totalBalance;
		}
		void deposit(float amount) {
			this.totalBalance = this.totalBalance + amount;
			System.out.println("The amount deposited is "+ amount + " and the net balance is "+this.totalBalance);
		}
		void withdrawal(float withdrawalAmt) {
			if(this.totalBalance - withdrawalAmt < 0) {
				System.out.println("Transaction not possible");
			}
			else {
				this.totalBalance = this.totalBalance - withdrawalAmt;
				System.out.println("The withdrawal is "+withdrawalAmt +" & net amount is "+this.totalBalance );
			}
		}
		void getBalance() {
			System.out.println("Your available balance is " + this.totalBalance);
		}

	}
class checkingAccount extends BankAccount {
			
	private float fee;
	public checkingAccount(int accountNumber, float totalBalance,float fee) {
		super(accountNumber, totalBalance);
		this.fee = fee;
	}
	void deductfee() {
		super.totalBalance = super.totalBalance - this.fee;
		System.out.println("The net balance after deduction of "+ this.fee + " is " + super.totalBalance);
	}
}

class savingAccount extends BankAccount{
	private float interestRate;
	public savingAccount(int accountNumber, float totalBalance,float interestRate) {
		super(accountNumber, totalBalance);
		this.interestRate = interestRate;
	}
	void addInterest() {
		super.totalBalance = super.totalBalance + (interestRate*1*super.totalBalance/100);
	}
}

public class Bank {
	public static void main(String[] args) {
		System.out.println("*************************************************");
		
		BankAccount acc1 = new BankAccount(1000,3445.34f);
		acc1.deposit(12000.0f);
		acc1.withdrawal(1234.4f);
		acc1.getBalance();
		
		System.out.println("*************************************************");
		

		checkingAccount cch1 = new checkingAccount(2100,50000f,10f);
		cch1.deposit(1000f);
		cch1.getBalance();
		cch1.deductfee();
		
		System.out.println("*************************************************");
		savingAccount sav1 = new savingAccount(2000,50000f,2.0f);
		sav1.deposit(1030f);
		sav1.withdrawal(1000f);
		sav1.addInterest();
		sav1.getBalance();
	}
}
