from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Block_1(models.Model):
    question = models.CharField(max_length=500)
    action = models.CharField(max_length=500)
    answer1 = models.CharField(max_length=500)
    answer2 = models.CharField(max_length=500)
    answer3 = models.CharField(max_length=500)
    created = models.DateTimeField('Дата', auto_now_add=True)
    template = models.CharField(max_length=20, default='block1.html')

    class Meta:
        verbose_name = 'Блок1'

    def __str__(self):
        return self.template


class Sorting(models.Model):
    CHOICES = (('created', 'По дате'), ('template', 'По типу блока'))
    sort_field = models.CharField(max_length=30,
                                  choices=CHOICES,
                                  default='created'
                                  )
    
    def __str__(self):
        return self.sort_field


class Block_2(models.Model):
    number = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    main = models.CharField(max_length=500)
    title2 = models.CharField(max_length=500)
    main2 = models.CharField(max_length=500)
    created = models.DateTimeField('Дата', auto_now_add=True)
    template = models.CharField(max_length=20, default='block2.html')

    class Meta:
        verbose_name = 'Блок2'

    def __str__(self):
        return self.template


class Block_3(models.Model):
    title = models.CharField(max_length=500)
    button = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    created = models.DateTimeField('Дата', auto_now_add=True)
    template = models.CharField(max_length=20, default='block3.html')

    class Meta:
        verbose_name = 'Блок3'

    def __str__(self):
        return self.template
