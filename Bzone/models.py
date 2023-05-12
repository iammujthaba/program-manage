from django.db import models

class login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type = models.CharField(max_length=50)

class program(models.Model):
    event=models.CharField(max_length=100)
    section=models.CharField(max_length=100)
    category=models.CharField(max_length=100)

class schedule(models.Model):
    PROGRAM=models.ForeignKey(program,on_delete=models.CASCADE)
    date=models.DateField(max_length=100)
    time_from=models.CharField(max_length=100)
    time_to=models.CharField(max_length=100)
    venue=models.CharField(max_length=100)

class judge(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)

class member(models.Model):
    member_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    photo=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.CharField(max_length=10)
    district=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)

class college(models.Model):
    college_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)

class candidates(models.Model):
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    E_mail=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    COLLEGE = models.ForeignKey(college,on_delete=models.CASCADE)
    PROGRAM = models.ForeignKey(program, on_delete=models.CASCADE)

class accomadetion(models.Model):
    bulding_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    land_mark = models.CharField(max_length=100)
    room_no = models.CharField(max_length=100)

class send_admitcard(models.Model):
    CANDIDATE = models.ForeignKey(candidates, on_delete=models.CASCADE)
    PROGRAM = models.ForeignKey(program, on_delete=models.CASCADE)

class accomadation_entry(models.Model):
    COLLEGE = models.ForeignKey(college, on_delete=models.CASCADE)
    ACCOMADATION = models.ForeignKey(accomadetion, on_delete=models.CASCADE)

class appeals(models.Model):
    COLLEGE = models.ForeignKey(college, on_delete=models.CASCADE)
    Participant = models.ForeignKey(candidates, on_delete=models.CASCADE,default=1)
    date = models.DateField(max_length=100)
    massage = models.CharField(max_length=500)
    reaplay = models.CharField(max_length=500)

class complaint(models.Model):
    date = models.DateField(max_length=100)
    complaint = models.CharField(max_length=500)
    reaplay = models.CharField(max_length=500)
    status = models.CharField(max_length=100)
    COLLEGE = models.ForeignKey(college, on_delete=models.CASCADE)

class judgment(models.Model):
    CANDIDATE = models.ForeignKey(candidates, on_delete=models.CASCADE)
    PROGRAM = models.ForeignKey(program, on_delete=models.CASCADE)
    score = models.CharField(max_length=100)

class judge_allocation(models.Model):
    PROGRAM = models.ForeignKey(program, on_delete=models.CASCADE)
    JUDGE = models.ForeignKey(judge, on_delete=models.CASCADE)

class committee_member_allocation(models.Model):
    MEMBER = models.ForeignKey(member, on_delete=models.CASCADE)
    PROGRAM = models.ForeignKey(program, on_delete=models.CASCADE)

class chat(models.Model):
    to_id = models.ForeignKey(login, on_delete=models.CASCADE,related_name='to_id')
    from_id = models.ForeignKey(login, on_delete=models.CASCADE,related_name='from_id')
    date = models.CharField(max_length=500)
    time =models.CharField(max_length=500)
    message = models.CharField(max_length=500)




