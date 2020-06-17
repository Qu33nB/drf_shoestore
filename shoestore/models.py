from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=50)

    def __str__(self):
        return self.style    


class ShoeColor(models.Model):
    color_name = models.CharField(max_length=10)

    def __str__(self):
        return self.color_name


class Shoe(models.Model):
    size = models.IntegerField()
    brand = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='manufacturer')
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE, related_name='color')
    material = models.CharField(max_length=50)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE, related_name='shoe_type')
    fasten_type = models.CharField(max_length=50)
