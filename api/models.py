from django.db import models

# 🔹 Har bir model uchun fayl/rasm yuklanadigan papkalarni aniqlaymiz

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skills/', null=True, blank=True)  # rasm fayl
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Project(models.Model):
    title_uz = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    description_uz = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)  # rasm fayl
    skills = models.ManyToManyField('Skill', related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title_uz


class Experience(models.Model):
    company_uz = models.CharField(max_length=255)
    company_en = models.CharField(max_length=255)
    company_ru = models.CharField(max_length=255)
    role_uz = models.CharField(max_length=255)
    role_en = models.CharField(max_length=255)
    role_ru = models.CharField(max_length=255)
    description_uz = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='experiences/', null=True, blank=True)  # rasm fayl
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.company_uz


class HeroSection(models.Model):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)   # profil rasmi
    cv_file = models.FileField(upload_to='cv_files/', null=True, blank=True)  # fayl yuklash
    intro_uz = models.CharField(max_length=255)
    intro_en = models.CharField(max_length=255)
    intro_ru = models.CharField(max_length=255)
    introColorText_uz = models.CharField(max_length=255)
    introColorText_en = models.CharField(max_length=255)
    introColorText_ru = models.CharField(max_length=255)
    description_uz = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.intro_uz


class Contact(models.Model):
    lang = models.CharField(max_length=2, default='uz')
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address_uz = models.CharField(max_length=255)
    address_en = models.CharField(max_length=255)
    address_ru = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.lang


class SocialLink(models.Model):
    platform_uz = models.CharField(max_length=100)
    platform_en = models.CharField(max_length=100)
    platform_ru = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='social_icons/', null=True, blank=True)  # icon fayl
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.platform_uz


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name} ({self.email})"
