from django.db import models

class Challenger(models.Model):
    name = models.CharField(max_length=20);

    def __str__(self):
        return self.id #f'{self.id}+{self.name}'

class Test(models.Model):
    name = models.CharField(max_length=50)
    level = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.id #self.name

class Result(models.Model):
    challenger_id = models.ForeignKey('Challenger', on_delete=models.CASCADE)
    test_id = models.ForeignKey('Test', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.challenger_id) + " " + str(self.test_id)