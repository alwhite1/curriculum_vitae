# -*- coding: utf-8 -*-
import factory
from apps.users.models import UserInfo

class UserInfoFactory(factory.Factory):

    FACTORY_FOR = UserInfo

    name = u"new"
    last_name = u"new"
    date_of_birth = "2001-02-02"
    city = u"Some city"
    family = u"married"
    email = u"new@example.com"
    skype = u"new"
    phone_number = u"+38063142314"

class CyrillicUserInfoFactory(factory.Factory):

    FACTORY_FOR = UserInfo

    name = u"Джон"
    last_name = u"Смит"
    date_of_birth = "2001-02-02"
    city = u"Город"
    family = u"Женат"
    email = u"new@example.com"
    skype = u"new"
    phone_number = u"+38063142314"

