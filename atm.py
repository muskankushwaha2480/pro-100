class Atm(object):
    def __init__(self,atm_card_no,pin_card_no):
        self.atm_card_no = atm_card_no
        self.pin_card_no = pin_card_no

    def checkingAccountBalance(self):
        print("you are having enough balance")

    def cashWithdrawl(self):
        print("cash withdrawaled")

atm_card_no = int(input("Enter your atm card no. : "))
pin_card_no = int(input("Enter the pin card no. : "))

atm = Atm(23456789 , 1234 )
atm.cashWithdrawl()
atm.checkingAccountBalance()
