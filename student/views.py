from django.shortcuts import render,redirect
from .models import Student,Lesson,Teacher,Question,Answare,Grade
from .forms import StuAuthenticationForm,TeacherAuthenticationForm,MakeExam,Writeq_e,AnswareExam,Gradestu,signin_tea,signin_stu
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.forms import modelformset_factory


# Create your views here.

def mainpage(request):
    if 'stu_id' in request.session:
        return render(request,'dashboardstu.html')
    elif 'tea_id' in request.session:
        return render(request,'dashboardtea.html')
    else:
        return render(request,'index.html')



def Studnet_List(request):
    if 'stu_id' in request.session:
        x=Student.objects.all()
        context={'x':x}
        return render(request,'stu_list.html',context)
    else:
        return HttpResponse('not login')

@csrf_exempt
def Login_Student(request):
    if request.method == 'GET':
        f_form = StuAuthenticationForm()
        return render(request, 'login_stu.html', {'form': f_form})
    
    elif request.method == 'POST':
        f_form = StuAuthenticationForm(request.POST)
        if f_form.is_valid():
            national_id = f_form.cleaned_data['national_id']
            stu_number = f_form.cleaned_data['stu_number']

            try:
                student = Student.objects.get(national_id=national_id, stu_number=stu_number)
                print(student)
                context={'name':student.name}

                request.session['stu_id'] = student.id
                print(student.id) 
                return render(request,'dashboardstu.html',context) 
            except Student.DoesNotExist:
                f_form.add_error(None, 'اطلاعات وارد شده اشتباه است')

        return render(request, 'login_stu.html', {'form': f_form})


def Logout_Student(request):
    stu_id = request.session.get('stu_id')
    if stu_id:
        logout(request)
        return render(request,'index.html')
    else:
        return HttpResponse('you are not login')
    


