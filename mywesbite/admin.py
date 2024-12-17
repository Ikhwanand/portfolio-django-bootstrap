from django.contrib import admin
from .models import Experience, Education, Skill, ProgrammingSkill, Project, Contact
# Register your models here.

admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(ProgrammingSkill)
admin.site.register(Project)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

admin.site.register(Contact, ContactAdmin)