import unittest
from main_m9 import Student

class TestStudent(unittest.TestCase):
    def test_init(self):
        """Test the initialization of Student objects"""
        student = Student("John", "Doe")
        self.assertEqual(student.first_name, "John")
        self.assertEqual(student.last_name, "Doe")
        self.assertEqual(student.grade_point, 0)
        self.assertEqual(student.credits, 0)
        self.assertEqual(student.gpa, 0.0)

    def test_gpa_calculation_single_course(self):
        """Test GPA calculation with a single course"""
        student = Student("Jane", "Smith")
        student.CalculateGPA('A', 3)
        self.assertEqual(student.credits, 3)
        self.assertEqual(student.grade_point, 12)  # A = 4.0 * 3 credits = 12
        self.assertEqual(student.GetGPA(), 4.0)

    def test_gpa_calculation_multiple_courses(self):
        """Test cumulative GPA calculation with multiple courses"""
        student = Student("Bob", "Johnson")
        student.CalculateGPA('A', 3)  # 3 credits, 12 grade points
        student.CalculateGPA('B', 4)  # 4 credits, 12 grade points
        student.CalculateGPA('C', 2)  # 2 credits, 4 grade points
        
        expected_credits = 9
        expected_grade_points = 28  # 12 + 12 + 4
        expected_gpa = expected_grade_points / expected_credits  # 28/9 = 3.11...
        
        self.assertEqual(student.credits, expected_credits)
        self.assertEqual(student.grade_point, expected_grade_points)
        self.assertAlmostEqual(student.GetGPA(), expected_gpa)

    def test_invalid_grade(self):
        """Test handling of invalid grade input"""
        student = Student("Alice", "Brown")
        
        # Store initial values
        initial_credits = student.credits
        initial_grade_points = student.grade_point
        
        # Try with invalid grade
        student.CalculateGPA('X', 3)
        
        # Values should not change
        self.assertEqual(student.credits, initial_credits)
        self.assertEqual(student.grade_point, initial_grade_points)


if __name__ == "__main__":
    unittest.main()