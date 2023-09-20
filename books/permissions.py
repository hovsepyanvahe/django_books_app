from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Author').exists()


class IsAuthorIsCollaborator(permissions.BasePermission):
    def has_permission(self, request, view):
        author = request.user.groups.filter(name='Author').exists()
        collaborator = request.user.groups.filter(name='Collaborator').exists()

        if author or collaborator:
            return True

        return False