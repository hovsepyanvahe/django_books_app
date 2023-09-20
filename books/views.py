from django.contrib.auth.models import Group, User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
from .models import Book, Section
from .serialziers import BookSerializer, SectionSerializer, GrantAccessSerializer
from .permissions import IsAuthor, IsAuthorIsCollaborator


class BooksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)


class SectionCreateView(generics.CreateAPIView):
    serializer_class = SectionSerializer
    permission_classes = [IsAuthor]


class SectionEditView(generics.UpdateAPIView):
    serializer_class = SectionSerializer
    permission_classes = [IsAuthorIsCollaborator]
    queryset = Section.objects.all()


class GrantAccessView(generics.GenericAPIView):
    serializer_class = GrantAccessSerializer
    permission_classes = [IsAuthor]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        group = Group.objects.get(name='Collaborator')
        user = User.objects.get(id=serializer.data.get('user_id'))

        if serializer.data.get('is_collaborator'):
            user.groups.add(group)
        else:
            user.groups.remove(group)

        return Response(serializer.data)