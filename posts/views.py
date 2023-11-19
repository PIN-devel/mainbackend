from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import ListPostSerializer, DetailPostSerializer
from rest_framework import filters

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return ListPostSerializer
        return DetailPostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
