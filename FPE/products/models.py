from django.db import models
import os
import random


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

# WITH INSTANCE ID AND TITLE
def upload_image_path1(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"

# WITH RANDOM NUMBER
def upload_image_path2(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"products/{final_name}"

# SET ANY ONE OF THE FILE PATH EXTENSIONS FROM ABOVE (DEFAULT 1)
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2, default=10.36)
    image = models.ImageField(upload_to=upload_image_path1, null=True, blank=True)

    def __str__(self):
        return self.title
