from Helping_functions import *

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
        try:
            amount = int(get_required_input("Enter the amound of Aid: ").strip())
            self.aids += amount
            print("\n --------- Aid Allocated Successfully ---------\n")
        except Exception as e:
            print(e)