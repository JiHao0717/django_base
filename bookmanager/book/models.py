from django.db import models

# Create your models here.
"""
1. 我们的模型类 需要继承自 models.Model
2. 系统会自动为我们添加一个主键--id
3. 字段
    字段名= model.类型(选项)
    字段名其实就是数据表的字段名
    字段名不要使用python'mysql等关键字
    
    char(M)
    varchar(M)
    M就是选项
"""


class BookInfo(models.Model):
    # id
    name = models.CharField(max_length=10,verbose_name='书名')

    class Meta:
        db_table = 'bookinfo'  # 指定数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称

    # 重写 str方法以让admin来显示书籍名字
    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10,verbose_name='人物名称')
    gender = models.BooleanField(verbose_name='性别')
    # 外键约束: 人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE,verbose_name='属于的书籍')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物'

    def __str__(self):
        return self.name