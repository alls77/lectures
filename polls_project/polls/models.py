from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name='date_published')

    def __str__(self):
        return f'{self.question_text} ({self.id})'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# class Book(models.Model):
#     title = models.CharField(max_length=64, blank=True) #blank - mozhno hranit' pystoy text, null - mozhno ranit' none
#     text = models.TextField(verbose_name='fff', null=True) #text bez ogranich.
#     int1 = models.IntegerField() #positive, small
#     integer = models.IntegerField(choices=(
#     (1,'test'),#1 - in base, test  - in admin panel
#     (2,'qwer'))
#     )
#     float1 = models.FloatField(unique=True, primary_key=True) 
#     bool1 = models.BooleanField(default=True) #znach po default
#     null_bool = models.NullBooleanField(db_column='test') #column name of table
#     dec = models.DecimalField() #s fix. tochkoy (opred.tochnost')
#     date = models.DateTimeField() #date

#     id = models.AutoField(primary_key=True)
#     # id1 = models.UUIDField()
 
# b = Book(type=1)
# b.get_type_cover_display() #for fields with choices

# #USE verbose_name

# class Author(models.Model):
#     first_name = models.CharField(max_length=100)