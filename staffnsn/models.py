from django.db import models
from  studentnsn.models import Academics, PersonalInformation
class StudentsAttendance(models.Model):
    class CurrentSemester(models.TextChoices):
        SEM1 = '1', '1'
        SEM2 = '2', '2'
        SEM3 = '3', '3'
        SEM4 = '4', '4'
        SEM5 = '5', '5'
        SEM6 = '6', '6'
        SEM7 = '7', '7'
        SEM8 = '8', '8'
        SEM9 = '9', '9'
        SEM10 = '10', '10'
    roll_number = models.BigIntegerField()
    semester = models.CharField(max_length=2, choices=CurrentSemester.choices,default=CurrentSemester.SEM1 )
    staff_name = models.TextField()
    Course_Code = models.TextField()
    Course_Name = models.CharField(max_length=100)
    Date_Attended = models.DateField()
    From_Time = models.TimeField()
    To_Time = models.TimeField()
    No_of_Hours = models.SmallIntegerField()
    Is_Present = models.BooleanField(default=False)  

class AttendancePercentage(models.Model): 
    roll_number = models.BigIntegerField()
    Semester = models.IntegerField()
    Course_Code = models.TextField(null=True, blank=True)  # Null for full course calculation
    Attendance_Percentage = models.FloatField()