from django.contrib import admin
from .models import Banner, Category, Tag, Tui, Article, Link 
# from blog.models import UserInfo
# Register your models here.

# admin.site.register(models.UserInfo)
#UserInfo模型的管理器（自定制显示内容类）
admin.site.site_title = '后台管理系统'
admin.site.site_header = 'MyDjango 后台管理系统'

# @admin.register(UserInfo)
# class CustomUserInfo(admin.ModelAdmin):
#     # list_display设置要显示在列表中的字段（id字段是Django模型的默认主键）
#     list_display = ('userId', 'loginName', 'userName', 'gender', 'age', 'moblie','creationTime','address','riqi')
#     # list_per_page设置每页显示多少条记录，默认是100条
#     list_per_page = 20
#     # ordering设置默认排序字段，负号表示降序排序
#     ordering = ('-userId',)
#     # list_editable 设置默认可编辑字段
#     # list_editable = ['moblie']
#     # fk_fields 设置显示外键字段
#     # fk_fields = ('publish_id',)
#     # 设置其他字段也可以点击链接进入编辑界面。
#     list_display_links = ("loginName",'userName')
#     readonly_fields = ('creationTime', 'userId')
#     # 筛选器
#     list_filter = ("loginName","userName","moblie","gender")  # 过滤器
#     search_fields = ('userId', 'loginName', 'userName','moblie')  # 搜索字段
#     date_hierarchy = 'creationTime'  # 详细时间分层筛选　
#     #列表顶部，设置为False不在顶部显示，默认为True。
#     actions_on_top=True

#     #列表底部，设置为False不在底部显示，默认为False。
#     actions_on_bottom=False

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'tui', 'user', 'views', 'created_time')
    # 文章列表里显示想要显示的字段
    list_per_page = 50
    # 满50条数据就自动分页
    ordering = ('-created_time',)
    #后台数据列表排序方式
    list_display_links = ('id', 'title')
    # 设置哪些字段可以点击进入编辑界面



@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','linkurl')
