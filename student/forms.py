from django import forms
from .models import Question,Exam,Lesson,Answare,Grade,Student,Teacher

class StuAuthenticationForm(forms.Form):
    national_id = forms.CharField(max_length=10, label="کد ملی")
    stu_number = forms.CharField(max_length=8, label="شماره دانش‌آموزی")

class TeacherAuthenticationForm(forms.Form):
    national_id = forms.CharField(max_length=10 , label="کد ملی")
    tea_number = forms.CharField(max_length=8 , label="شماره استادی")

class Writeq_e(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['q_id','text_q','q_grade','lesson_l']
        labels = {
            'q_id':'کد سوال',
            'text_q':'متن سوال',
            'q_grade':'بارم سوال',
            'lesson_l':'نام درس'
        }

class MakeExam(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['name','lesson_id','exam_date','exam_time','ex_time','num_q']
        labels = {
            'name': 'نام درس',
            'lesson_id': 'شناسه درس',
            'exam_date': 'تاریخ آزمون',
            'exam_time': 'ساعت شروع آزمون',
            'ex_time':'مدت زمان آزمون',
            'num_q':'تعداد سوالات'
        }

class AnswareExam(forms.ModelForm):
    class Meta:
        model = Answare
        fields = ['text_an']
        labels ={
            'text_an':'پاسخ',
            
        }

class Gradestu(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['grade']
        labels = {
            'grade': 'نمره'
        }


class signin_stu(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['national_id','stu_number','name','family','lesson_list']
        labels ={
            'national_id':'کد ملی',
            'stu_number':'شماره دانش آموزی',
            'name':'نام',
            'family':'نام خانوادگی',
            'lesson_list':'دروس'
        }




class signin_tea(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['national_id','tea_number','name','family','lesson_list']
        labels ={
            'national_id':'کد ملی',
            'tea_number':'شماره استادی ',
            'name':'نام',
            'family':'نام خانوادگی',
            'lesson_list':'دروس'
        }