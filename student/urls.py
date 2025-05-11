from django.urls import path
from .views import *

urlpatterns = [
    path('',mainpage,name='main'),
    path('all/',Studnet_List),
    path('login/stu',Login_Student),
    path('signin/stu',signinstu),
    path('logout/stu',Logout_Student),
    path('signin/tea',signintea),
    path('login/tea',Login_Teacher),
    path('logout/tea',Logout_Teacher),
    path('lessonstu/',dashboardstu),
    path('lessontea/',dashboardtea),
    path('maindashtea/',maindashboardtea),
    path('maindashstu/',maindashboardstu),
    path('detaillesson/<str:pk>/',detaillesson,name='detail'),
    path('detaillesson_stu/<str:pk>/',detaillesson_stu,name='detail_stu'),
    path('editexam/<str:pk>/',edit_exam,name='edit'),
    path('newquestoin/<str:pk>/',writeq,name='nq'),
    path('addquestion/<str:pk>/',W_E_question,name='aq'),
    path('makeexex/<str:pk>/',selectmakeexam),
    path('stufortea/',student_for_tea),
    path('student_detail/<str:pk>/',student_detail,name='stu_det'),
    path('exam/<str:pk>/<str:pp>/<str:tt>/',startexam),
    path('showansware/<str:pk>/<str:lk>/',showansware),
    path('setmark/<str:pk>/<str:pn>/',addgrade)

    

]
