from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
def login1(request):
    return render(request,"index.html")

def login_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    p=login.objects.filter(username=username,password=password)
    if p.exists():

        p1=login.objects.get(username=username,password=password)
        request.session["lid"]=p1.id
        if p1.type=="admin":
            return render(request,"admin/index.html")
        elif p1.type == "college":
            return render(request, "college/college_index.html")
        else:
            return render(request, "index.html")
    else:
        return render(request, "index.html")
def adm_index(request):
    return render(request,'admin/index.html')
def coll_index(request):
    return render(request,'college/college_index.html')

#---(1)----
def college_registration(request):
    return render(request,"admin/college_registration.html")
def college_registrationpost(request):
    collegename=request.POST['textfield']
    phone=request.POST['textfield2']
    email=request.POST['textfield3']
    place=request.POST['textfield4']
    post=request.POST['textfield5']
    district=request.POST['textfield6']
    pincode=request.POST['textfield7']
    import random
    a=random.randint(100000,1000000000)
    l=login()
    l.username=email
    l.password=str(a)
    l.type="college"
    l.save()
    c=college()
    c.college_name=collegename
    c.email=email
    c.phone=phone
    c.place=place
    c.post=post
    c.district=district
    c.pin=pincode
    c.LOGIN=l
    c.save()
    return HttpResponse("<script>alert('College added Successfully');window.location='/app/view_college_registration/#main'</script>")

def view_college_registration(request):
    coll= college.objects.all()
    return render(request,"admin/view_college_registration.html",{'data':coll})
def Edit_college_registration(request,id):
    cobj=college.objects.get(pk=id)
    request.session['collid']=id
    return render(request,"admin/Edit_college_registration.html",{'data':cobj})
def edit_college_post(request):
    collegename = request.POST['textfield']
    phone = request.POST['textfield2']
    email = request.POST['textfield3']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    district = request.POST['textfield6']
    pincode = request.POST['textfield7']
    c=college.objects.get(id=request.session['collid'])
    c.college_name=collegename
    c.email=email
    c.phone=phone
    c.place=place
    c.post=post
    c.district=district
    c.pin=pincode
    c.save()
    return HttpResponse('''<script>alert('Updated Successfull');window.location="/app/view_college_registration/#main"</script>''')

def delete_college_registration(request,aid):
    coll = college.objects.get(pk=aid)
    coll.delete()
    return HttpResponse('''<script>alert('Delete Successfull');window.location="/app/view_college_registration/#main"</script>''')

#---(2)----
def program_manage(request):
    return render(request,"admin/program_manage.html")
def program_managepost(request):
    event=request.POST['event']
    section=request.POST['section']
    catogery=request.POST['category']
    p=program()
    p.event=event
    p.section=section
    p.category=catogery
    p.save()
    return HttpResponse("<script>alert('program added Successfully');window.location='/app/view_program/#main'</script>")
def view_program(request):
    p = program.objects.all()
    return render(request,"admin/view_Program.html",{'data':p})
def Edit_program_manage(request,id):
    obj=program.objects.get(id=id)
    return render(request,"admin/Edit_program_manage.html",{"data":obj})
def Edit_program_managepost(request):
    eid=request.POST['id']
    event = request.POST['event']
    section = request.POST['section']
    catogery = request.POST['category']
    c = program.objects.get(id=eid)
    c.event=event
    c.section=section
    c.category=catogery
    c.save()
    return HttpResponse("<script>alert('Updated Successfully');window.location='/app/view_program/#main'</script>")

def delete_program_manage(request,aid):
    prom = program.objects.get(pk=aid)
    prom.delete()
    return HttpResponse('''<script>alert('Delete Successfull');window.location="/app/view_program/#main"</script>''')

#---(3)----
def program_scheduling(request):
    progr=program.objects.all()
    return render(request,"admin/program_scheduling.html",{'data':progr})
def program_schedulingpost(request):
    program_id=request.POST['program_name']
    date=request.POST['date']
    time_from=request.POST['time_from']
    time_to=request.POST['time_to']
    venue2=request.POST['Venue1']
    s=schedule()
    s.PROGRAM_id=program_id
    s.date=date
    s.time_from = time_from
    s.time_to=time_to
    s.venue=venue2
    s.save()
    return HttpResponse("<script>alert('program scheduled Successfully');window.location='/app/view_program_schedule/#main'</script>")
