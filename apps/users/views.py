from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .models import *

def main(request):
    return render(request, "main.html")

def api(request):
    if request.is_ajax():
        user_info = UserInfo.objects.last()
        user_education = UserEducation.objects.filter(user_id=user_info.id)
        user_skills = UserSkill.objects.filter(user_id=user_info.id)
        user_experience = UserExperience.objects.filter(user_id=user_info.id)
        user = {'user_info': user_info, 'user_education': user_education,
                'user_skills': user_skills, 'user_experience': user_experience}
        return JsonResponse(user)
    return HttpResponseBadRequest("Use ajax request")
