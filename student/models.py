from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    lesson_id = models.CharField(max_length=5)
    exam_date = models.DateField()
    exam_time = models.TimeField()
    ex_time = models.CharField(max_length=100,null=True)
    num_q = models.CharField(max_length=10,null=True)


    def __str__(self):
        return self.lesson_id
    




class Student(models.Model):
    national_id = models.CharField(max_length=10)
    stu_number = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    lesson_list = models.ManyToManyField(Lesson)



    def __str__(self):
        return self.stu_number
    

class Teacher(models.Model):
    national_id = models.CharField(max_length=10)
    tea_number = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    lesson_list = models.ManyToManyField(Lesson)

    def __str__(self):
        return self.tea_number
    



class Exam(models.Model):
    exam_name = models.OneToOneField(Lesson,on_delete=models.CASCADE)
    ex_time = models.CharField(max_length=100)
    num_q = models.CharField(max_length=10,null=True)




    def __str__(self):
        return self.exam_name.name
    


class Question(models.Model):
    q_id = models.CharField(max_length=4)
    text_q = models.TextField()
    q_grade = models.CharField(max_length= 20)
    lesson_l = models.ForeignKey(Lesson,on_delete=models.CASCADE)

    
    def __str__(self):
        x = str(self.lesson_l) + '-'+ str(self.q_id)
        return x

# class Grade(models.Model):
#     stu_grade_n = models.ForeignKey(Student,on_delete=models.CASCADE)
#     lesson_name = models.OneToOneField(Student,on_delete=models.CASCADE)
#     grade = models.CharField(max_length=4)


#     def __str__(self):
#         x = str(self.stu_grade_n) + '-' + str(self.lesson_name)
#         return x
    
class Answare(models.Model):
    text_an = models.TextField()
    q_number = models.CharField(max_length=20)
    lesson_l_l = models.CharField(max_length=30)
    studnet_number = models.CharField(max_length=8)

    def __str__(self):
        x = 'lesson_name:'+str(self.lesson_l_l)+ 'question_id :' +str(self.q_number)+ 'stunumber: ' +str(self.studnet_number)
        return x


class Grade(models.Model):
    stu = models.ForeignKey(Student,on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=200)
    grade = models.FloatField()

    def __str__(self):
        x ='stuname : '+str(self.stu)+'lesson name :'+str(self.lesson_name)
        return x


