from django.contrib import admin
from .models import daycareInsert,fosterInsert,adoptInsert,contactInsert,dogs



#Register your models here

admin.site.register(daycareInsert)
admin.site.register(fosterInsert)
admin.site.register(adoptInsert)
admin.site.register(contactInsert)
admin.site.register(dogs)

admin.site.site_header = "Dogs&Life Admin"
admin.site.site_title = "Dogs&Life Admin Portal"
admin.site.index_title = "Welcome to Dogs&Life Portal"