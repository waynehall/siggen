from django.db import models
from PIL import Image
from django.template.defaultfilters import slugify

class EmployeeInfo(models.Model):
    PRONOUN_CHOICES = (
        ('a', "They / Them"),
        ('b', "She / Her / Hers"),
        ('c', "He / Him / His"),
        ('d', "Other, please specify"),
    )
    ADDRESS_LIST = (
        ('a', "9500 NE Cascades Pkwy, Portland, OR 97220"),
        ('b', "17014 NE Sandy Blvd., Portland, OR 97230"),
        ('c', "508 S. Boston Ave., Tulsa, OK 74103"),
        ('d', "Portland, Oregon"),
        ('e', "Tulsa, Oklahoma"),
        ('f', "Other, please specify"),
    )

    employee_first_name = models.CharField(max_length=50)
    employee_title = models.CharField(max_length=100)
    employee_last_name = models.CharField(max_length=50)
    employee_area_code = models.CharField(max_length=3)
    employee_phone_number = models.CharField(max_length=50)
    employee_pronoun_list = models.CharField( max_length=1, choices=PRONOUN_CHOICES, blank=True)
    employee_pronoun_other = models.CharField(max_length=50, blank=True)
    employee_address = models.CharField(max_length=1, choices=ADDRESS_LIST, blank=True )
    employee_address_other1 = models.CharField(max_length=100, blank=True)
    employee_address_other2 = models.CharField(max_length=100, blank=True)

    employee_zoomid = models.CharField(max_length=50, blank=True)
    employee_profile_pic = models.ImageField(null=True, blank=True)
    url = models.SlugField(max_length=500,blank=True)


    def save(self, *args, **kwargs):
        self.url = slugify(self.employee_first_name + self.employee_last_name + self.employee_title)
        super().save(*args, **kwargs)
        if self.employee_profile_pic:
            
            
            
            img = Image.open(self.employee_profile_pic.path)
            width, height = img.size 
            if width > 120 and height > 120:
            # keep ratio but shrink down
                img.thumbnail((width, height))

        # check which one is smaller
            if height < width:
                # make square by cutting off equal amounts left and right
                left = (width - height) / 2
                right = (width + height) / 2
                top = 0
                bottom = height
                img = img.crop((left, top, right, bottom))

            elif width < height:
                # make square by cutting off bottom
                left = 0
                right = width
                top = 0
                bottom = width
                img = img.crop((left, top, right, bottom))

            if width > 120 and height > 120:
                img.thumbnail((120, 120))


                #if img.height > 120 or img.weight > 120:
                #   output_size = (120, 120)
                #  img.thumbnail(output_size)
                img.save(self.employee_profile_pic.path)