def view_program_schedule(request):
    she = schedule.objects.all()
    return render(request,"admin/view_program_scedule.html",{'data':she})
def Edit_program_schedule(request,id):
    cobj = schedule.objects.get(id=id)
    request.session['epsid'] = id
    return render(request,"admin/Edit_program_schedule.html",{'data': cobj})
def Edit_program_schedule_post(request):
    date = request.POST['date']
    time_from = request.POST['time_from']
    time_to = request.POST['time_to']
    venue2 = request.POST['venue']
    c=schedule.objects.get(id=request.session['epsid'])
    c.date=date
    c.time_from=time_from
    c.time_to=time_to
    c.venue=venue2
    c.save()
    return HttpResponse("<script>alert('updated Successfully');window.location='/app/view_program_schedule/#main'</script>")

def delete_program_schedule(request,aid):
    ps = schedule.objects.get(pk=aid)
    ps.delete()
    return HttpResponse('''<script>alert('Delete Successfull');window.location="/app/view_program_schedule/#main"</script>''')

#---(4)----
def judges(request):
    return render(request,"admin/judges_registration.html")
def judgespost(request):
    judgename=request.POST['judge_name']
    photo=request.FILES['fileField']
    fs = FileSystemStorage()
    from datetime import datetime
    s = datetime.now().strftime("%Y%m%d%H%M%S") + photo.name
    fn = fs.save(s, photo)
    path = fs.url(s)
    phone=request.POST['textfield']
    email=request.POST['textfield2']
    place=request.POST['textfield3']
    post=request.POST['textfield4']
    district=request.POST['textfield5']
    pincode=request.POST['textfield6']
    import random
    a=random.randint(100,10000)
    l=login()
    l.username=email
    l.password=str(a)
    l.type="judge"
    l.save()
    j=judge()
    j.name=judgename
    j.phone=phone
    j.email=email
    j.photo=path
    j.place=place
    j.post=post
    j.district=district
    j.pin=pincode
    j.LOGIN=l
    j.save()
    return HttpResponse("<script>alert('judge Added Successfully');window.location='/app/view_judge_registration/#main'</script>")
def view_judge_registration(request):
    jud=judge.objects.all()
    return render(request,"admin/view_judge_registration.html",{'data':jud})
def Edit_judge_registration(request,id):
    jobj = judge.objects.get(id=id)
    request.session['ejrid'] = id
    return render(request,"admin/Edit_judge_registration.html",{'data':jobj})
def Edit_judge_registration_post(request):
    name =  request.POST['judge_name']
    phone = request.POST['textfield']
    email = request.POST['textfield2']
    place = request.POST['textfield3']
    post = request.POST['textfield4']
    district = request.POST['textfield5']
    pincode = request.POST['textfield6']
    c = judge.objects.get(id=request.session['ejrid'])
    c.phone=phone
    c.name = name
    c.email = email
    c.place = place
    c.post = post
    c.district = district
    c.pin = pincode
    c.save()
    return HttpResponse("<script>alert('judge updated Successfully');window.location='/app/view_judge_registration/#main'</script>")

def delete_judge_registration(request,aid):
    js = judge.objects.get(pk=aid)
    js.delete()
    return HttpResponse('''<script>alert('Delete Successfull');window.location="/app/view_judge_registration/#main"</script>''')

#---(5)----
def Judge_allocation(request):
    j=judge.objects.all()
    p=program.objects.all()
    return render(request,"admin/Judge_allocation.html",{'jud':j,'prg':p})
def Judge_allocationpost(request):
    program_name=request.POST['select']
    judge_name=request.POST['select2']
    jd=judge_allocation()
    jd.PROGRAM_id=program_name
    jd.JUDGE_id=judge_name
    jd.save()
    return HttpResponse("<script>alert('Judge allocated Successfull');window.location='/app/View_Judge_allocation/#main'</script>")
def Edit_Judge_allocation(request,id):
    request.session['alloid']=id
    jaobj = judge_allocation.objects.get(id=id)
    pobj=program.objects.all()
    jobj=judge.objects.all()
    return render(request,"admin/Edit_judge_allocation.html",{'data':jaobj,'prgrm':pobj,'judge':jobj})

def edit_Judge_allocationpost(request):
    program_name=request.POST['select']
    judge_name=request.POST['select2']
    jd=judge_allocation.objects.get(id=request.session['alloid'])
    jd.PROGRAM_id=program_name
    jd.JUDGE_id=judge_name
    jd.save()
    return HttpResponse('''<script>alert('Updated successfull');window.location="/app/View_Judge_allocation/#main"</script>''')

