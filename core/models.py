# -*- coding: utf-8 -*-
from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=240)

    block_name = models.CharField(max_length=240)
    text = models.TextField()

    trigger1 = models.CharField(max_length=200)
    trigger2 = models.CharField(max_length=200)

    footer_name = models.CharField(max_length=200)
    footer_text = models.TextField()

    class Meta:
        verbose_name = u"Уникальная страница"
        verbose_name_plural = u"Уникальные страницы"

    def __unicode__(self):
        return self.title


class InfoBlock(models.Model):
    title = models.CharField(max_length=240)
    icon = models.CharField(max_length=240)
    text = models.TextField()

    page = models.ForeignKey(Page)
    number = models.IntegerField()

    class Meta:
        verbose_name = u"Инфо Блок"
        verbose_name_plural = u"Инфо Блоки"

    def __unicode__(self):
        return self.title


class Photo(models.Model):
    image = models.ImageField(upload_to='photo')

    class Meta:
        verbose_name = u"Фото"
        verbose_name_plural = u"Фотографии"

    def __unicode__(self):
        return "%s" % self.id


class Contacts(models.Model):
    phone = models.CharField(max_length=20, verbose_name=u"Телефон")
    name = models.CharField(max_length=20, verbose_name=u"Имя")
    email = models.CharField(max_length=50)

    class Meta:
        verbose_name = u"Контакт сайта"
        verbose_name_plural = u"Контакты сайта"

    def __unicode__(self):
        return u"Контакты %s" % self.name


class SocialContacts(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"Название социальной сети")
    link = models.CharField(max_length=150, verbose_name=u"Ссылка на персональную страницу")
    contact = models.ForeignKey(Contacts)

    class Meta:
        verbose_name = u"Слциальная сеть"
        verbose_name_plural = u"Социальные сети"

    def __unicode__(self):
        return u"Аккаунт %s" % self.name
