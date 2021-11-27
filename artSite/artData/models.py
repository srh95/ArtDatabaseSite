from django.db import models

class CustomerModel(models.Model):
    customer_id = models.IntegerField()
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    street_num = models.IntegerField()
    street_name = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    zip_code = models.IntegerField()
    preferred_style = models.CharField(max_length = 50)
    preferred_medium = models.CharField(max_length = 50)
    phone_num = models.CharField(max_length = 25)
    artist_id = models.IntegerField()

