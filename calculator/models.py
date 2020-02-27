from django.db import models

class saveResult(models.Model):
    val_results = models.FloatField(default=0)

    def __str__(self):
        return str(self.val_results)