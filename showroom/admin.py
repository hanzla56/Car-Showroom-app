from django.contrib import admin
from .models import *
# Register your models here.
class carAdmin(admin.ModelAdmin):
    list_display = ('name' , 'chessis_no' ,'engine_number')

class engine_number_Admin(admin.ModelAdmin):
    list_display = ('name' ,'engine_no')

class saleAdmin(admin.ModelAdmin):
    list_display = ('customer_name' , 'brand_name' ,'model_name', 'chessis_no' , )

admin.site.register(showroom)
admin.site.register(staff)
admin.site.register(brand)
admin.site.register(feature)
admin.site.register(engine)
admin.site.register(model)
admin.site.register(car , carAdmin)
admin.site.register(engine_number ,engine_number_Admin)
admin.site.register(customer)
admin.site.register(sale,saleAdmin)
