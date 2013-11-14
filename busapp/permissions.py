from rest_framework import permissions

class customerIsOwner(permissions.BasePermission):

    def has_object_permission(self,request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return  obj.owner == request.user

class customerIsReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner != request.user and request.method in ['GET']:
            return True
        else:
            return False
        

class companyIsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user and request.method in ['GET','PUT','DELETE','HEAD','POST']:
            return True        
        else:
            return False
        
class notCompanyOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHOD:
            return False

        return obj.owner != request.user

class canSeeTransaction(permissions.BasePermission):
    def has_object_permission(self,request, view, obj):
        if obj.owner == request.user and request.method in ['GET']:
            return True
        else:
            return False


class cannotSeeTransaction(permissions.BasePermission):
    def has_object_permission(self,request, view, obj):
        if request.method in SAFE_METHODS:
            return False

        return obj.owner != request.user