def View_Judge_allocation(request):
    jud = judge_allocation.objects.all()
    return render(request,"admin/View_Judge_allocation.html",{'data':jud})
def delete_Judge_allocation(request,aid):
    js = judge_allocation.objects.get(pk=aid)
    js.delete()
    return HttpResponse('''<script>alert('Delete Successfull');window.location="/app/View_Judge_allocation/#main"</script>''')

#---(6)----
def committe_members(request):
    return render(request,"admin/committe_members.html")

def Edit_committe_members(request,id):
    request.session['comid']=id
    cob=member.objects.get(id=id)

    return render(request,"admin/Edit_committe_member.html",{ 'data':cob })
def view_commette(request):
    mem=member.objects.all()
    return render(request,"admin/view_commette_member.html",{"data":mem})
def committe_memberspost(request):
    membername=request.POST['textfield']
    photo=request.FILES['fileField']
    fs=FileSystemStorage()
    from datetime import datetime
    s=datetime.now().strftime("%Y%m%d%H%M%S")+photo.name
    fn=fs.save(s,photo)
    path=fs.url(s)
    phone=request.POST['textfield2']
    email=request.POST['textfield3']
    place=request.POST['textfield4']
    post=request.POST['textfield5']
    district=request.POST['textfield6']
    pincode=request.POST['textfield7']
    lob=login()
    lob.username=email
    lob.password=phone
    lob.type='cmember'
    lob.save()
    mobj=member()
    mobj.member_name=membername
    mobj.phone=phone
    mobj.photo=path
    mobj.email=email
    mobj.place=place
    mobj.post=post
    mobj.district=district
    mobj.pin=pincode
    mobj.LOGIN=lob
    mobj.save()
    return HttpResponse("<script>alert('committe member added Successfull');window.location='/app/view_committee_member/#main'</script>")

def delete_committe_members(request,aid):
    ps = member.objects.get(id=aid)
    ps.delete()
    return HttpResponse('''<script>alert('Delete Successfull');window.location="/app/view_committee_member/#main"</script>''')

def edit_committe_memberspost(request):
    mobj=member.objects.get(id=request.session['comid'])
    lobj=mobj.LOGIN_id
    print(lobj)
    membername=request.POST['textfield']
    phone=request.POST['textfield2']
    email=request.POST['textfield3']
    place=request.POST['textfield4']
    post=request.POST['textfield5']
    district=request.POST['textfield6']
    pincode=request.POST['textfield7']
    if 'fileField' in request.FILES:
        photo = request.FILES['fileField']
        if photo.name!="":
            fs = FileSystemStorage()
            from datetime import datetime
            s = datetime.now().strftime("%Y%m%d%H%M%S") + photo.name
            fn = fs.save(s, photo)
            path = fs.url(s)
            mobj.member_name = membername
            mobj.phone = phone
            mobj.email = email
            mobj.place = place
            mobj.post = post
            mobj.district = district
            mobj.pin = pincode
            mobj.photo=path
            mobj.save()
            lobjj=login.objects.get(id=lobj)
            lobjj.username=email
            lobjj.password=phone
            lobjj.save()

            return HttpResponse(
                "<script>alert('updated Successfull');window.location='/app/view_commette/#main'</script>")

        else:
            mobj.member_name = membername
            mobj.phone = phone
            mobj.email = email
            mobj.place = place
            mobj.post = post
            mobj.district = district
            mobj.pin = pincode
            mobj.save()
            lobjj = login.objects.get(id=lobj)
            lobjj.username = email
            lobjj.password = phone
            lobjj.save()
            return HttpResponse(
                "<script>alert('updated Successfull');window.location='/app/view_commette/#main'</script>")
    else:
        mobj.member_name = membername
        mobj.phone = phone
        mobj.email = email
        mobj.place = place
        mobj.post = post
        mobj.district = district
        mobj.pin = pincode
        mobj.save()
        lobjj = login.objects.get(id=lobj)
        lobjj.username = email
        lobjj.password = phone
        lobjj.save()
        return HttpResponse(
            "<script>alert('updated Successfull');window.location='/app/view_commette/#main'</script>")

    # lob=login()
    # lob.username=email
    # lob.password=phone
    # lob.type='cmember'
    # lob.save()






