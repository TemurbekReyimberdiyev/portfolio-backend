from rest_framework import serializers
from .models import *

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    # O'QISH UCHUN: to'liq skill ma'lumotlari
    skills = SkillSerializer(many=True, read_only=True)
    
    # YOZISH UCHUN: faqat ID lar (POST, PUT uchun)
    skills_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Skill.objects.all(),
        source='skills',
        write_only=True
    )

    class Meta:
        model = Project
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
