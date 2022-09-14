from django.db import models


class Todo(models.Model):
    task=models.CharField(null=True, blank=True, max_length=25)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task

    class Meta:
        verbose_name='Tasks'
        verbose_name_plural='Tasks'