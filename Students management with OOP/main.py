
print("\n\n-------------Students Management System------------- ")

class Student:
    def __init__(self, name, roll, cls):
        self.name = name 
        self.roll = roll
        self.cls = cls

    def show(self):
        print(f"Roll: {self.roll}, Name: {self.name}, Class: {self.cls}")


class StudentManager:
    def __init__(self):
        self.students = []
        self.load_from_file()


    def load_from_file(self):
        try:
            with open ("A_students.txt", "r") as f:
                for line in f:
                    name, roll, cls = line.strip().split(", ")
                    self.students.append(Student(name, int(roll), int(cls)))
        except FileNotFoundError:
            print("File not found !!")


    def save_to_file(self):
        with open("A_students.txt", "w") as f:
            for i in self.students:
                f.write(f"{i.name}, {i.roll}, {i.cls}\n")
                

    def add_student(self):
        while True:
            try:
                name = input("Enter name: ")
                break
            except KeyboardInterrupt:
                print("\nPLease try agian")
                continue
        while True:
            try:
                roll = int(input("Enter roll: "))
                break
            except KeyboardInterrupt:
                print("\nPLease try agian")
                continue
            except Exception:
                print("Please enter a valid roll number")
                continue
        while True:
            try:
                cls = int(input("Enter class: "))
                if cls<=0 or cls>=13:
                    print("Please enter a valid class (1-12)")
                    continue
                else:
                    break
            except KeyboardInterrupt:
                print("\nPLease try agian")
                continue
            except Exception:
                print("Please enter a valid class")
                continue
        for i in self.students:
            if i.roll==roll:
                print(f"\nThere is already a student with the roll number {roll}..... So we can't save this data !!")
                return
        s = Student(name, roll, cls)    
        self.students.append(s)
        print("\nStudent added successfully")
        self.save_to_file()


    def view_student(self):
        if self.students == []:
            print("No student found !!")
            return      
        for i in self.students:
            i.show()

    
    def search_student(self):
        while True:
            try:
                user = int(input("\nEnter the roll number of the student: "))
                break
            except KeyboardInterrupt:
                print("\n\nPlease re-enter the roll number.......\n")
                continue
            except Exception:
                print("\nPlease enter a valid roll number.....")
        for i in self.students:
            if i.roll == user:
                print(f"\nThe student of roll number {user} is {i.name} from class {i.cls}")
                return
        print("\nStudent not found !!")


    def delete_student(self):
        while True:
            try:
                user = int(input("\nEnter the roll number of the student which you want to delete: "))
                break
            except KeyboardInterrupt:
                print("\n\nPlease re-enter the rol number........")
                continue
            except Exception:
                print("\nPlease enter a valid roll number.......")
                continue
        found = False
        updated_students = []
        for i in self.students:
            if i.roll!=user:
                updated_students.append(i)
            else:
                found=True
        if found:
            self.students = updated_students
            print("\nDeletion completed....")
        elif found==False:
            print("\nNo student found !!")
        self.save_to_file()

    
    def update_student(self):
        while True:
            try:
                user = int(input("\nEnter the roll number of the student which you want to update: "))
                break
            except KeyboardInterrupt:
                print("\n\nPlease re-enter the rol number........")
                continue
            except Exception:
                print("\nPlease enter a valid roll number.......")
        student_to_update = None
        for i in self.students:
            if i.roll == user:
                student_to_update = i
                break
        if student_to_update:
            print(f"\nCurrent name of the roll number {user} is {student_to_update.name}")
            while True:
                try:
                    new_name = input("What name you want to rename with: ")
                    break
                except KeyboardInterrupt:
                    print("\n\nPlease re-enter your choice")
                    continue
            student_to_update.name = new_name
            print("\nRenaming completed !!")
            print(f"\n\nCurrent class of the roll number {user} is {student_to_update.cls}")
            while True:
                try:
                    new_class = int(input("What class you want to reset with: : "))
                    if new_class<=0 or new_class>=13:
                        print("Please enter a valid class (1-12)")
                        continue
                    else:
                        break
                except KeyboardInterrupt:
                    print("\n\nPlease re-enter the rol number........")
                    continue
                except Exception:
                    print("\nPlease enter a valid class.......")
                    continue
            student_to_update.cls = new_class
            print("\nClass updated !!")
            self.save_to_file()
        else:
            print(f"\nThere is no student with roll number {user}")


manager = StudentManager()



def menu():
    while True:
        try:
            choice = int(input("\nSelect one--\n1. Add student\n2. View student\n3. Search student\n4. Update student\n5.Exit\n\nyour choice - "))
            if choice<=0 or choice>=6:
                print("\nPlease enter a valid choice (1-5)")
                continue
        except KeyboardInterrupt:
            print("\nPlease try again !!")
            continue
        except Exception:
            print("\nPlease enter a valid number (1-5)\n")
            continue

        if choice==1:
            manager.add_student()
            input("Press enter to go to menu........")
        elif choice==2:
            manager.view_student()
            input("Press enter to go to menu........")
        elif choice==3:
            manager.search_student()
            input("Press enter to go to menu........")
        elif choice==4:
            manager.update_student()
            input("Press enter to go to menu........")
        elif choice==5:
            print("\n\nProgram closing...........\n")
            break
        
menu()

    









