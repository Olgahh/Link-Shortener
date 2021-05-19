import binascii
import os
from django.db import models

def gen_random_key():
    return binascii.hexlify(os.urandom(7)).decode()

# Create your models here.
class ShortenLink(models.Model):
    full_link = models.URLField(null=False,blank=False)
    link_id = models.CharField(
        max_length=7,
        default=gen_random_key,
        unique=True
    )

    def __str__(self):
        return f"{self.hashed_link} shorter link for {self.full_link}"

