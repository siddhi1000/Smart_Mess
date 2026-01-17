from django.test import TestCase
from apps.attendance.models import Attendance
from apps.users.models import User

class AttendanceModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@college.edu',
            password='testpassword'
        )
        self.attendance = Attendance.objects.create(
            user=self.user,
            date='2024-01-01',
            status='present'
        )

    def test_attendance_creation(self):
        self.assertEqual(self.attendance.user, self.user)
        self.assertEqual(self.attendance.date, '2024-01-01')
        self.assertEqual(self.attendance.status, 'present')

    def test_attendance_str(self):
        self.assertEqual(str(self.attendance), f'{self.user.email} - {self.attendance.date}')

    def test_attendance_status(self):
        self.attendance.status = 'absent'
        self.attendance.save()
        self.assertEqual(self.attendance.status, 'absent')