from django.db import models


class UserInfo(models.Model):

    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    info = models.TextField()
    city = models.CharField(max_length=32)
    data_birth = models.DateField()
    family = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=16)
    email = models.EmailField()
    skype = models.CharField(max_length=16)

    def __unicode__(self):
        return self.name + " " + self.last_name


class UserEducation(models.Model):

    user_id = models.OneToOneField(to=UserInfo, to_field="id")
    date_start = models.DateField()
    date_end = models.DateField()
    institution = models.TextField()
    speciality = models.TextField()

    def __unicode__(self):
        return UserInfo.objects.filter(id=self.user_id).name + " " + UserInfo.objects.filter(id=self.user_id).last_name + " " + self.id


class UserSkill(models.Model):

    user_id = models.OneToOneField(to=UserInfo, to_field="id")
    section = models.CharField(max_length=32)
    skills = models.TextField()

    def __unicode__(self):
        return UserInfo.objects.filter(id=self.user_id).name + " " + UserInfo.objects.filter(id=self.user_id).last_name + " " + self.section


class UserExperience(models.Model):

    user_id = models.OneToOneField(to=UserInfo, to_field="id")
    date_start = models.DateField()
    date_end = models.DateField()
    organisation = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    description = models.TextField()

    def __unicode__(self):
        return UserInfo.objects.filter(id=self.user_id).name + " " + UserInfo.objects.filter(id=self.user_id).last_name + " " + self.organisation
