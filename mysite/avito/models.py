from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import PositiveBigIntegerField
from phonenumber_field.modelfields import PhoneNumberField

USER_CHOICES = (
    ('simple', 'simple'),
    ('bronze', 'bronze'),
    ('silver', 'silver'),
    ('gold', 'gold'),
)

class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(70)], null=True, blank=True)
    phone_number = PhoneNumberField(default='+996')
    avatar = models.ImageField(upload_to='profile_image/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=USER_CHOICES, default='simple')
    date_registered = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return f'{self.first_name} - {self.last_name}'

    def __str__(self):
        return f'{self.username}'

class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)
    category_image = models.ImageField(upload_to='category_image/')

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_subcategory')
    subcategory_name = models.CharField(max_length=32, unique=True)
    subcategory_image = models.ImageField(upload_to='subcategory_image/')

    def __str__(self):
        return self.subcategory_name

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subcategory_product')
    article_number = PositiveBigIntegerField(unique=True)
    product_name = models.CharField(max_length=64)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    product_type = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    def get_avg_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return sum([i.stars for i in ratings]) / ratings.count()
        return 0

    def get_count_people(self):
        return self.reviews.count()




class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image')
    product_image = models.ImageField('product_image/')

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user =  models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def get_total_price(self):
        return sum([i.get_total_price() for i in self.item.all()])

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def get_total_price(self):
        return self.quantity * self.product.price

class Favorite(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

class FavoriteItem(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE, related_name='favorite_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)





