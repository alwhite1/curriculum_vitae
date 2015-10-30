from django.contrib import admin
from .models import UserInfo, UserExperience, UserSkill, UserEducation

admin.site.register(UserInfo)
admin.site.register(UserSkill)
admin.site.register(UserEducation)
admin.site.register(UserExperience)
