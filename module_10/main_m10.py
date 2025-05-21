class Student:
    def __init__(self, first_name, last_name):
        """
        Initialize a Student object with first name and last name.
        Grade points and credits are initialized to zero.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.grade_point = 0
        self.credits = 0
        self.gpa = 0.0

    def CalculateGPA(self, course_grade, course_credits):
        """
        Calculate the cumulative GPA based on the new course grade and credits.
        
        Args:
            course_grade (str): Letter grade for the course (A, B, C, D, F)
            course_credits (float): Number of credits for the course
        """
        # Convert letter grade to grade points
        grade_point_map = {
            'A': 4.0,
            'B': 3.0,
            'C': 2.0,
            'D': 1.0,
            'F': 0.0
        }
        
        # Get grade points for the course
        if course_grade in grade_point_map:
            course_grade_points = grade_point_map[course_grade] * course_credits
            
            # Update total grade points and credits
            self.grade_point += course_grade_points
            self.credits += course_credits
            
            # Calculate new GPA if credits are not zero
            if self.credits > 0:
                self.gpa = self.grade_point / self.credits
        else:
            print(f"Invalid grade '{course_grade}'. Please use A, B, C, D, or F.")

    def GetGPA(self):
        """
        Return the current cumulative GPA.
        
        Returns:
            float: The student's current GPA
        """
        return self.gpa


class DeclaredStudent(Student):
    def __init__(self, first_name, last_name, concentration=""):
        """
        Initialize a DeclaredStudent object with first name, last name, and concentration.
        Inherits from the Student class.
        
        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            concentration (str): Student's declared concentration
        """
        # Call the parent class constructor
        super().__init__(first_name, last_name)
        self.concentration = concentration
    
    def GetConcentration(self):
        """
        Return the student's concentration.
        
        Returns:
            str: The student's concentration or "NA" if not declared
        """
        if not self.concentration:
            return "NA"
        return self.concentration
    
    def GetYear(self):
        """
        Determine the student's year based on cumulative credits.
        
        Returns:
            str: The student's classification (Freshman, Sophomore, Junior, Senior, or Multi-year)
        """
        if self.credits <= 33:
            return "Freshman"
        elif self.credits <= 66:
            return "Sophomore"
        elif self.credits <= 96:
            return "Junior"
        elif self.credits <= 130:
            return "Senior"
        else:
            return "Multi-year Student"


def main():
    # Prompt for student information
    first_name = ""
    while not first_name:
        first_name = input("Enter student's first name: ").strip()
        if not first_name:
            print("First name is required. Please try again.")
    
    last_name = ""
    while not last_name:
        last_name = input("Enter student's last name: ").strip()
        if not last_name:
            print("Last name is required. Please try again.")

    concentration = input("Enter student's concentration (or leave blank if undeclared): ")
    
    # Create a Declared Student 
    student = DeclaredStudent(first_name, last_name, concentration)
    
    # Loop to input courses
    while True:
        # Ask if user wants to add a course
        while True:
            add_course = input("\nAdd a course? (Y/N): ").strip().upper()
            if add_course in ['Y', 'N']:
                break
            else:
                print("Invalid input. Please enter Y or N.")
                
        if add_course != 'Y':
            break
        
        # Get course details
        try:
            # Validate course credits
            while True:
                credit_input = input("Enter course credits: ").strip()
                if credit_input:
                    try:
                        course_credits = float(credit_input)
                        if course_credits > 0:
                            break
                        else:
                            print("Credits must be greater than 0.")
                    except ValueError:
                        print("Invalid input. Credits must be a number.")
                else:
                    print("Course credits are required. Please try again.")
            
            # Validate course grade
            while True:
                course_grade = input("Enter course grade (A, B, C, D, F): ").strip().upper()
                if course_grade in ['A', 'B', 'C', 'D', 'F']:
                    break
                else:
                    print("Invalid grade. Please enter A, B, C, D, or F.")
        
        except ValueError:
            print("An error occurred. Please try again.")
    
    
    # Display results
    print("\nStudent Information:")
    print(f"Name: {student.first_name} {student.last_name}")
    print(f"Concentration: {student.GetConcentration()}")
    print(f"Total Credits: {student.credits}")
    print(f"Cumulative GPA: {student.GetGPA():.2f}")
    print(f"Year: {student.GetYear()}")


# Run the main program
if __name__ == "__main__":
    main()