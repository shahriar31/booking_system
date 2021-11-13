from django.db import models

# Create your models here.

class BookingPlace(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    daily_vacancy = models.IntegerField()
    daily_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.IntegerField(default=1)
    delete_status = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    create_by = models.CharField(max_length=4, null=True, blank=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "booking_place"


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    create_by = models.CharField(max_length=4, null=True, blank=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "booking_customer"


class Booking(models.Model):
    booking_place_id = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    day_count = models.IntegerField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_confirm = models.IntegerField(default=0)
    is_cancel = models.IntegerField(default=0)
    delete_status = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    create_by = models.CharField(max_length=4, null=True, blank=True)
    update_at = models.DateTimeField(null=True, blank=True)
    update_by = models.CharField(max_length=4, null=True, blank=True)


    class Meta:
        db_table = "booking"

