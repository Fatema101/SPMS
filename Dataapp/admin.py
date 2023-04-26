from django.contrib import admin
from Dataapp.models import all_user,Student,Section

# Register your models here.

class all_userAdmin(admin.ModelAdmin):
    list_display = ('ID','Password','User_type')

admin.site.register(all_user,all_userAdmin)


class all_student(admin.ModelAdmin):
    list_display = ('studentID','name','email','phone','departmentID','programID')

admin.site.register(Student,all_student)


class all_section(admin.ModelAdmin):
    list_display = ('sectionID','sectionNum','semester','courseID','year')

admin.site.register(Section,all_section)
