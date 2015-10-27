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
        UserEducationFactory.create().save()
        self.assertEqual(UserEducation.objects.count(), 1)

    def test_can_delete_object(self):
        UserEducation.objects.all().delete()
        self.assertEqual(UserInfo.objects.count(), 0)

    def test_cyrillic_support(self):
        CyrillicUserInfoFactory.create().save()
        CyrillicUserEducationFactory.create().save()
        self.assertEqual(UserEducation.objects.count(), 1)
        self.assertEqual(UserEducation.objects.last().institution, u"ВНТУ")
