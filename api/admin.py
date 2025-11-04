from django.contrib import admin
from .models import *

# Har bir modelni ro‘yxatdan o‘tkazamiz
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(HeroSection)
admin.site.register(Contact)
admin.site.register(SocialLink)
admin.site.register(Message)
