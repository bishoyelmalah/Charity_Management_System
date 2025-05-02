""" 
    Python Course 2025 @ AAST - Final Project
    Credits to Bishoy Mina El Malah 

"""

from datetime import datetime

# ========== DataBase ==================================

donors_DB = {}
donations_DB = {}
beneficiary_DB = {}

# ======== Main Classes ================================

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


class Donation:
    def add_donation(self):
        user = get_donor_auth()
        if user is None:
            print(" --------- Authentication failed. Returning to the Main Menu .... ---------\n")
            return
        print("\n===============================================")
        print("============= Adding New Donation =============")
        print("===============================================\n")
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


class Beneficiary:
    def add_ben(self, income):
        print("\n==============================================")
        print("=========== Adding New Beneficiary ===========")
        print("================================================\n")
        self.name = get_required_input("Enter the Beneficiary's Name (Required): ")
        self.contact = get_required_input("Enter the Beneficiary's Contact - Email/Phone (Required): ")
        self.income = income
        self.aids = 0
        beneficiary_DB[self.name] = self
        print("\n -------- Beneficiary added Successfully -------- \n")

    def get_info(self):
        print("\n")
        for key, value in self.__dict__.items():
            print(f" - {key.capitalize()}: {value}")
        change = get_required_input("\nDo you want to change any information? (y/n): ").lower()
        if change == "y":
            self.change_info()

    def change_info(self):
        print(f"\nIf you don't want to change specific field leave it blank by pressing enter.\n")
        for key, value in self.__dict__.items():
            if (key == "aids"):
                continue
            new_value = input(f" - {key.capitalize()} ({value}): ").strip()
            if key == "name":
                beneficiary_DB[new_value] = beneficiary_DB[self.name]
                del beneficiary_DB[self.name]
            if new_value != "":
                setattr(self, key, new_value)
        
        print("\n ------- Beneficiary information updated successfully -------\n")

    def allocate_aid(self):
        amount = int(get_required_input("Enter the amound of Aid: ").strip())
        self.aids += amount
        print("\n --------- Aid Allocated Successfully ---------\n")




# ================ Helping Functions ======================================

def menu():
    print("\n[1] Register Donor")
    print("[2] Show/Edit Donor Information")
    print("[3] Register Beneficiary")
    print("[4] Show/Edit Beneficiary Information")
    print("[5] Add Donation")
    print("[6] Allocate Donation")
    print("[7] Generate Reports")
    print("[8] Exit\n")


def get_required_input(text):
    value = input(text).strip()
    while value == "":
        value = input(text).strip()
    return value


def get_donor_auth():
    username = get_required_input("Enter the username of the Donor's account:  ")
    if (username not in donors_DB):
        print("\nSorry, we didn't find this username in our DataBase.\nMake sure you entered it correctly or add this Donor to the system by pressing [1] in the Main Menu.\n")
        return
    
    password = get_required_input("Enter the password: ").strip()
    counter = 3
    while(password != donors_DB[username].password and counter != 0):
        print(f" ------------ The password you've enterd is wrong. You have {counter} tries left. ------------\n")
        password = get_required_input("Enter the password: ").strip()
        counter -= 1
    
    if (counter == 0):
        print("\nSorry you tried to enter the password many times. Please try again later.\n")
        return
    
    return donors_DB[username]


def get_ben_auth():
    ben = get_required_input("Enter the Beneficiary's Name: ").strip()
    if ben not in beneficiary_DB:
        return
    return beneficiary_DB[ben]


def show_donors_report():
    counter = 1
    for donor in donors_DB.values():
        print(f"\n ============== {counter} ==============")
        for key, value in donor.__dict__.items():
            if key == "password" or key == "donations":
                continue
            elif key == "total_donations":
                print(f"Total Donations: {value} $")
            else:
                print(f"{key.capitalize()}: {value}")
        counter += 1


def show_ben_report():
    counter = 1
    for ben in beneficiary_DB.values():
        print(f"\n ============== {counter} ==============")
        for key, value in ben.__dict__.items():
            if key == "aids":
                print(f"Total Aids: {value}")
            else:
                print(f"{key.capitalize()}: {value}")



def show_donations_report():
    for key, value in donations_DB.items():
        for donor, donation in value.items():
            print(f"{key} >> {donor}")
            print(f" - Amount: {donation.amount}")
            print(f" - Type: {donation.type}\n")



def is_ben_eligible(income):
    if income <= 1000:
        return True
    else:
        print("\n --------- Sorry, this Beneficiary's income is more than 1000 $ --------- \n")
        return False

def get_report():
    print("\n[1] Donors Report")
    print("[2] Beneficiraies Report")
    print("[3] Donations Report\n")
    choice = get_required_input("Enter the number of your choice: ")

    if choice == "1":
        # Donors Report
        show_donors_report()
    elif choice == "2":
        # Beneficiaries Report
        show_ben_report()
    elif choice == "3":
        # Donations Report
        show_donations_report()
    else:
        print("\n --------- Sorry, you've entered unknown choice ---------")

# ========== Main Program =================================

print("\n==================================================================")
print("============ Welcome to the Charity Management System ============")
print("==================================================================")
while(True):
    menu()
    choice = get_required_input("Enter the number of your choice: ")
    if (choice == "1"):
        # Register Donor
        donor = Donor()
        donor.add_donor()
    elif (choice == "2"):
        # Show/Edit Donor Information
        user = get_donor_auth()
        if user is None:
            print(" ---------- Authentication failed. Returning to the Main Menu. ----------")
            continue
        user.get_info()
    elif (choice == "3"):
        # Regisiter Beneficiary
        income = int(get_required_input("Enter Beneficiary's Income (Required): "))
        if is_ben_eligible(income):
            ben = Beneficiary()
            ben.add_ben(income)
    elif (choice == "4"):
        # Show/Edit Beneficiary Information
        ben = get_ben_auth()
        if ben is None:
            print("\n -------- Sorry, we didn't find this Beneficiary in our DataBase --------")
            continue
        ben.get_info()
    elif (choice == "5"):
        # Add Donation
        donation = Donation()
        donation.add_donation()
    elif (choice == "6"):
        # Aid Allocation
        ben = get_ben_auth()
        if ben is None:
            print(" -------- Sorry, we didn't find this Beneficiary in our DataBase --------")
            continue
        ben.allocate_aid()
    elif (choice == "7"):
        # Generate Reports
        get_report()
    elif (choice == "8"):
        # Exit
        print("\n==================================================================")
        print("============ Thank you for using our system, GoodBye! ============")
        print("==================================================================")
        break
    else:
        print("\n --------- Sorry, you've entered unknown choice ---------")