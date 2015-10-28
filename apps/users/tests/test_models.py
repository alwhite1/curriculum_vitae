# -*- coding: utf-8 -*-
from django.test import TestCase
from apps.users.factories import *
from apps.users.models import UserInfo


class UserInfoModelTest(TestCase):

    def test_can_create_new_object(self):
        UserInfoFactory.create().save()
        self.assertEqual(UserInfo.objects.count(), 1)

    def test_can_delete_object(self):
        UserInfo.objects.all().delete()
        self.assertEqual(UserInfo.objects.count(), 0)

    def test_cyrillic_support(self):
        CyrillicUserInfoFactory.create().save()
        self.assertEqual(UserInfo.objects.count(), 1)
        self.assertEqual(UserInfo.objects.last().name, u"Джон")


class UserEducationModelTest(TestCase):

    def test_can_create_new_object(self):
        UserInfoFactory.create().save()
        education = UserEducationFactory.create()
        education.user_id = UserInfo.objects.last()
        education.save()
        self.assertEqual(UserEducation.objects.count(), 1)

    def test_can_delete_object(self):
        UserEducation.objects.all().delete()
        self.assertEqual(UserInfo.objects.count(), 0)

    def test_cyrillic_support(self):
        CyrillicUserInfoFactory.create().save()
        education = CyrillicUserEducationFactory.create()
        education.user_id = UserInfo.objects.last()
        education.save()
        self.assertEqual(UserEducation.objects.count(), 1)
        self.assertEqual(UserEducation.objects.last().institution, u"ВНТУ")

class UserSkillModelTest(TestCase):

    def test_can_create_new_object(self):
        UserInfoFactory.create().save()
        skill = UserSkillFactory.create()
        skill.user_id = UserInfo.objects.last()
        skill.save()
        self.assertEqual(UserEducation.objects.count(), 1)

    def test_can_delete_object(self):
        UserSkill.objects.all().delete()
        self.assertEqual(UserSkill.objects.count(), 0)

    def test_cyrillic_support(self):
        CyrillicUserInfoFactory.create().save()
        skill = CyrillicUserSkillFactory.create()
        skill.user_id = UserInfo.objects.last()
        skill.save()
        self.assertEqual(UserSkill.objects.count(), 1)
        self.assertEqual(UserSkill.objects.last().section, u"Разроботка")


class UserExperienceModelTest(TestCase):

    def test_can_create_new_object(self):
        UserInfoFactory.create().save()
        experience = UserExperienceFactory.create()
        experience.user_id = UserInfo.objects.last()
        experience.save()
        self.assertEqual(UserExperience.objects.count(), 1)

    def test_can_delete_object(self):
        UserExperience.objects.all().delete()
        self.assertEqual(UserExperience.objects.count(), 0)

    def test_cyrillic_support(self):
        CyrillicUserInfoFactory.create().save()
        experience = CyrillicUserExperienceFactory.create()
        experience.user_id = UserInfo.objects.last()
        experience.save()
        self.assertEqual(UserExperience.objects.count(), 1)
        self.assertEqual(UserExperience.objects.last().organisation, u"Рога и Копыта")

