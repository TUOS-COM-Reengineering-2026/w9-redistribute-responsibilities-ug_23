from Account import Account
from Branch import Branch
from Customer import Customer
from Payroll import Payroll
from Staff import Staff


class Bank:
    def __init__(self):
        self.accounts = []
        self.customers = []
        self.customer_addresses = {}  # key: customer, value: address
        self.customer_phone_numbers = {}  # key: customer, value: phone number
        self.branches = []
        self.payroll = None

    def setup_branch(self, branch: Branch):
        self.branches.append(branch)

    def close_branch(self, branch: Branch, transfer_branch: Branch):
        for staff in branch.get_staff():
            self.transfer_staff_member(branch, transfer_branch, staff)
        self.branches.remove(branch)

    def transfer_staff_member(self, from_branch: Branch, to_branch: Branch, staff: Staff):
        from_branch.remove_staff_member(staff)
        to_branch.add_staff_member(staff)

    def setup_new_account(self, account: Account, customer: Customer):
        account.set_customer(customer)
        self.accounts.append(account)

        if customer not in self.customers:
            self.customers.append(customer)

    def obtain_balance(self, account: Account):
        return account.get_balance()

    # RP2 - Moved behaviour to Account.py
    def add_interest(self, account: Account):
        account.add_interest()

    # RP2 - Moved behaviour to Account.py
    def add_funds(self, account: Account, amount: float):
        account.add_funds(amount)

    # RP2 - Moved behaviour to Account.py
    def close_account(self, account: Account):
        account.close_account()
        self.accounts.remove(account)

    def change_payroll_date(self, payroll: Payroll, date: str, staff_category: str):
        self.payroll = payroll
        self.payroll.get_staff_category_pay_schedule(staff_category).set_pay_date(date)
