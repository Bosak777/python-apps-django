from django.db import models


class Memo(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
