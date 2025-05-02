from Helping_functions import *
from datetime import datetime

class Donation:
    def add_donation(self):
        user = get_donor_auth()
        if user is None:
            print(" --------- Authentication failed. Returning to the Main Menu .... ---------\n")
            return
        print("\n===============================================")
        print("============= Adding New Donation =============")
        print("===============================================\n")
        try:
            self.amount = int(get_required_input("Enter the amount of Donation: "))
            while self.amount <= 0:
                print("Amount must be a positive number.")
                self.amount = int(get_required_input("Enter the amount of Donation: "))
            self.type = get_required_input("Enter the type of Donation (Cash / Non-Cash): ")
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user.donations[current_time] = self
            user.total_donations += self.amount
            donations_DB[current_time] = {user.name: self}
            print("\n -------- Donation added Successfully -------- \n")
        except Exception as e:
            print(f"{e}")