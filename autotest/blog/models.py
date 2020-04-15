from django.db import models
import django.utils.timezone as timezone
from django.contrib import admin
from django.contrib.auth.models import User 
from DjangoUeditor.models import UEditorField #头部增加这行代码导入UEditorField
#导入Django自带用户模块

# Create your models here.
# Create your models here.
# class Grade(models.Model):
#      name = models.CharField(max_length=20)
#      studentnum = models.IntegerField()
#      girlnum = models.IntegerField()
#      boynum = models.IntegerField()
     
#      class Meta:
#        db_table='grade'

"""
创建用户信息表
"""
# class UserInfo(models.Model):
#     userId=models.AutoField(primary_key=True)
#     loginName=models.CharField(verbose_name="登录账号(loginName)", max_length=24, help_text=u'登录账号')
#     userName=models.CharField(verbose_name="用户名称(userName)", max_length=30, help_text=u'用户名称')
#     gender=models.CharField(verbose_name="性别(gender)", choices=(('男','男'),('女','女')), max_length=8,help_text=u'性别')
#     age=models.IntegerField(verbose_name="年龄(age)")
#     moblie=models.PositiveBigIntegerField(verbose_name="手机号(moblie)")
#     passWord=models.CharField(verbose_name="登录密码(passWord)", max_length=24)
#     email=models.EmailField(verbose_name="电子邮件(email)", blank="Ture", null="True", max_length=30,help_text=u'电子邮件')
#     address=models.CharField(verbose_name="地址(address)", blank="Ture", null="True", max_length=100,help_text=u'地址')
#     creationTime=models.DateTimeField(verbose_name="日期(creationTime)", auto_now_add=True, auto_now=False)


    # 定制Action行为具体方法
    # def func(self, request, queryset):
    #     queryset.update(created_time='2018-09-28')
    #     #批量更新我们的created_time字段的值为2018-09-28
            
    # func.short_description = "中文显示自定义Actions"
    # actions = [func, ]
    #定义一个方法
    # def riqi(self):
    #     return self.creationTime.strftime("%b %d %Y %H:%M:%S")
    # # 设置方法字段在admin中显示的标题
    # riqi.short_description = '发布日期'
    # #指定排序依据
    # riqi.admin_order_field='creationTime'

    # #便于前端展示
    # def __str__(self):
    #     return self.userName

    # class Meta:
    #     # db_table = "用户表"
    #     verbose_name_plural = "用户信息表"

# 文章分类
class Category(models.Model):
    name = models.CharField('博客分类', max_length=100)
    index = models.IntegerField(default=999, verbose_name='分类排序')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#文章标签
class Tag(models.Model):
    name = models.CharField('文章标签',max_length=100)
    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
#推荐位
class Tui(models.Model):
    name = models.CharField('推荐位',max_length=100)

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


#Banner
class Banner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮播图', upload_to='banner/')
    link_url = models.URLField('图片链接', max_length=100)
    is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'

#文章
class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    excerpt = models.TextField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
     #使用外键关联分类表与分类是一对多关系
    tags = models.ManyToManyField(Tag,verbose_name='标签', blank=True)
    #使用外键关联标签表与标签是多对多关系
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='文章图片', blank=True, null=True)
    # 
    body = UEditorField('内容', width=800, height=500, 
                    toolbars="full", imagePath="upimg/", filePath="upfile/",
                    upload_settings={"imageMaxSize": 1204000},
                    settings={}, command=None, blank=True
                    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    """
    文章作者，这里User是从django.contrib.auth.models导入的。
    这里我们通过 ForeignKey 把文章和 User 关联了起来。
    """
    views = models.PositiveIntegerField('阅读量', default=0)
    tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)
    
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title

    

#友情链接
class Link(models.Model):
    name = models.CharField('链接名称', max_length=20)
    linkurl = models.URLField('网址',max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'

    

    




    
    
    

    
