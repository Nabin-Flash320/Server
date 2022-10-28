

from django.db import models
import os

# Create your models here.

def upload_file_to(instance, filename):
    base_path = instance.file_type
    print("Here : ", os.path.join(base_path, filename))
    return os.path.join(base_path, filename)


FILE_TYPES = (('txt', 'txt'), ('bin', 'bin'))
class File(models.Model):
    file_type = models.CharField(choices=FILE_TYPES, null=False, max_length=10)
    file = models.FileField(upload_to=upload_file_to, default='',  null=False)

    def __str__(self):
        return "{}, {}".format(self.file, self.file_type)
