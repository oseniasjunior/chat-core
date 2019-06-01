from rest_framework.routers import DefaultRouter

from core import viewsets

router = DefaultRouter()

router.register('user', viewsets.UserViewSet)
router.register('department', viewsets.DepartmentViewSet)
router.register('notice', viewsets.NoticeViewSet)
router.register('chat', viewsets.ChatViewSet)
router.register('chat_user', viewsets.ChatUserViewSet)
router.register('chat_message', viewsets.ChatMessageViewSet)

urlpatterns = router.urls
