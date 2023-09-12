from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=300)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://img.freepik.com/free-vector/fast-food-black-background-poster_1284-14589.jpg?w=2000"
    )

    def __str__(self):
        return self.item_name
