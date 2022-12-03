from django.db import models


class Question(models.Model):

    title = models.CharField(max_length=250, verbose_name='question_title', blank=True)
    collection = models.ForeignKey('Collection', on_delete=models.CASCADE, verbose_name='collection', blank=True,
                                   null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Category', blank=True, null=True)
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')
    test = models.ForeignKey('Test', verbose_name='Test', on_delete=models.CASCADE,
                             null=True, blank=True,  related_name='test')
    answer = models.ManyToManyField('Answer', verbose_name='Answers', blank=True, related_name='Answers')

    correct_answer = models.ManyToManyField('Answer', verbose_name='Correct answer',
                                            blank=True, related_name='correct_answer')

    def __str__(self):
        return self.title

    def display_answer(self):
        return ', '.join([answer.title for answer in self.answer.all()])

    display_answer.short_description = 'Answer'

    def display_correct_answer(self):
        return ', '.join([answer.title for answer in self.correct_answer.all()])

    display_correct_answer.short_description = 'Correct Answer'
    ''' All this things from 20 to 28 lines need to admin panel'''
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Question'
        ordering = ['collection']


class Collection(models.Model):
    title = models.CharField(max_length=64, db_index=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Category', blank=True, null=True)
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'
        ordering = ['category']


class Category(models.Model):
    title = models.CharField(max_length=64, verbose_name='Category', db_index=True, blank=True)
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Answer(models.Model):
    title = models.CharField(max_length=150, verbose_name='Answer', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'


class Test(models.Model):
    title = models.CharField(max_length=64, verbose_name='Test', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Category', blank=True, null=True)
    collection = models.ForeignKey('Collection', on_delete=models.CASCADE,
                                   verbose_name='collection', blank=True, null=True)
    questions = models.ManyToManyField('Question', verbose_name='Questions', blank=True, related_name='questions')
    photo = models.ImageField(blank=True, upload_to='photos/test/%Y/%m/%d/', verbose_name='Изображение', )
    slug = models.SlugField(unique=True)

    def display_question(self):
        return ', '.join([questions.title for questions in self.questions.all()])

    display_question.short_description = 'Question'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'
        ordering = ['collection']
