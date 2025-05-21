import unittest
from main_m10 import Student, DeclaredStudent

class TestStudent(unittest.TestCase):
    def setUp(self):
        """Set up a student object for testing"""
        self.student = Student("John", "Doe")
    
    def test_initialization(self):
        """Test that the Student object is initialized correctly"""
        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.last_name, "Doe")
        self.assertEqual(self.student.grade_point, 0)
        self.assertEqual(self.student.credits, 0)
        self.assertEqual(self.student.gpa, 0.0)
    
    def test_calculate_gpa_single_course(self):
        """Test GPA calculation with a single course"""
        self.student.CalculateGPA("A", 3.0)
        self.assertEqual(self.student.credits, 3.0)
        self.assertEqual(self.student.grade_point, 12.0)  # 3.0 credits * 4.0 (A grade)
        self.assertEqual(self.student.gpa, 4.0)  # 12.0 / 3.0
    
    def test_calculate_gpa_multiple_courses(self):
        """Test GPA calculation with multiple courses"""
        self.student.CalculateGPA("A", 3.0)  # 3.0 credits * 4.0 = 12.0 points
        self.student.CalculateGPA("B", 3.0)  # 3.0 credits * 3.0 = 9.0 points
        self.student.CalculateGPA("C", 4.0)  # 4.0 credits * 2.0 = 8.0 points
        
        # Total: 10.0 credits, 29.0 grade points, GPA = 29.0 / 10.0 = 2.9
        self.assertEqual(self.student.credits, 10.0)
        self.assertEqual(self.student.grade_point, 29.0)
        self.assertEqual(self.student.gpa, 2.9)
    
    def test_calculate_gpa_invalid_grade(self):
        """Test GPA calculation with an invalid grade"""
        # Initial values
        initial_credits = self.student.credits
        initial_grade_point = self.student.grade_point
        initial_gpa = self.student.gpa
        
        # This should not change any values
        self.student.CalculateGPA("X", 3.0)
        
        # Values should remain unchanged
        self.assertEqual(self.student.credits, initial_credits)
        self.assertEqual(self.student.grade_point, initial_grade_point)
        self.assertEqual(self.student.gpa, initial_gpa)
    
    def test_get_gpa(self):
        """Test the GetGPA method"""
        self.assertEqual(self.student.GetGPA(), 0.0)
        
        self.student.CalculateGPA("B", 3.0)
        self.assertEqual(self.student.GetGPA(), 3.0)


class TestDeclaredStudent(unittest.TestCase):
    def setUp(self):
        """Set up a declared student object for testing"""
        self.student_with_concentration = DeclaredStudent("Jane", "Smith", "Computer Science")
        self.student_without_concentration = DeclaredStudent("Bob", "Johnson", "")
    
    def test_initialization(self):
        """Test that the DeclaredStudent object is initialized correctly"""
        # Test student with concentration
        self.assertEqual(self.student_with_concentration.first_name, "Jane")
        self.assertEqual(self.student_with_concentration.last_name, "Smith")
        self.assertEqual(self.student_with_concentration.concentration, "Computer Science")
        self.assertEqual(self.student_with_concentration.grade_point, 0)
        self.assertEqual(self.student_with_concentration.credits, 0)
        self.assertEqual(self.student_with_concentration.gpa, 0.0)
        
        # Test student without concentration
        self.assertEqual(self.student_without_concentration.first_name, "Bob")
        self.assertEqual(self.student_without_concentration.last_name, "Johnson")
        self.assertEqual(self.student_without_concentration.concentration, "")
    
    def test_get_concentration(self):
        """Test the GetConcentration method"""
        self.assertEqual(self.student_with_concentration.GetConcentration(), "Computer Science")
        self.assertEqual(self.student_without_concentration.GetConcentration(), "NA")
    
    def test_get_year_freshman(self):
        """Test GetYear method for a freshman student (0-33 credits)"""
        self.student_with_concentration.CalculateGPA("A", 15.0)
        self.student_with_concentration.CalculateGPA("B", 15.0)
        # Total credits: 30.0
        self.assertEqual(self.student_with_concentration.GetYear(), "Freshman")
    
    def test_get_year_sophomore(self):
        """Test GetYear method for a sophomore student (34-66 credits)"""
        self.student_with_concentration.CalculateGPA("A", 34.0)
        self.student_with_concentration.CalculateGPA("B", 15.0)
        # Total credits: 49.0
        self.assertEqual(self.student_with_concentration.GetYear(), "Sophomore")
    
    def test_get_year_junior(self):
        """Test GetYear method for a junior student (67-96 credits)"""
        self.student_with_concentration.CalculateGPA("A", 67.0)
        self.student_with_concentration.CalculateGPA("B", 15.0)
        # Total credits: 82.0
        self.assertEqual(self.student_with_concentration.GetYear(), "Junior")
    
    def test_get_year_senior(self):
        """Test GetYear method for a senior student (97-130 credits)"""
        self.student_with_concentration.CalculateGPA("A", 97.0)
        self.student_with_concentration.CalculateGPA("B", 15.0)
        # Total credits: 112.0
        self.assertEqual(self.student_with_concentration.GetYear(), "Senior")
    
    def test_get_year_multiyear(self):
        """Test GetYear method for a multiyear student (>130 credits)"""
        self.student_with_concentration.CalculateGPA("A", 131.0)
        # Total credits: 131.0
        self.assertEqual(self.student_with_concentration.GetYear(), "Multi-year Student")
    
    def test_inheritance(self):
        """Test that DeclaredStudent inherits methods from Student"""
        self.student_with_concentration.CalculateGPA("A", 3.0)
        self.assertEqual(self.student_with_concentration.GetGPA(), 4.0)
        

if __name__ == '__main__':
    unittest.main()