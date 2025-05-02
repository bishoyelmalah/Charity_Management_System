from Helping_functions import *

class Donor:
    def add_donor(self):
        print("\n========================================")
        print("=========== Adding New Donor ===========")
        print("========================================\n")
        self.name = get_required_input("Enter the Donor's Name (Required): ")
        self.username = get_required_input("Enter a username for Donor's account (Required | Can't be changed): ")
        self.contact = get_required_input("Enter the Contact info - Email/Phone (Required): ")
        self.password = get_required_input("Enter a password for Donor's account (Required): ")
        self.total_donations = 0
        self.donations = {}
        donors_DB[self.username] = self
        print("\n -------- Donor added Successfully --------\n")


    def get_info(self):
        print(f"\n========= Hello, {self.name} =========")
        print("Showing info ....\n")
        for key, value in self.__dict__.items():
            if key == "donations":
                self.get_donations()
                continue
            elif key == "password":
                continue
            elif key == "total_donations":
                print(f"Total Donations: {value} $")
            else:
                print(f"{key.capitalize()}: {value}")

        change = get_required_input("\nDo you want to change any information? (y/n): ").lower()
        if change == 'y':
            self.change_info()


    def change_info(self):
        print(f"\nIf you don't want to change specific field leave it blank by pressing enter.\n")
        for key, value in self.__dict__.items():
            if key == "donations" or key == "username" or key == "total_donations":
                continue
            elif key == "password":
                change_pass = get_required_input(f"Change the Password (y/n): ").lower()
                if change_pass == 'y':
                    self.change_pass(key)
                    break
            else:
                change = input(f"Change {key.capitalize()} ({value}): ").strip()
                if change != "":
                    setattr(self, key, change)


    def change_pass(self, key):
        old_pass = get_required_input("Enter your old password: ").strip()
        if old_pass == self.password:
            new_pass = get_required_input("Enter the new password: ").strip()
            setattr(self, key, new_pass)
        else:
            print(" --------- Sorry, you entered wrong password! ---------")

    def get_donations(self):
        print("\nDonations:")
        for date, donation in self.donations.items():
            print(f" - {date} >> Amount: {donation.amount} | Type: {donation.type}")