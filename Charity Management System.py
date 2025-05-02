""" 
    Python Course 2025 @ AAST - Final Project
    Credits to Bishoy Mina El Malah 

"""

from DataBase import *
from Donors import *
from Donations import *
from Beneficiaries import *
from Helping_functions import *

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
        try:
            income = int(get_required_input("Enter Beneficiary's Income (Required): "))
            if is_ben_eligible(income):
                ben = Beneficiary()
                ben.add_ben(income)
        except Exception as e:
            print(e)
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