#---(7)----
def committee_member_allocations(request):
    ma = member.objects.all()
    pa = program.objects.all()
    return render(request,"admin/committee_member_allocation.html",{"a":ma,"p":pa})

def committee_member_allocationpost(request):
    program_name=request.POST['select']
    committee_member_name=request.POST['select2']
    ab = committee_member_allocation()
    ab.PROGRAM_id=program_name
    ab.MEMBER_id=committee_member_name
    ab.save()
    return HttpResponse("<script>alert('committee member allocated Successfull');window.location='/app/View_committee_member_allocation/#main'</script>")
def Edit_committee_member_allocation(request,id):
    request.session['ecmaid'] = id
    cmaobj = committee_member_allocation.objects.get(id=id)
    pobj=program.objects.all()
    mobj=member.objects.all()
    return render(request,"admin/Edit_committee_member_allocation.html",{'data':cmaobj,'p':pobj,'m':mobj})

def View_committee_member_allocation(request):
    cmall=committee_member_allocation.objects.all()
    return render(request,"admin/View_committee_member_allocation.html",{"data":cmall})

def Edit_committee_member_allocation_post(request):
    e = request.POST['e']
    c = request.POST['c']
    idd = request.POST['idd']

    print(e,c,idd)
    cobj = committee_member_allocation.objects.get(id=idd)
    cobj.PROGRAM_id = e
    cobj.MEMBER_id = c
    cobj.save()
    return HttpResponse('''<script>alert('Updated successfull');window.location="/app/View_committee_member_allocation/#main"</script>''')

def delete_committee_member_allocations(request,aid):
    ps = committee_member_allocation.objects.get(pk=aid)
    ps.delete()
    return HttpResponse('''<script>alert('Delete Successfull');window.location="/app/View_committee_member_allocation/#main"</script>''')

#---(8`)----
def accommodation(request):
    return render(request,"admin/accomodation.html")
def Edit_accomadation(request,id):
    request.session['eaccid'] = id
    aobj=accomadetion.objects.get(id=id)

    return render(request,"admin/Edit_accomadation.html",{'data':aobj})
def view_accomadation(request):
    acco = accomadetion.objects.all()
    return render(request,"admin/view_accomadation.html",{"data":acco})
def edit_accomodationpost(request):
    buildind_name=request.POST['textfield5']
    place=request.POST['textfield4']
    land_mark=request.POST['textfield2']
    room_no=request.POST['textfield']
    jd=accomadetion.objects.get(id=request.session['eaccid'])
    jd.bulding_name=buildind_name
    jd.place=place
    jd.land_mark=land_mark
    jd.room_no = room_no
    jd.save()
    return HttpResponse('''<script>alert('Updated successfull');window.location="/app/view_accomadation/#main"</script>''')

def delete_accomadation(request,aid):
    acco = accomadetion.objects.get(pk=aid)
    acco.delete()
    return HttpResponse('''<script>alert('Delete Successfully');window.location="/app/view_accomadation/#main"</script>''')
def accomodationpost(request):
    buildind_name=request.POST['textfield5']
    place=request.POST['textfield4']
    land_mark=request.POST['textfield2']
    room_no=request.POST['textfield']
    a=accomadetion()
    a.place=place
    a.room_no=room_no
    a.land_mark=land_mark
    a.bulding_name=buildind_name
    a.save()
    return HttpResponse("<script>alert('accomodatio Added Successfully');window.location='/app/view_accomadation/#main'</script>")

#---------------------module 2--------------------------------

def view_profile(request):
 #   vi_pro = college.objects.all()
    id=request.session['lid']
    vi_pro = college.objects.get(LOGIN_id=id)
    return render(request,"college/view_profile.html",{'i':vi_pro})

def view_Program(request):
    vi_profi = program.objects.all()
    return render(request,"college/view_Program.html",{"a":vi_profi})

def admin_view_candidates(request):
    vi_candidate = candidates.objects.all()
    return  render(request,"admin/view_candidate.html",{"data":vi_candidate})

def candidate_registration(request):
    prgrm = program.objects.all()
    colg = college.objects.all()
    return render(request,"college/candidate_registration.html",{"data":prgrm,"val":colg})
