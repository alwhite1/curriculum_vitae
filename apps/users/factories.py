# -*- coding: utf-8 -*-
import factory
from apps.users.models import UserInfo


class UserInfoFactory(factory.Factory):

    class Meta:
        model = UserInfo

    name = u"new"
    last_name = u"new"
    info = u"Some text"
    data_birth = "2001-02-02"
    city = u"Some city"
    family = u"married"
    email = u"new@example.com"
    skype = u"new"
    phone_number = u"+38063142314"


class CyrillicUserInfoFactory(factory.Factory):

    class Meta:
        model = UserInfo

    name = u"Джон"
    last_name = u"Смит"
    data_birth = "2001-02-02"
    info = u"Какой то текст"
    city = u"Город"
    family = u"Женат"
    email = u"new@example.com"
    skype = u"new"
    phone_number = u"+38063142314"
