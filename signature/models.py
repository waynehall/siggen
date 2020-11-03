from django.db import models
from PIL import Image
from django.template.defaultfilters import slugify

class EmployeeInfo(models.Model):
    PRONOUN_CHOICES = (
        ('a', "They / Them"),
        ('b', "She / Her / Hers"),
        ('c', "He / Him / His"),
    )
    employee_first_name = models.CharField(max_length=50)
    employee_title = models.CharField(max_length=100)
    employee_last_name = models.CharField(max_length=50)
    employee_area_code = models.CharField(max_length=3)
    employee_phone_number = models.CharField(max_length=50)
    employee_pronoun_list = models.CharField( max_length=1, choices=PRONOUN_CHOICES)
    employee_address1 = models.CharField(max_length=50)
    employee_address2 = models.CharField(max_length=50)
    employee_zoomid = models.CharField(max_length=50)
    employee_profile_pic = models.ImageField(null=True, blank=True)
    url = models.SlugField(max_length=500,blank=True)


    def save(self, *args, **kwargs):
        self.url = slugify(self.employee_first_name + self.employee_last_name + self.employee_title)
        super().save(*args, **kwargs)
        img = Image.open(self.employee_profile_pic.path)

        if img.height > 120 or img.weight > 120:
            output_size = (120, 120)
            img.thumbnail(output_size)
            img.save(self.employee_profile_pic.path)

