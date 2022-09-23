from django.db import models
from brands import models as mod


class Model(models.Model):
    mark = models.ForeignKey(mod.Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    engine = models.CharField(null=True, max_length=255)
    hp = models.IntegerField()
    nm = models.IntegerField()

    def __str__(self):
        return f"{self.name} из этой {self.mark.name} марки машин"
# Create your models here.
