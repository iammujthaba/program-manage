"""Mainproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Bzone import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login1/', views.login1),
    path('logout/', views.logout),
    path('login_POST/', views.login_post),

    #path('allocation/',views.allocation),
#---(1)----
    path('college_registration/', views.college_registration),
    path('Edit_college_registration/<id>', views.Edit_college_registration),
    path('edit_college_post/', views.edit_college_post),
    path('view_college_registration/', views.view_college_registration),
    path('college_registrationpost/', views.college_registrationpost),
    path("delete_college_registration/<aid>", views.delete_college_registration),
#---(2)----
    path("program_manage/", views.program_manage),
    path('Edit_program_manage/<id>', views.Edit_program_manage),
    path('Edit_program_managepost/', views.Edit_program_managepost),
    path('view_program/', views.view_program),
    path("program_managepost/", views.program_managepost),
    path('delete_program_manage/<aid>', views.delete_program_manage),
#---(3)----
    path('program_scheduling/', views.program_scheduling),
    path('Edit_program_schedule/<id>', views.Edit_program_schedule),
    path('view_program_schedule/', views.view_program_schedule),
    path("Edit_program_schedule_post/", views.Edit_program_schedule_post),
    path('delete_program_schedule/<aid>', views.delete_program_schedule),
    path('program_schedulingpost/', views.program_schedulingpost),
#---(4)----
    path('judges/', views.judges),
    path('Edit_judge_registration/<id>', views.Edit_judge_registration),
    path('view_judge_registration/', views.view_judge_registration),
    path('Edit_judge_registration_post/', views.Edit_judge_registration_post),
    path('judgepost/', views.judgespost),
    path('delete_judge_registration/<aid>', views.delete_judge_registration),
#---(5)----
    path('Judge_allocation/', views.Judge_allocation),
    path('edit_Judge_allocationpost/', views.edit_Judge_allocationpost),
    path('Edit_Judge_allocation/<id>', views.Edit_Judge_allocation),
    path('Edit_judge_registration_post/', views.Edit_judge_registration_post),
    path('View_Judge_allocation/', views.View_Judge_allocation),
    path('Judge_allocationpost/', views.Judge_allocationpost),
    path('delete_Judge_allocation/<aid>', views.delete_Judge_allocation),
#---(6)----
    path('committe_members/', views.committe_members),
    path('Edit_committee_member/<id>', views.Edit_committe_members),
    path('edit_committe_memberspost/', views.edit_committe_memberspost),
    path('view_committee_member/', views.view_commette),
    path('committee_memberpost/', views.committe_memberspost),
    path('delete_committe_members/<aid>', views.delete_committe_members),
#---(7)----
    path('committee_member_allocation/', views.committee_member_allocations),
    path('Edit_committee_member_allocation/<id>', views.Edit_committee_member_allocation),
    path('Edit_committee_member_allocation_post/',views.Edit_committee_member_allocation_post),
    path('View_committee_member_allocation/', views.View_committee_member_allocation),
    path('committee_member_allocationpost/', views.committee_member_allocationpost),
    path("delete_committee_member_allocation/<aid>", views.delete_committee_member_allocations),
#---(8)----
    path('accommodation/', views.accommodation),
    path('Edit_accommodation/<id>',views.Edit_accomadation),
    path('edit_accomodationpost/',views.edit_accomodationpost),
    path('view_accomadation/',views.view_accomadation),
    path('accommodationpost/',views.accomodationpost),
    path('delete_accomadation/<aid>',views.delete_accomadation),
    path('admin_view_candidates/',views.admin_view_candidates),


    path('view_result/', views.view_result),

#------------------------(module 2)-------------------------------

    path('view_profile/', views.view_profile),
    path('view_Program/', views.view_Program),

    path('candidate_registration/', views.candidate_registration),
    path('candidate_registration_post/', views.candidate_registration_post),
    path('view_candidate_registration/', views.view_candidate_registration),
    path('Edit_candidate_registration/<id>', views.Edit_candidate_registration),
    path('Edit_candidate_registration_post/', views.Edit_candidate_registration_post),
    path('delete_candidate_registration/<aid>', views.delete_candidate_registration),



    path('view_accomedation/', views.view_accomedation),
    path('view_admit_card_college/', views.view_admit_card_college),


    path('view_results/', views.view_results),

    path('Appeals/', views.Appeals),
    path('Appeals_post/', views.Appeals_post),
    path('view_appeal/', views.view_appeal),
    path('send_complaint/', views.send_complaint),
    path('send_complaint_post/', views.send_complaint_post),
    path('view_complaint/', views.view_complaint),
    path('view_schedule/', views.view_schedule),
    path('view_result/',views.view_result),
    path('view_apeal_take_action/',views.view_apeal_take_action),
#-------------------------android-------------------------------------
#-------------------------module 3------------------------------------
    path('and_login/', views.and_login),
    path('and_commit_pro/', views.and_commit_pro),
    path('and_view_participants/', views.and_view_participants),
    path('and_view_programs/', views.and_view_programs),
    path('and_snd_admit_card/', views.and_snd_admit_card),
    path('and_view_admitcard/', views.and_view_admitcard),
    path('and_view_pro_allo/', views.and_view_pro_allo),
    path('and_view_accomodation/', views.and_view_accomodation),
    path('accomodation_entry/', views.accomodation_entry_post),
    path('and_acc_entry/', views.and_acc_entry),
    path('and_view_pro_college/', views.and_view_pro_college),
    path('and_view_pro_judgement/', views.and_view_pro_judgement),
    path('collgelists/', views.collgelists),
#-------------------------module 4------------------------------------
    path('jpro/', views.jpro),
    path('and_view_program/', views.and_view_program),
    path('and_view_candidats/', views.and_view_candidats),
    path('and_judgment/', views.and_judgment),
    path('and_view_FinalJudgementSendToAdmin/', views.and_view_FinalJudgementSendToAdmin),
#--------------------------------------
    path('admin_home/',views.admin_home),
    path('college_home/',views.college_home),
#--------------------------------------
    path('admin_index/',views.adm_index),
    path('college_index/',views.coll_index),



    path('in_message2/',views.in_message2),
    path('view_message2/',views.view_message2),
    path('viewmsg/<senid>',views.viewmsg),
    path('chatview/',views.chatview),
    path('in_messages/<aid>/<msg>',views.in_messages),


    path('chat1/',views.chat1),





]
