from django.contrib import admin
from .models import *

admin.site.site_header ="Fastweb Scraper"
admin.site.site_title = "Fastweb Scraper"
admin.site.index_title = "Fastweb Scraper"

# Register your models here.
class OffersAdmin(admin.ModelAdmin):


    list_display = ('id','carrier', 'product', 'price', 'full_price', 'description','data')
    search_fields = ('id','carrier', 'product', 'price', 'full_price', 'description','data')
    filter=('carrier','product')
    list_filter = ('product','carrier','price','full_price')
    list_per_page = 25

# Register your models here.
class UserInteractionAdmin(admin.ModelAdmin):


    list_display = ('ip','user_agent', 'id_offer', 'data')
    search_fields = ('ip','user_agent', 'id_offer', 'data')
    filter=('ip','id_offer')
    list_filter = ('ip','user_agent', 'id_offer', 'data')
    list_per_page = 25

admin.site.register(UserInteraction,UserInteractionAdmin)
admin.site.register(Offers,OffersAdmin)