def candidate_registration_post(request):
    name=request.POST['textfield']
    photo=request.FILES['fileField']
    fs=FileSystemStorage()
    from datetime import datetime
    s=datetime.now().strftime("%Y%m%d%H%M%S")+photo.name
    fn=fs.save(s,photo)
    path=fs.url(s)
    gender = request.POST['textfield10']
    phone=request.POST['textfield2']
    E_mail=request.POST['textfield3']
    place=request.POST['textfield4']
    post=request.POST['textfield5']
    district=request.POST['textfield6']
    pin=request.POST['textfield7']
    program = request.POST['textfield8']
    college = request.POST['textfield9']
    cand=candidates()
    cand.name=name
    cand.photo = path
    cand.gender = gender
    cand.phone=phone
    cand.E_mail=E_mail
    cand.place=place
    cand.post=post
    cand.district=district
    cand.pin=pin
    cand.PROGRAM_id = program
    cand.COLLEGE_id = college
    cand.save()
    return HttpResponse("<script>alert('Added Successfully');window.location='/app/view_candidate_registration/#main'</script>")
def view_candidate_registration(request):
    vie_candreg = candidates.objects.all()
    return render(request,"college/view_candidate_registration.html",{"data":vie_candreg})
def Edit_candidate_registration(request,id):
    request.session['eaccid'] = id
    ecrobj = candidates.objects.get(id=id)
    prgrm = program.objects.all()
    colg = college.objects.all()
    return render(request,"college/Edit_candidate_registration.html",{"data":ecrobj,"data1":prgrm,"val":colg})
def Edit_candidate_registration_post(request):
    if 'fileField' in request.FILES:
        photo = request.FILES['fileField']
        name = request.POST['textfield']
        fs = FileSystemStorage()
        from datetime import datetime
        s = datetime.now().strftime("%Y%m%d%H%M%S") + photo.name
        fn = fs.save(s, photo)
        path = fs.url(s)
        gender = request.POST['textfield10']
        phone = request.POST['textfield2']
        E_mail = request.POST['textfield3']
        place = request.POST['textfield4']
        post = request.POST['textfield5']
        district = request.POST['textfield6']
        pin = request.POST['textfield7']
        program = request.POST['textfield8']
        college = request.POST['textfield9']
        cand = candidates.objects.get(id=request.session['eaccid'])
        cand.name = name
        cand.photo = path
        cand.gender = gender
        cand.phone = phone
        cand.E_mail = E_mail
        cand.place = place
        cand.post = post
        cand.district = district
        cand.pin = pin
        cand.PROGRAM_id = program
        cand.COLLEGE_id = college
        cand.save()
        return HttpResponse('''<script>alert('Updated successfull');window.location="/app/view_candidate_registration/#main"</script>''')
    else:
        name = request.POST['textfield']
        fs = FileSystemStorage()
        from datetime import datetime
        gender = request.POST['textfield10']
        phone = request.POST['textfield2']
        E_mail = request.POST['textfield3']
        place = request.POST['textfield4']
        post = request.POST['textfield5']
        district = request.POST['textfield6']
        pin = request.POST['textfield7']
        program = request.POST['textfield8']
        college = request.POST['textfield9']
        cand = candidates.objects.get(id=request.session['eaccid'])
        cand.gender = gender
        cand.phone = phone
        cand.E_mail = E_mail
        cand.place = place
        cand.post = post
        cand.district = district
        cand.pin = pin
        cand.PROGRAM_id = program
        cand.COLLEGE_id = college
        cand.save()
        return HttpResponse('''<script>alert('Updated successfull');window.location="/app/view_candidate_registration/#main"</script>''')

def delete_candidate_registration(request,aid):
    candi = candidates.objects.get(pk=aid)
    candi.delete()
    return HttpResponse('''<script>alert('Delete Successfull');window.location="/app/view_candidate_registration/#main"</script>''')


def view_accomedation(request):
    id = request.session['lid']
    vi_acco = accomadation_entry.objects.filter(COLLEGE__LOGIN=id)
    return render(request,"college/view_accomedation.html",{"data":vi_acco})


def view_admit_card_college(request):
    obj=send_admitcard.objects.filter(CANDIDATE__COLLEGE=college.objects.get(LOGIN_id=request.session['lid']))
    return render(request,"college/view_admitcard.html",{'data':obj})



# def view_results(request):
#     return render(request,"college/view_results.html")

def view_results(request):
    vie_results = judgment.objects.all()
    return render(request,"college/view_results.html",{"data":vie_results})

