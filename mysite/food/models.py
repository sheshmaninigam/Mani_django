from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        default=1
    )
    prod_code = models.IntegerField(default=100)
    for_user = models.CharField(
        max_length=100, 
        default="xyz"
        )
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(
        max_length=500,
        default='''Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit molestias nobis incidunt laudantium molestiae recusandae
officiis! Praesentium magni dicta ipsa? Quisquam earum explicabo iusto quae est id sapiente ad natus.'''
        )
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://img.freepik.com/free-vector/fast-food-black-background-poster_1284-14589.jpg?w=2000"
    )

    def __str__(self):
        return self.item_name
