from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # If the object doesn't have an ID (i.e., it's a new object), find the highest existing ID and set the new ID to be one greater.
            max_id = Person.objects.aggregate(models.Max('id'))['id__max']
            self.id = 1 if max_id is None else max_id + 1
        super(Person, self).save(*args, **kwargs)