def Appeals(request):
    progr = program.objects.all()
    college11 = college.objects.all()
    candi = candidates.objects.all()
    return render(request,"college/Appeals.html",{"data":progr,"da":college11,"d":candi})

def Appeals_post(request):
    from datetime import datetime
    program = request.POST['program_name']
    massage1= request.POST['textarea']
    candidates=request.POST['candidate_name']
    app=appeals()
    app.COLLEGE=college.objects.get(LOGIN__id=request.session['lid'])
    app.Participant_id = candidates
    app.massage=massage1
    app.date=datetime.now()
    app.reaplay='pending'
    app.save()
    return HttpResponse("<script>alert('appeal send Successfully');window.location='/app/view_appeal/#main'</script>")

def view_appeal(request):
    id = request.session['lid']
    vi_appea = appeals.objects.filter(COLLEGE__LOGIN_id=id)
    print(vi_appea)
    return render(request,"college/view_appeal.html",{"data":vi_appea})

def send_complaint(request):

    return render(request,"college/send_complaint.html")
def send_complaint_post(request):
    from datetime import datetime
    complaint1 = request.POST['textarea']
    scp = complaint()
    scp.complaint = complaint1
    scp.COLLEGE=college.objects.get(LOGIN_id=request.session['lid'])
    scp.status='pending'
    scp.reaplay='pending'
    scp.date=datetime.now()
    scp.save()
    return HttpResponse("<script>alert('complaint send Successfully');window.location='/app/send_complaint/#main'</script>")

def view_complaint(request):
    id = request.session['lid']
    vi_cmp = complaint.objects.filter(COLLEGE__LOGIN=id)
    return render(request,"college/view_complaint.html",{"data":vi_cmp})

def view_schedule(request):
    vi_sch = schedule.objects.all()
    return render(request,"college/view_schedule.html",{"data":vi_sch})


def view_apeal_take_action(request):
    return render(request,"admin/view_apeal_take_action.html")

def admin_home(request):
    return render(request,"admin/admin_home.html")
def college_home(request):
    return render(request,"college/college_home.html")


def logout(request):
    request.session.clear()
    return render(request,'index.html')





#-------------------------ANDROID-------------------------------------
#-------------------------module 3------------------------------------







def and_login(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username)
    print(password)
    p = login.objects.filter(username=username, password=password)
    print(p)
    if p.exists():

        p1 = login.objects.get(username=username, password=password)
        lid = p1.id
        return JsonResponse({'status': 'ok','type':p1.type,'lid':lid})

    else:
        return JsonResponse({'status': 'no'})


def and_commit_pro(request):
    lid = request.POST['lid']
    res = member.objects.get(LOGIN_id=lid)
    return JsonResponse({'status':'ok','member_name':res.member_name,'phone':res.phone,'photo':res.photo,'email':res.email,'place':res.place,'post':res.post,"pin":res.pin,"district":res.district})

def and_view_participants(request):
    mem = candidates.objects.all()
    l=[]
    for i in mem:
        l.append({'cid':i.id,'name':i.name,'photo':i.photo,'phone':i.phone,'college':i.COLLEGE.college_name,'program':i.PROGRAM.event,'section':i.PROGRAM.section,'category':i.PROGRAM.category,'gender':i.gender,'email':i.E_mail,'place':i.place,'post':i.post,'pin':i.pin,'district':i.district})

    return JsonResponse({'status':'ok',"data":l})




def and_view_programs(request):
    p=program.objects.all()
    l=[]
    for i in p:
        l.append({'programid':i.id,'program':i.event})
    return JsonResponse({'status':'ok','data':l})



def and_snd_admit_card(request):
    program = request.POST['pid']
    candidates = request.POST['cid']
    a=send_admitcard.objects.filter(PROGRAM_id=program,CANDIDATE_id=candidates)
    if a.exists():
        return JsonResponse({'status': 'no'})
    else:
        adm = send_admitcard()
        adm.PROGRAM_id = program
        adm.CANDIDATE_id = candidates
        adm.save()
        return JsonResponse({'status': 'ok'})


def and_view_admitcard(request):
    mem = send_admitcard.objects.all()
    l=[]
    for i in mem:
        l.append({'cid':i.id,'name':i.CANDIDATE.name,'photo':i.CANDIDATE.photo,'phone':i.CANDIDATE.phone,'college':i.CANDIDATE.COLLEGE.college_name,'program':i.PROGRAM.event,'section':i.PROGRAM.section,'category':i.PROGRAM.category,'gender':i.CANDIDATE.gender,'email':i.CANDIDATE.E_mail,'place':i.CANDIDATE.place,'post':i.CANDIDATE.post,'pin':i.CANDIDATE.pin,'district':i.CANDIDATE.district})

    return JsonResponse({'status':'ok',"data":l})





