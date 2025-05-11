from django.urls import path
from .views import *

urlpatterns = [
    path('',mainpage,name='main'),
    path('all/',Studnet_List,name = 'allstu'),
    path('login/stu',Login_Student,name = 'loginstu'),
    path('signin/stu',signinstu,name = 'signinstu'),
    path('logout/stu',Logout_Student,name = 'logoutstu'),
    path('signin/tea',signintea,name = 'signintea'),
    path('login/tea',Login_Teacher,name = 'logintea'),
    path('logout/tea',Logout_Teacher,name = 'logouttea'),
    path('lessonstu/',dashboardstu,name = 'lessonstu'),
    path('lessontea/',dashboardtea,name = 'leessontea'),
    path('maindashtea/',maindashboardtea,name = 'maindashboardtea'),
    path('maindashstu/',maindashboardstu,name = 'maindashboardstu'),
    path('detaillesson/<str:pk>/',detaillesson,name='detail'),
    path('detaillesson_stu/<str:pk>/',detaillesson_stu,name='detail_stu'),
    path('editexam/<str:pk>/',edit_exam,name='edit'),
    path('newquestoin/<str:pk>/',writeq,name='nq'),
    path('addquestion/<str:pk>/',W_E_question,name='aq'),
    path('makeexex/<str:pk>/',selectmakeexam,name = 'makeexam'),
    path('stufortea/',student_for_tea,name = 'studentforteacher'),
    path('student_detail/<str:pk>/',student_detail,name='stu_det'),
    path('exam/<str:pk>/<str:pp>/<str:tt>/',startexam,name = 'examexam'),
    path('showansware/<str:pk>/<str:lk>/',showansware,name = 'showanswarean'),
    path('setmark/<str:pk>/<str:pn>/',addgrade,name = 'setmarkstu')

    

]
