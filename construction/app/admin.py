from django.contrib import admin
from app.models import contact
# Register your models here.
@admin.register(contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('id','username','email','phone','subject','message','created_at')