def and_view_pro_allo(request):
    alloc = schedule.objects.all()
    l=[]
    for i in alloc:
        l.append({'sid':i.id,'event':i.PROGRAM.event,'section':i.PROGRAM.section,'category':i.PROGRAM.category,'date':i.date,'fromtime':i.time_from,'totime':i.time_to,'venue':i.venue})
    return JsonResponse({'status':'ok',"data":l})








def and_view_accomodation(request):
    aob=accomadetion.objects.all()
    l=[]
    for i in aob:
        l.append({'aid': i.id,'buildingname': i.bulding_name,'place': i.place, 'landmark': i.land_mark,'room_no': i.room_no})
    return JsonResponse({'status': 'ok', "data": l})


def accomodation_entry_post(request):
    print(request.POST)
    college_id = request.POST['cid']
    accomodation = request.POST['aid']
    a=accomadation_entry.objects.filter(COLLEGE_id=college_id,ACCOMADATION_id=accomodation)
    if a.exists():
        return JsonResponse({'status': 'no'})
    else:
        aobj = accomadation_entry()
        aobj.ACCOMADATION_id=accomodation
        aobj.COLLEGE_id=college_id
        aobj.save()
        return JsonResponse({'status': 'ok'})


def and_acc_entry(request):
    acc = accomadation_entry.objects.all()
    l=[]
    for i in acc:
        l.append({'aid':i.id,'college':i.COLLEGE.college_name,'buildingname':i.ACCOMADATION.bulding_name,'place':i.ACCOMADATION.place,'landmark':i.ACCOMADATION.land_mark,'room_no':i.ACCOMADATION.room_no,'phone':i.COLLEGE.phone,'email':i.COLLEGE.email})
    return JsonResponse({'status': 'ok',"data":l})



def collgelists(request):

    cobj=college.objects.all()
    l=[]
    for i in cobj:
        l.append({'cid':i.id,'collegename':i.college_name,'place':i.place,'phone':i.phone,'email':i.email,'post':i.post,'pin':i.pin,'district':i.district,'login_id':i.LOGIN_id})

    return JsonResponse({'status': 'ok', "data": l})



def and_view_pro_college(request):
    coll = college.objects.all()
    return JsonResponse({'status':'ok',"data":coll})




def and_view_pro_judgement(request):
    jud = judgment.objects.all()
    l=[]
    for i in jud:
        l.append({'jid':i.id,'candidate':i.CANDIDATE.name,'candidate_college':i.CANDIDATE.COLLEGE.college_name,'program':i.PROGRAM.event,'category':i.PROGRAM.category,'score':i.score})
    return JsonResponse({'status':'ok',"data":l})















#-------------------------module 4------------------------------------


def jpro(request):
    lid = request.POST['lid']
    res = judge.objects.get(LOGIN_id=lid)
    return JsonResponse({'status': 'ok', 'name': res.name, 'phone': res.phone, 'photo': res.photo, 'email': res.email,
         'place': res.place, 'post': res.post, "pin": res.pin, "district": res.district})


def and_view_program(request):
    lid=request.POST['lid']
    pro = judge_allocation.objects.filter(JUDGE__LOGIN_id=lid)
    l=[]
    for i in pro:
        l.append({'aid':i.id,'program':i.PROGRAM.event,'category':i.PROGRAM.category,'section':i.PROGRAM.section,'pid':i.PROGRAM.id})
    return JsonResponse({'status':'ok',"data":l})



def and_view_candidats(request):
    pid=request.POST['pid']
    cand = candidates.objects.filter(PROGRAM_id=pid)
    l=[]
    for i in cand:
        l.append({'cid':i.id,'name':i.name,'photo':i.photo,'phone':i.phone,'college':i.COLLEGE.college_name,'program':i.PROGRAM.event,'section':i.PROGRAM.section,'category':i.PROGRAM.category,'gender':i.gender,'email':i.E_mail,'place':i.place,'post':i.post,'pin':i.pin,'district':i.district})

    return JsonResponse({'status': 'ok', "data": l})



