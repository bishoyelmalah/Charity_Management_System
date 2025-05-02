from DataBase import *

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