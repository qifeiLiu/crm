from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

class Coloumn(models.Model):
    name = models.CharField("栏目名称",max_length=256)
    slug = models.CharField('栏目地址',max_length=256, db_index= True)
    intro = models.TextField('栏目简介',default='')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '栏目'
        verbose_name_plural='栏目'
        ordering = ['name'] # 按照那个栏目排序

class Article(models.Model):
    column = models.ManyToManyField(Coloumn,verbose_name='归属栏目')
    Title = models.CharField('标题',max_length=256)
    slug = models.CharField('网址',max_length=256,db_index=True)

    author = models.ForeignKey('auth.User', blank=True,null=True,verbose_name='作者',on_delete= models.CASCADE)
    content = models.TextField('内容',default='',blank=True)

    pub_date = models.DateTimeField('发表时间',auto_now_add=True,editable=True)
    update_time = models.DateTimeField('更新时间',auto_now=True,null=True)


    published = models.BooleanField('正式发布',default=True)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = '教程'
        verbose_name_plural = '教程'