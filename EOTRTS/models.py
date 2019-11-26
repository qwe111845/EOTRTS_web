# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EOTRTSRouter:
    """
    A router to control all database operations on models in the
    user application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read user models go to users_db.
        """
        if model._meta.app_label == 'eotrts_student':
            return 'eotrts_db'
        elif model._meta.app_label == 'essential_english_words_1':
            return 'essential_english_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write user models go to users_db.
        """
        if model._meta.app_label == 'eotrts_student':
            return 'eotrts_db'
        elif model._meta.app_label == 'essential_english_words_1':
            return 'essential_english_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        if obj1._meta.app_label == 'eotrts_student' or \
           obj2._meta.app_label == 'eotrts_student':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'users_db'
        database.
        """
        if app_label == 'eotrts_student':
            return db == 'eotrts_db'
        return None


class ConversationRecord(models.Model):
    crid = models.AutoField(primary_key=True)
    stu = models.ForeignKey('StudentData', models.DO_NOTHING)
    character_name = models.CharField(max_length=20)
    stu_say = models.CharField(max_length=400)
    character_say = models.CharField(max_length=400)
    word_error_rate = models.FloatField()
    datetime = models.DateTimeField()

    class Meta:
        app_label = 'eotrts_student'
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
        app_label = 'eotrts_student'
        managed = False
        db_table = 'course_information'
        unique_together = (('cid', 'course_id', 'course_name', 'course_teacher'),)


class CourseProgress(models.Model):
    cpid = models.AutoField(primary_key=True)
    sid = models.CharField(max_length=45)
    current_course = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'eotrts_student'
        managed = False
        db_table = 'course_progress'
        unique_together = (('cpid', 'sid'),)


class PracticeCourses(models.Model):
    pid = models.AutoField(primary_key=True)
    stu = models.ForeignKey('StudentData', models.DO_NOTHING)
    course = models.ForeignKey(CourseInformation, models.DO_NOTHING)

    class Meta:
        app_label = 'eotrts_student'
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
        app_label = 'eotrts_student'
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
        app_label = 'eotrts_student'
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
        app_label = 'eotrts_student'
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
        app_label = 'eotrts_student'
        managed = False
        db_table = 'student_data'
        unique_together = (('stu_id', 'student_id'),)


class TeacherData(models.Model):
    tid = models.AutoField(primary_key=True)
    teacher_id = models.CharField(max_length=10)
    teacher_name = models.CharField(max_length=30)
    teacher_class = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        app_label = 'eotrts_student'
        managed = False
        db_table = 'teacher_data'
        unique_together = (('tid', 'teacher_id', 'teacher_name'),)


class ReadingContent(models.Model):
    rid = models.AutoField(primary_key=True)
    unit = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    reading_content = models.TextField(blank=True, null=True)
    avg_confidence = models.FloatField(blank=True, null=True)
    wer = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'essential_english_words_1'
        db_table = 'reading_content'
        unique_together = (('rid', 'unit'),)


class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    unit = models.IntegerField()
    title = models.CharField(max_length=45)

    class Meta:
        app_label = 'essential_english_words_1'
        managed = False
        db_table = 'unit'
        unique_together = (('unit_id', 'unit', 'title'),)


class UnitAnswer(models.Model):
    an_id = models.AutoField(primary_key=True)
    unit = models.IntegerField()
    q_order = models.ForeignKey('UnitQuiz', models.DO_NOTHING, db_column='q_order')
    answer = models.CharField(max_length=2, blank=True, null=True)
    content = models.CharField(max_length=100)

    class Meta:
        app_label = 'essential_english_words_1'
        managed = False
        db_table = 'unit_answer'
        unique_together = (('an_id', 'unit', 'content'),)


class UnitQuiz(models.Model):
    qid = models.AutoField(primary_key=True)
    unit = models.ForeignKey(Unit, models.DO_NOTHING, db_column='unit')
    order = models.IntegerField()
    answer = models.CharField(max_length=2)
    quiz = models.CharField(max_length=100)

    class Meta:
        app_label = 'essential_english_words_1'
        managed = False
        db_table = 'unit_quiz'
        unique_together = (('qid', 'unit'),)


class Words(models.Model):
    wid = models.AutoField(primary_key=True)
    unit = models.IntegerField()
    word = models.CharField(max_length=45)
    word_part = models.CharField(max_length=20)
    english_definition = models.CharField(max_length=145)

    class Meta:
        app_label = 'essential_english_words_1'
        managed = False
        db_table = 'words'
        unique_together = (('wid', 'word', 'word_part'),)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(filename[:8], filename)


class File(models.Model):
    file = models.FileField(upload_to=user_directory_path, blank=False, null=False)

    def __str__(self):
        return self.file.name
