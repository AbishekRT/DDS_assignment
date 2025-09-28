import datetime

# Patient class
class Patient:
    def __init__(self, patient_id, name, blood_type, urgency):
        self.patient_id = patient_id
        self.name = name
        self.blood_type = blood_type
        self.urgency = urgency  # 1 = most urgent, 5 = least urgent
        self.status = "Waiting"
        self.time_registered = datetime.datetime.now()

def __str__(self):
    return self.patient_id + " " + self.name + " " + self.blood_type + " " + str(self.urgency) + " " + self.status


# Global data structures
patients = []

# Blood type compatibility
compatibility = {
    "O": ["O", "A", "B", "AB"],   # universal donor
    "A": ["A", "AB"],
    "B": ["B", "AB"],
    "AB": ["AB"]
}

# Functions

def register_patient():
    print("\n--- Register New Patient ---")
    patient_id = input("Enter Patient ID: ").strip()
    name = input("Enter Name: ").strip()

    # validate blood type
    while True:
        blood_type = input("Enter Blood Type (O, A, B, AB): ").strip().upper()
        if blood_type in ["O", "A", "B", "AB"]:
            break
        else:
            print("Invalid blood type. Try again.")

    # validate urgency
    while True:
        try:
            urgency = int(input("Enter Urgency Level (1=Critical to 5=Stable): "))
            if 1 <= urgency <= 5:
                break
            else:
                print("Urgency must be between 1 and 5.")
        except ValueError:
            print("Please enter a number.")

    patient = Patient(patient_id, name, blood_type, urgency)
    patients.append(patient)
    print("Patient " + name + " registered successfully!")


def update_donor_availability():
    print("\n--- Donor Availability ---")
    donor_type = input("Enter Donor Blood Type (O, A, B, AB): ").strip().upper()
    if donor_type not in compatibility:
        print("Invalid blood type.")
        return

    compatible_types = compatibility[donor_type]
    compatible_patients = [p for p in patients if p.blood_type in compatible_types and p.status == "Waiting"]

    if not compatible_patients:
        print("No compatible patients found.")
        return

    # sort by urgency, then by time registered (FIFO if same urgency)
    compatible_patients.sort(key=lambda p: (p.urgency, p.time_registered))

    # pick the first one
    selected = compatible_patients[0]
    selected.status = "Matched"
    print(f"Patient {selected.name} (ID: {selected.patient_id}) matched for transplant!")


def complete_transplant():
    print("\n--- Complete Transplant ---")
    matched = [p for p in patients if p.status == "Matched"]

    if not matched:
        print("No patients currently matched.")
        return

    patient = matched[0]  # only one can be matched at a time
    patient.status = "Transplanted"
    print(f"Patient {patient.name} (ID: {patient.patient_id}) marked as Transplanted.")


def view_waiting_list():
    print("\n--- Waiting List ---")
    if not patients:
        print("No patients registered.")
        return

    print(f"{'ID':<6} {'Name':<10} {'BT':<3} {'Urg':<3} {'Status':<12}")
    print("-" * 40)
    for p in patients:
        print(p)


def check_matching_status():
    print("\n--- Matching Status ---")
    matched = [p for p in patients if p.status == "Matched"]
    if matched:
        patient = matched[0]
        print(f"Patient {patient.name} (ID: {patient.patient_id}) is currently matched and waiting for surgery.")
    else:
        print("No patients are currently matched. System is ready for next donor.")


# Main menu
# -------------------------------
def main():
    while True:
        print("\n====== Kidney Transplant Waiting List System ======")
        print("1. Register New Patient")
        print("2. Update Donor Availability")
        print("3. Complete Transplant Procedure")
        print("4. View Waiting List")
        print("5. Check Matching Status")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_patient()
        elif choice == "2":
            update_donor_availability()
        elif choice == "3":
            complete_transplant()
        elif choice == "4":
            view_waiting_list()
        elif choice == "5":
            check_matching_status()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# Run the program

if __name__ == "__main__":
    main()