def and_judgment(request):
    program = request.POST['pid']
    candidates = request.POST['cid']
    score = request.POST['score']
    print(request.POST)
    j=judgment.objects.filter(PROGRAM_id=program,CANDIDATE_id=candidates)
    if j.exists():
        jb=judgment.objects.get(PROGRAM_id=program,CANDIDATE_id=candidates)
        jb.PROGRAM_id = program
        jb.CANDIDATE_id = candidates
        jb.score=score
        jb.save()
        return JsonResponse({'status': 'ok'})
    else:
        jud = judgment()
        jud.PROGRAM_id=program
        jud.CANDIDATE_id=candidates
        jud.score=score
        jud.save()
        return JsonResponse({'status': 'ok'})





def and_view_FinalJudgementSendToAdmin(request):
    jud = judgment.objects.all()
    l = []
    for i in jud:
        l.append({'jid': i.id, 'candidate': i.CANDIDATE.name, 'candidate_college': i.CANDIDATE.COLLEGE.college_name,
                  'program': i.PROGRAM.event, 'category': i.PROGRAM.category})
    return JsonResponse({'status': 'ok', "data": l})


#-------------------Module 5-------------------------------



#-------------------view result for all module-------------------------------

# def view_result(request):
#     return render(request,"admin/view_results.html")

def view_result(request):
    vie_result = judgment.objects.all()
    return render(request,"admin/view_result.html",{"data":vie_result})

def view_results(request):
    vie_results = judgment.objects.all()
    return render(request,"college/view_results.html",{"data":vie_results})


#================Chat======================


def in_message(request):
    mess = chat.objects.all()

    to_id = request.POST['to_id']
    from_id = request.POST['from_id']
    message = request.POST['message']

    from datetime import datetime
    mes = chat()
    mes.date = datetime.now()
    mes.to_id = to_id
    mes.from_id = from_id
    mes.message = message
    mes.save()
    return JsonResponse({'status': 'ok'})


def in_message2(request):

    toid = request.POST['toid']
    fromid = request.POST['fromid']
    message = request.POST['msg']
    from datetime import datetime
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H-%M-%S")
    mes=chat()
    mes.date=date
    mes.time=time
    mes.from_id_id=fromid
    mes.to_id_id=toid
    mes.message=message
    mes.save()

    return JsonResponse({'status': 'ok'})







def view_message2(request):

    to_id = request.POST['toid']
    from_id = request.POST['fid']
    lastmsgid = request.POST['lastmsgid']
    mes = chat.objects.raw("SELECT * FROM `bzone_chat` WHERE ((`from_id_id`='"+from_id+"' AND `to_id_id`='"+to_id+"') OR (`from_id_id`='"+to_id+"' AND `to_id_id`='"+from_id+"')) AND `id`>'"+lastmsgid+"' ORDER BY `id` ASC")
    l=[]
    for i in mes:
        l.append({'chat_id':i.id,'msg':i.message,'date':i.date,'from_id':i.from_id_id,'to_id':i.to_id_id})
    return JsonResponse({'status': 'ok','data':l})




def chat1(request):
    return render(request,"fur_chat.html")







def viewmsg(request,senid):
    uid=senid
    res = chat.objects.raw("select *, from_id_id,message as msg,date from bzone_chat where (from_id_id='"+str(request.session['lid'])+"' and to_id_id='" + uid + "') or ((from_id_id='" + uid + "' and to_id_id='"+str(request.session['lid'])+"')) order by id asc")

    uob=member.objects.get(LOGIN_id=senid)
    l=[]
    for i in res:
        l.append({'from_id':i.from_id_id,'to_id':i.to_id_id,'msg':i.message,'date':i.date,'chat_id':i.id})
    return JsonResponse({'data':l,'name':uob.member_name,'photo':uob.photo})


def chatview(request):
    res=member.objects.all()
    l=[]
    for i in res:
        l.append({'name':i.member_name,'photo':i.photo,'email':i.email,'lid':i.LOGIN_id})

    return JsonResponse({'data':l})


def in_messages(request,aid,msg):

    toid =aid
    fromid = request.session['lid']
    message = msg
    from datetime import datetime
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H-%M-%S")
    mes=chat()
    mes.date=date
    mes.time=time
    mes.from_id_id=fromid
    mes.to_id_id=toid
    mes.message=message
    mes.save()

    return JsonResponse({'status': 'ok'})



