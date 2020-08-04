package Forex;
public	class BankAccount implements CreditCard {
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
		
		@Override
		public float currentBalance() {
			return totalBalance;
		}
		@Override
		public String toString() {
			return "BankAccount [accountNumber=" + accountNumber + ", totalBalance=" + totalBalance + "]";
		}
		

	}

