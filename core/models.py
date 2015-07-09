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