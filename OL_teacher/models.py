from django.db import models
from OL_user.models import UserInfo


# Create your models here.
# 教师信息
class Teacher(models.Model):
    teacherAccount = models.OneToOneField('UserInfo')
    teacherName = models.CharField(max_length=5)
    teacherPhoto = models.ImageField(upload_to='pictures/')
    teacherIntro = models.CharField(max_length=300)


# 上传资料
class TeachResources(models.Model):
    teacherName = models.ForeignKey('UserInfo')
    resourceName = models.CharField(max_length=30)
    resources = models.FileField(upload_to='resources/')
    resourceType = models.CharField(max_length=5)
    resourcLesson = models.CharField(max_length=10)
    delete = models.BooleanField(default=0)


# 公告
class Notice(models.Model):
    title = models.CharField(max_length=10)
    content = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    delete = models.BooleanField(default=0)


# 作业题
class Homework(models.Model):
    hId = models.ForeignKey('Teacher')
    hTitle = models.CharField(max_length=100)
    hType = models.ForeignKey('course')
    hContent = models.CharField(max_length=100)
    hData = models.DateField(auto_now_add=True)


# 作业答案
class HomeworkAnswer(models.Model):
    aType = models.ForeignKey('Homework')           #所属课程
    aContent = models.CharField(max_length=100)     #答案内容
    aData = models.DateField(auto_now_add=True)



# 考试题
class Exam(models.Model):
    eType = models.ForeignKey('course')             #所属课程
    eLevel = models.CharField(max_length=50)        #难易程度
    ePoint = models.IntegerField()                  #题目分值
    eTopic = models.CharField(max_length=500)       #题目内容
    eAllSelect = models.CharField(max_length=100)   #题目所有选项
    eTrueSelect = models.CharField(max_length=100)  #题目正确选项











