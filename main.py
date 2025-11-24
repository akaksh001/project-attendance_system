# Employee Attendance System 

attendance_list = []

# ANSI color codes (can be removed if not needed)
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
END = "\033[0m"
BOLD = "\033[1m"

 

def is_valid_name(name):
    return name.replace(" ", "").isalpha() 

def is_unique_id(employee_id):
    return not any(rec['id'] == employee_id for rec in attendance_list)

def is_valid_status(status):
    return status.lower() in ("present", "absent")

def print_heading(title, emoji=""):
    print(f"\n{BOLD}{CYAN}{'='*40}\n{emoji} {title}\n{'='*40}{END}")

def create_attendance():
    print_heading("Create Attendance Record", "🆕")
    while True:
        employee_id = input("Employee ID: ").strip()
        if not employee_id:
            print(f"{RED}❌ Employee ID cannot be empty. Please enter again.{END}")
            continue
        if not is_unique_id(employee_id):
            print(f"{RED}❌ Employee ID already exists. Please enter a unique ID.{END}")
            continue
        break

    # << Check if the user adding correct data >>

    while True: 
        name = input("Name: ").strip()
        if not is_valid_name(name):
            print(f"{RED}❌ Name must contain only alphabets. Please enter again.{END}")
        else:
            break

    while True:
        status = input("Status (present/absent): ").strip().lower()
        if not is_valid_status(status):
            print(f"{RED}❌ Status must be 'present' or 'absent'. Please enter again.{END}")
        else:
            break
 
# Making Records of the attendence 

    record = {'id': employee_id, 'name': name, 'status': status}
    attendance_list.append(record)
    print(f"{GREEN}✅ Record created.{END}")

def read_attendance():
    print_heading("All Attendance Records", "📋")
    if not attendance_list:
        print(f"{RED}No records found.{END}")
        return
    # Table headers
    print(f"{BOLD}| {'ID':<10} | {'Name':<20} | {'Status':<8} |{END}")
    print("-"*46)
    for rec in attendance_list:
        status_color = GREEN if rec['status'] == "present" else RED
        print(f"| {rec['id']:<10} | {rec['name']:<20} | {status_color}{rec['status']:<8}{END} |")
    print("-"*46)

def update_attendance():
    print_heading("Update Attendance Record", "🔄")
    employee_id = input("Enter Employee ID to update: ").strip()
    for rec in attendance_list:
        if rec['id'] == employee_id:
            while True:
                status = input("New Status (present/absent): ").strip().lower()
                if not is_valid_status(status):
                    print(f"{RED}❌ Status must be 'present' or 'absent'. Please enter again.{END}")
                else:
                    rec['status'] = status
                    print(f"{GREEN}✅ Record updated.{END}")
                    return
    print(f"{RED}❌ Employee not found.{END}")

def delete_attendance():
    print_heading("Delete Attendance Record", "🗑️")
    employee_id = input("Enter Employee ID to delete: ").strip()
    for rec in attendance_list:
        if rec['id'] == employee_id:
            attendance_list.remove(rec)
            print(f"{GREEN}✅ Record deleted.{END}")
            return
    print(f"{RED}❌ Employee not found.{END}")

def menu():
    while True:
        print(f"\n{BOLD}{CYAN}{'='*10} Employee Attendance System {'='*10}{END}")
        print(f"{BOLD}1. Create 🎫")
        print("2. View Records 📋")
        print("3. Update Record 🔄")
        print("4. Delete Record 🗑️")
        print("5. Exit 🚪\n" + END)
        choice = input("Enter choice (1-5): ")
        if choice == '1': create_attendance()
        elif choice == '2': read_attendance()
        elif choice == '3': update_attendance()
        elif choice == '4': delete_attendance()
        elif choice == '5':
            print(f"{GREEN}👋 Thank you for using Employee Attendance System!{END}")
            break
        else:
            print(f"{RED}❌ Invalid choice.{END}")

if __name__ == "__main__":
    menu()
