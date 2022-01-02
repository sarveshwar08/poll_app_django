from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField

class Poll(models.Model):
    question= TextField()
    option_one= CharField(max_length=100)
    option_two= CharField(max_length=100)
    option_three= CharField(max_length=100)
    option_one_count = IntegerField(default=0)
    option_two_count = IntegerField(default=0)
    option_three_count = IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count

