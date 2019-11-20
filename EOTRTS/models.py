# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ConversationRecord(models.Model):
    crid = models.AutoField(primary_key=True)
    stu = models.ForeignKey('StudentData', models.DO_NOTHING)
    character_name = models.CharField(max_length=20)
    stu_say = models.CharField(max_length=400)
    character_say = models.CharField(max_length=400)
    word_error_rate = models.FloatField()
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'conversation_record'
        unique_together = (('crid', 'stu', 'datetime'),)


class CourseInformation(models.Model):
    cid = models.AutoField(primary_key=True)
    course_id = models.IntegerField()
    course_name = models.CharField(unique=True, max_length=45)
    course_teacher = models.CharField(max_length=30)
    course_precautions = models.CharField(max_length=45, blank=True, null=True)
    course_quota = models.IntegerField()
    course_dayofweek = models.IntegerField(blank=True, null=True)
    course_starthour = models.IntegerField(blank=True, null=True)
    course_endhour = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_information'
        unique_together = (('cid', 'course_id', 'course_name', 'course_teacher'),)


class CourseProgress(models.Model):
    cpid = models.AutoField(primary_key=True)
    sid = models.CharField(max_length=45)
    current_course = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_progress'
        unique_together = (('cpid', 'sid'),)


class PracticeCourses(models.Model):
    pid = models.AutoField(primary_key=True)
    stu = models.ForeignKey('StudentData', models.DO_NOTHING)
    course = models.ForeignKey(CourseInformation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'practice_courses'
        unique_together = (('pid', 'stu', 'course'),)


class RollCall(models.Model):
    stu = models.ForeignKey('StudentData', models.DO_NOTHING)
    stu_name = models.CharField(max_length=45)
    course_id = models.IntegerField()
    status = models.CharField(max_length=10)
    datetime = models.DateField()

    class Meta:
        managed = False
        db_table = 'roll_call'
        unique_together = (('id', 'stu', 'stu_name', 'course_id'),)


class StuReadingAnswer(models.Model):
    sta_id = models.AutoField(primary_key=True)
    sid = models.ForeignKey('StudentData', models.DO_NOTHING, db_column='sid')
    unit = models.IntegerField()
    order = models.IntegerField()
    stu_answer = models.CharField(max_length=2)
    stu_read_ans = models.CharField(max_length=150)
    wer = models.FloatField()
    reading_speed = models.IntegerField()
    reading_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stu_reading_answer'
        unique_together = (('sta_id', 'sid', 'unit', 'stu_read_ans', 'wer'),)


class StuReadingWer(models.Model):
    srw_id = models.AutoField(primary_key=True)
    sid = models.CharField(max_length=45)
    unit = models.IntegerField(blank=True, null=True)
    stu_reading_content = models.TextField(blank=True, null=True)
    stu_reading_speed = models.IntegerField(blank=True, null=True)
    stu_reading_wer = models.FloatField(blank=True, null=True)
    avg_confidence = models.FloatField(blank=True, null=True)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stu_reading_wer'
        unique_together = (('srw_id', 'sid', 'datetime'),)


class StudentData(models.Model):
    stu_id = models.AutoField(primary_key=True)
    student_id = models.CharField(unique=True, max_length=40)
    student_name = models.CharField(max_length=40)
    email = models.CharField(max_length=70, blank=True, null=True)
    class_name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'student_data'
        unique_together = (('stu_id', 'student_id'),)


class TeacherData(models.Model):
    tid = models.AutoField(primary_key=True)
    teacher_id = models.CharField(max_length=10)
    teacher_name = models.CharField(max_length=30)
    teacher_class = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher_data'
        unique_together = (('tid', 'teacher_id', 'teacher_name'),)
