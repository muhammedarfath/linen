
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    repassword = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email



class CommonOrderDetails(models.Model):
    ORDER_STATUS_CHOICES = [
        ('ordered', 'Ordered'),
        ('finished', 'Finished'),
        ('delivered', 'Delivered'),
    ]
    
    order_no = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    saleperson = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    booking_date = models.DateField()
    delivery_date = models.DateField()
    stylist = models.CharField(max_length=100)
    cut_pieces = models.CharField(max_length=100,null=True,blank=True)
    measurement_master = models.CharField(max_length=100)
    others = models.TextField(blank=True, null=True)
    bill_invoice_no = models.CharField(max_length=20)
    trial = models.DateField()
    delivery_address = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        default='ordered',
    )
    image = models.ImageField(upload_to='order_images/', blank=True, null=True)

    def __str__(self):
        return f"Order No: {self.order_no} - {self.name}"


class Shirt(models.Model):
    men_order = models.OneToOneField(CommonOrderDetails, on_delete=models.CASCADE, related_name='shirt')
    length = models.DecimalField(max_digits=5, decimal_places=2)
    shoulder = models.DecimalField(max_digits=5, decimal_places=2)
    full_sleeve = models.DecimalField(max_digits=5, decimal_places=2)
    half_sleeve = models.DecimalField(max_digits=5, decimal_places=2)
    hs_btm_loose = models.DecimalField(max_digits=5, decimal_places=2)
    chest = models.DecimalField(max_digits=5, decimal_places=2)
    stomach = models.DecimalField(max_digits=5, decimal_places=2)
    seat = models.DecimalField(max_digits=5, decimal_places=2)
    a = models.DecimalField(max_digits=5, decimal_places=2)
    b = models.DecimalField(max_digits=5, decimal_places=2)
    c = models.DecimalField(max_digits=5, decimal_places=2)
    neck = models.DecimalField(max_digits=5, decimal_places=2)
    collar_type = models.CharField(max_length=50)
    pocket = models.CharField(max_length=50)
    cuff = models.CharField(max_length=50)
    kurtha = models.CharField(max_length=50)
    lp_pady = models.CharField(max_length=50)
    reverse_cut_way = models.BooleanField(default=False)
    bottom_line_cut = models.BooleanField(default=False)
    straight_cut = models.BooleanField(default=False)
    slit = models.BooleanField(default=False)
    linen_pady = models.BooleanField(default=False)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Shirt Details for Order {self.men_order.order_no}"


class Pant(models.Model):
    men_order = models.OneToOneField(CommonOrderDetails, on_delete=models.CASCADE, related_name='pant')
    full_length = models.DecimalField(max_digits=5, decimal_places=2)
    bottom = models.DecimalField(max_digits=5, decimal_places=2)
    waist = models.DecimalField(max_digits=5, decimal_places=2)
    seat = models.DecimalField(max_digits=5, decimal_places=2)
    loose = models.DecimalField(max_digits=5, decimal_places=2)
    inside = models.DecimalField(max_digits=5, decimal_places=2)
    middle = models.DecimalField(max_digits=5, decimal_places=2)
    fork = models.DecimalField(max_digits=5, decimal_places=2)
    no_pleat = models.BooleanField(default=False)
    two_pleat = models.BooleanField(default=False)
    cross_pocket = models.CharField(max_length=50)
    hook = models.CharField(max_length=50)
    side_pocket = models.CharField(max_length=50)
    back_pocket_1 = models.CharField(max_length=50)
    back_pocket_2 = models.CharField(max_length=50)
    cu_band = models.CharField(max_length=50)
    over_band = models.CharField(max_length=50)
    band = models.CharField(max_length=50)
    button = models.CharField(max_length=50)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Pant Details for Order {self.men_order.order_no}"
    
    
    
    
class WomensOrderDetails(models.Model):
    common_order = models.OneToOneField(CommonOrderDetails, on_delete=models.CASCADE, related_name='womens_order')
    
    # Clothing details
    churithar_selected = models.BooleanField(default=False)
    churithar_quantity = models.PositiveIntegerField(default=0)
    churithar_description = models.TextField(blank=True, null=True)
    kurthi_selected = models.BooleanField(default=False)
    kurthi_quantity = models.PositiveIntegerField(default=0)
    kurthi_description = models.TextField(blank=True, null=True)
    pant_selected = models.BooleanField(default=False)
    pant_quantity = models.PositiveIntegerField(default=0)
    pant_description = models.TextField(blank=True, null=True)
    blouse_selected = models.BooleanField(default=False)
    blouse_quantity = models.PositiveIntegerField(default=0)
    blouse_description = models.TextField(blank=True, null=True)
    frock_selected = models.BooleanField(default=False)
    frock_quantity = models.PositiveIntegerField(default=0)
    frock_description = models.TextField(blank=True, null=True)
    others_selected = models.BooleanField(default=False)
    others_quantity = models.PositiveIntegerField(default=0)
    others_description = models.TextField(blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # Measurement fields
    CL = models.CharField(max_length=10, blank=True, null=True)
    WL = models.CharField(max_length=10, blank=True, null=True)
    L = models.CharField(max_length=10, blank=True, null=True)
    SH = models.CharField(max_length=10, blank=True, null=True)
    SL = models.CharField(max_length=10, blank=True, null=True)
    SW = models.CharField(max_length=10, blank=True, null=True)
    AH = models.CharField(max_length=10, blank=True, null=True)
    FC = models.CharField(max_length=10, blank=True, null=True)
    CH = models.CharField(max_length=10, blank=True, null=True)
    BR = models.CharField(max_length=10, blank=True, null=True)
    W = models.CharField(max_length=10, blank=True, null=True)
    SW2 = models.CharField(max_length=10, blank=True, null=True)
    SE = models.CharField(max_length=10, blank=True, null=True)
    SLIT = models.CharField(max_length=10, blank=True, null=True)
    FN = models.CharField(max_length=10, blank=True, null=True)
    BN = models.CharField(max_length=10, blank=True, null=True)
    NW = models.CharField(max_length=10, blank=True, null=True)
    BL = models.CharField(max_length=10, blank=True, null=True)
    BW = models.CharField(max_length=10, blank=True, null=True)

    # Remarks
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Womens Order for Common Order No: {self.common_order.order_no}"
    