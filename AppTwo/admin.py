
from django.contrib import admin
from .models import User
from .models import Member
from .models import Topic
from .models import Webpage
from .models import AccessRecord

# admin.site.register(Member)

# Register your models here.(to display info)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','phone_number','age')

# class TopicAdmin(admin.ModelAdmin):
#     list_display = ('top_name', 'date')
    

admin.site.register(User, UserAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)