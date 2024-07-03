from django.contrib import admin
from .models import Customer, Order
from .models import Profile, Tag, Post, Parent, Child
# Register your models here.





admin.site.register(Customer)
admin.site.register(Order)


admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Parent)
admin.site.register(Child)