@csrf_exempt
def signinstu(request):
    if request.method == 'GET':
        form = signin_stu()
        context = {'form':form}
        return render(request,'singin_stu.html',context)
    elif request.method == 'POST':
        form = signin_stu(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            return HttpResponse('sign in not valid')

    else:
        return HttpResponse('your method isnt get or post')


#show lessons for a stu
def dashboardstu(request):
    list1=[]
    if 'stu_id' in request.session:
        x = request.session['stu_id']
        temp_temp = Student.objects.get(id = x)
        for m in temp_temp.lesson_list.all():
            place = Lesson.objects.get(lesson_id = m)
            list1.append(place.name)
            
        context = {'stu_id':list1}
        print(list1)
        return render(request,'lessonstu.html',context)
    else:
        return HttpResponse('not login')

#maindashboard student
def maindashboardstu(request):
    if 'stu_id' in request.session:
        return render(request,'dashboardstu.html')
    else:
        return HttpResponse('you are not login')

def detaillesson_stu(request, pk):
    if 'stu_id' in request.session:
        y = request.session['stu_id']
        temp_temp_temp = Student.objects.get(id=y)
        temp = Lesson.objects.get(name=pk)

        try:
            GradeGrade = Grade.objects.get(stu=temp_temp_temp, lesson_name=pk)
        except Grade.DoesNotExist:
            GradeGrade = None

        context = {'lesson_d': temp, 'stu': temp_temp_temp, 'G': GradeGrade}
        return render(request, 'detaillesson_stu.html', context)
    else:
        return HttpResponse('you are not login')

# @csrf_exempt
# def startexam(request,pk):
#     lesson_num = Lesson.objects.get(name = pk)
#     q_forexam = Question.objects.filter(lesson_l = lesson_num)
#     if request.method == 'GET':
#         form = AnswareExam()
#         context={'q':q_forexam,'form':form}
#         return render(request,'exam.html',context) 
#     elif request.method == 'POST':
#         form = AnswareExam(request.POST)
#         if form.is_valid():
#             return HttpResponse("ok and save")
#         else:
#             return HttpResponse("this form isnt valid")
#     else:
#         return HttpResponse('this method not post or get')
@csrf_exempt
def startexam(request, pk, pp, tt):
    if 'stu_id' in request.session:
        y = request.session['stu_id']
        tempstu = Student.objects.get(id=y)
        print(tempstu)
        print(pk)
        mm = Answare.objects.filter(studnet_number=tempstu,lesson_l_l=pk)
        print(mm)
        if mm.exists():
            return HttpResponse('شما یکبار امتحان دادی')
        else:
            lesson_obj = Lesson.objects.get(name=pk)
            questions = Question.objects.filter(lesson_l=lesson_obj)

            if request.method == 'POST':
                for question in questions:
                    answer_text = request.POST.get(f'answer_{question.q_id}')
                    if answer_text:
                        Answare.objects.create(
                            text_an=answer_text,
                            q_number=question.q_id,
                            lesson_l_l=lesson_obj.name,
                            studnet_number=pp
                        )
                return redirect('detail_stu',pk=pk)

            else:
                context = {
                    'questions': questions,
                    'lesson': pk,
                    'student_number': pp,
                    'time_limit': int(tt)  
                }
                return render(request, 'exam.html', context)
    else:
        return HttpResponse('you are not login')
#teacher do this work
def showansware(request,pk,lk):
    x = Answare.objects.filter(studnet_number = pk,lesson_l_l = lk)
    
    if x:
        z = Lesson.objects.get(name = lk)
        y = Question.objects.filter(lesson_l = z)
        return render(request,'answarestu.html',context={'x':x,'y':y,'lesson':lk,'stu':pk})

    else:
        return HttpResponse('nothing')
    # for z in range(1):
    #     y = Question.objects.get(lesson_l = x[z].lesson_l_l)

# teacher do this work   
def addgrade(request,pk,pn):
    
    if request.method == 'GET':
        form = Gradestu()
        return render(request,'grade.html',context={'form':form})
    elif request.method == 'POST':
        form = Gradestu(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stu_det',pk=pn)
        else:
            return HttpResponse('isnt valid')
    else:
        return HttpResponse('bad method')
        

# def addgrade(request,pk,pn):
    
#     if request.method == 'GET':
#         form = Gradestu()
#         return render(request,'grade.html',context={'form':form})
#     elif request.method == 'POST':
#         form = Gradestu(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('stu_det',pk=pn)
#         else:
#             return HttpResponse('isnt valid')
#     else:
#         return HttpResponse('bad method')

@csrf_exempt
def addgrade(request, pk, pn):
    student = Student.objects.get(stu_number=pk)  # گرفتن دانش‌آموز با id

    if request.method == 'GET':
        form = Gradestu()
        return render(request, 'grade.html', {'form': form})

    elif request.method == 'POST':
        form = Gradestu(request.POST)
        if form.is_valid():
            grade_obj = form.save(commit=False)  # ذخیره موقت
            grade_obj.stu = student
            grade_obj.lesson_name = pn  # چون pn اسم درسه
            grade_obj.save()
            return redirect('stu_det', pk=pn)
        else:
            return HttpResponse('isnt valid')

    else:
        return HttpResponse('bad method')



@csrf_exempt
def Login_Teacher(request):
    if request.method == 'GET':
        f_form = TeacherAuthenticationForm()
        return render(request, 'login_tea.html', {'form': f_form})
    
    elif request.method == 'POST':
        f_form = TeacherAuthenticationForm(request.POST)
        if f_form.is_valid():
            national_id = f_form.cleaned_data['national_id']
            tea_number = f_form.cleaned_data['tea_number']

            try:
                teacher = Teacher.objects.get(national_id=national_id, tea_number=tea_number)
                print(teacher)

                request.session['tea_id'] = teacher.id
                print(teacher.id)  
                return render(request,'dashboardtea.html') 
            except Teacher.DoesNotExist:
                f_form.add_error(None, 'اطلاعات وارد شده اشتباه است')

        return render(request, 'login_tea.html', {'form': f_form})


def Logout_Teacher(request):
    tea_id = request.session.get('tea_id')
    if tea_id:
        logout(request)
        return render(request,'index.html')
    else:
        return HttpResponse('you are not login')

@csrf_exempt
def signintea(request):
    if request.method == 'GET':
        form = signin_tea()
        context = {'form':form}
        return render(request,'singin_tea.html',context)
    elif request.method == 'POST':
        form = signin_tea(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            return HttpResponse('sign in not valid')

    else:
        return HttpResponse('your method isnt get or post')




#show lessons for a tea
def dashboardtea(request):
    list1=[]
    if 'tea_id' in request.session:
        x = request.session['tea_id']
        temp_temp = Teacher.objects.get(id = x)
        for m in temp_temp.lesson_list.all():
            place = Lesson.objects.get(lesson_id = m)
            list1.append(place.name)
            
        context = {'tea_id':list1}
        
        return render(request,'lessontea.html',context)
    else:
        return HttpResponse('not login')
    


#maindashboard teacher
def maindashboardtea(request):
    tea_id = request.session.get('tea_id')
    if tea_id:
        return render(request,'dashboardtea.html')
    else:
        return HttpResponse('you are not login teacher')

def detaillesson(request,pk):
    temp = Lesson.objects.get(name = pk)
    if temp:
        context = {'lesson_d':temp}
        return render(request,'detaillesson.html',context)
    else:
        return HttpResponse("dont have this lesson.")
    


def edit_exam(request, pk):
    try:
        t_temp = Lesson.objects.get(name=pk)  
    except Lesson.DoesNotExist:
        return HttpResponse("رکوردی با این مشخصات پیدا نشد.")

    if request.method == "POST":
        form = MakeExam(request.POST, instance=t_temp)
        if form.is_valid():
            form.save()
            return redirect('detail',pk=pk)
    else:
        form = MakeExam(instance=t_temp)

    context = {'form': form}
    return render(request, 'changelesson.html', context)

# def W_E_question(request,pk):
#     x = Lesson.objects.get(name = pk)
#     try:
#         t_t_temp = Question.objects.get(lesson_l = x)
#     except Question.DoesNotExist:
#         return render(request,'dontfindq.html')
#     if request.method == "POST":
#         form = Writeq_e(request.POST , instance=t_t_temp)
#         if form.is_valid():
#             form.save()
#             return redirect('detail',pk=pk)
#     else:
#         form = Writeq_e(instance=t_t_temp)
#         context={'form':form}
#         return render(request,'writeq.html',context)
def W_E_question(request, pk):
    lesson = Lesson.objects.get(name=pk)
    QuestionFormSet = modelformset_factory(Question, form=Writeq_e, extra=0)
    queryset = Question.objects.filter(lesson_l=lesson)

    if not queryset.exists():
        return render(request, 'dontfindq.html')

    if request.method == "POST":
        formset = QuestionFormSet(request.POST, queryset=queryset)
        if formset.is_valid():
            formset.save()
            return redirect('detail', pk=pk)
    else:
        formset = QuestionFormSet(queryset=queryset)

    return render(request, 'writeq.html', {'formset': formset})


def writeq(request,pk):
    x = Lesson.objects.get(name = pk)
    if x:
        if request.method == 'GET':
            form = Writeq_e()
            context = {'form':form}
            return render(request,'writequestion.html',context)
        elif request.method == 'POST':
            form = Writeq_e(request.POST)
            if form.is_valid():
                form.save()
                return redirect('aq',pk=pk)
            else:
                return HttpResponse('no its not valid')
        else:
            return HttpResponse("nothing")
        


def selectmakeexam(request,pk):
    lesson = Lesson.objects.get(name=pk)
    QuestionFormSet = modelformset_factory(Question, form=Writeq_e, extra=0)
    queryset = Question.objects.filter(lesson_l=lesson)
    

    if queryset:
        return redirect('aq',pk=lesson.name)
    else:
        return redirect('nq',pk=lesson.name)
    

#show student for teacher (lesson)
def student_for_tea(request):
    list1=[]
    if 'tea_id' in request.session:
        x = request.session['tea_id']
        temp_one = Teacher.objects.get(id = x)
        for m in temp_one.lesson_list.all():
            place = Lesson.objects.get(lesson_id = m)
            list1.append(place.name)

        context = {'tea_id':list1}
        return render(request,'teacher_students.html',context)

    else:
        return HttpResponse('not login')
    
#show student for teacher (person)
def student_detail(request,pk):
    temp = Lesson.objects.get(name = pk)
    print(temp)
    x = Student.objects.filter(lesson_list = temp)
    print(x)

    # y = Answare.objects.filter(studnet_number = x)
    
    if x :
        context = {'x':x,'lesson':pk}
        return render(request,'student_detail.html',context)
    else:
        return HttpResponse('dont have student')


    