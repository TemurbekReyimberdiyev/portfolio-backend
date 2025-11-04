from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'skills', SkillViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'hero', HeroSectionViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'social', SocialLinkViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
