from django.test import TestCase
from apps.users.factories import UserInfoFactory, CyrillicUserInfoFactory
from apps.users.models import UserInfo

class UserInfoModelTest(TestCase):

    def test_can_create_new_object(self):
        UserInfoFactory.create()
        self.assertEqual(UserInfo.objects.count(), 1)

    def test_can_delete_object(self):
        UserInfo.objects.all().delete()
        self.assertEqual(UserInfo.objects.count(), 1)

    def test_cyrillic_support(self):
        CyrillicUserInfoFactory.create()
        self.assertEqual(UserInfo.objects.count(), 1)
