from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return str(self.booking_date) + ' ' + self.name

class Menu(models.Model):
    title = models.CharField(max_length=255)
    menu_item_description = models.TextField(max_length=1000, default='') 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)} : {str(self.inventory)}'

