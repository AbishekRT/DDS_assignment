import datetime
import heapq

# Patient class
class Patient:
    def __init__(self, patient_id, name, blood_type, urgency):
        self.patient_id = patient_id
        self.name = name
        self.blood_type = blood_type
        self.urgency = urgency  # 1 = most urgent, 5 = least urgent
        self.status = "Waiting"
        self.time_registered = datetime.datetime.now()

    def __lt__(self, other):
        # Priority by urgency, then by time registered
        return (self.urgency, self.time_registered) < (other.urgency, other.time_registered)

    def __str__(self):
        return f"{self.patient_id:<6} {self.name:<10} {self.blood_type:<3} {self.urgency:<3} {self.status:<12}"

# Global data structures
patients_heap = []  # priority queue (min-heap)

compatibility = {
    "O": ["O", "A", "B", "AB"],
    "A": ["A", "AB"],
    "B": ["B", "AB"],
    "AB": ["AB"]
}

# Functions
def register_patient():
    print("\n--- Register New Patient ---")
    pid = input("Enter Patient ID: ").strip()
    name = input("Enter Name: ").strip()
    
    while True:
        bt = input("Enter Blood Type (O, A, B, AB): ").strip().upper()
        if bt in ["O", "A", "B", "AB"]:
            break
        print("Invalid blood type.")

    while True:
        try:
            urg = int(input("Enter Urgency Level (1=Critical to 5=Stable): "))
            if 1 <= urg <= 5:
                break
            else:
                print("Urgency must be 1–5.")
        except ValueError:
            print("Please enter a number.")

    p = Patient(pid, name, bt, urg)
    heapq.heappush(patients_heap, p)
    print(f"Patient {name} added successfully!")

def update_donor_availability():
    print("\n--- Donor Availability ---")
    donor_type = input("Enter Donor Blood Type (O, A, B, AB): ").strip().upper()
    if donor_type not in compatibility:
        print("Invalid blood type.")
        return

    compatible = compatibility[donor_type]
    waiting = [p for p in patients_heap if p.blood_type in compatible and p.status == "Waiting"]

    if not waiting:
        print("No compatible patients found.")
        return

    # find the highest priority patient (heap property ensures efficiency)
    waiting.sort()  # ensures correct order if multiple compatible exist
    selected = waiting[0]
    selected.status = "Matched"
    print(f"Patient {selected.name} (ID: {selected.patient_id}) matched for transplant!")

def complete_transplant():
    print("\n--- Complete Transplant ---")
    matched = [p for p in patients_heap if p.status == "Matched"]
    if not matched:
        print("No matched patients.")
        return
    patient = matched[0]
    patient.status = "Transplanted"
    print(f"Patient {patient.name} successfully transplanted!")

def view_waiting_list():
    print("\n--- Waiting List ---")
    if not patients_heap:
        print("No patients registered.")
        return
    print(f"{'ID':<6} {'Name':<10} {'BT':<3} {'Urg':<3} {'Status':<12}")
    print("-" * 40)
    for p in sorted(patients_heap):
        print(p)

def main():
    while True:
        print("\n===== Kidney Transplant Waiting List System =====")
        print("1. Register New Patient")
        print("2. Update Donor Availability")
        print("3. Complete Transplant")
        print("4. View Waiting List")
        print("5. Exit")

        c = input("Enter your choice: ").strip()
        if c == "1":
            register_patient()
        elif c == "2":
            update_donor_availability()
        elif c == "3":
            complete_transplant()
        elif c == "4":
            view_waiting_list()
        elif c == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
