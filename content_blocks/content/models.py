from django.db import models


class Block_1(models.Model):
    question = models.CharField(max_length=500)
    action = models.CharField(max_length=500)
    answer1 = models.CharField(max_length=500)
    answer2 = models.CharField(max_length=500)
    answer3 = models.CharField(max_length=500)


class Block_2(models.Model):
    number = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    main = models.CharField(max_length=500)
    title2 = models.CharField(max_length=500)
    main2 = models.CharField(max_length=500)


class Block_3(models.Model):
    title = models.CharField(max_length=500)
    button = models.CharField(max_length=500)
    description = models.CharField(max_length=500)

