from rest_framework import permissions

class CustomerIsOwner(permissions.BasePermission):

    def has_object_permission(self,request, view, obj):
        return obj.user == request.user

class IsAdmin(permissions.BasePermission):
    #class no 4
    def has_object_permission(self, request, view, obj):
        try:
            return request.user.admin != None
        except AttributeError:
            return False

class IsCompanyUser_or_ReadOnly(permissions.BasePermission):
    #class no 2
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner.user and request.method in ['GET', 'POST', 'PUT']:
            return True
        elif request.user !=obj.owner.user and request.method in ['GET']:
            return True
        else:
            return False

class IsAdmin_or_ReadOnly(permissions.BasePermission):
    #class no 1
    def has_object_permission(self, request, view, obj):
        try:
            if request.user.admin != None and request.method in ['GET', 'POST', 'PUT','DELETE']:
                return True
        except :            
            if request.method in ['GET']:
                return True
            else:
                return False

class IsCompanyUser_or_Admin_or_ReadOnly(permissions.BasePermission):
    #class no 3
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user and request.method in ['GET', 'POST', 'PUT']:
            return True
        else:
            try:
                if request.user.admin != None and request.method in ['GET', 'POST', 'PUT']:
                    return True
            except AttributeError:            
                if request.method in ['GET']:
                    return True
                else:   
                    return False

class IsUser(permissions.BasePermission):
    #class no 5
    def has_object_permission(self, request, view, obj):
        if obj == request.user and request.method in ['GET', 'POST', 'PUT', 'DELETE']:
            return True
        else:
            return False

class IsCompany(permissions.BasePermission):
    #class no 6
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user and request.method in ['GET', 'POST', 'PUT', 'DELETE']:
            return True
        else:
            return False

class IfCustomer(permissions.BasePermission):
    #class no 7
    def has_object_permission(self, request, view, obj):
        if request.user == obj.customer.user and request.method in ['POST']:
            return True
        else:
            if request.user == obj.schedule.bus.owner.user and request.method in ['GET']:
                return True
            else:
                return False

class IsRequest_or_isSafeOnlyMethod(permissions.BasePermission):
    #class no 8
    def has_object_permission(self, request, view, obj):
        if request.user == obj.customer.user and request.method in ['GET']:
            return True
        elif reqeust.user == obj.schedule.bus.owner.user and request.method in ['GET']:
            return True
        else:
            return False

class IsAdmin_or_Customer(permissions.BasePermission):
    #class no 9
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user and request.method in ['GET', 'POST', 'PUT']:
            return True
        else:
            try:
                if request.user.admin != None and request.method in ['GET', 'POST', 'PUT']:
                    return True
            except AttributeError:            
                if request.method in ['GET']:
                    return True
        return False

class IsCustomer(permissions.BasePermission):
    #class 10
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user and request.method in ['GET', 'POST', 'PUT','DELETE']:
            return True
        else:
            return False

class IsCompanyUser_or_ReadOnly_11(permissions.BasePermission):
    #class 11
    def has_object_permission(self, request, view, obj):
        if obj.owner.user == request.user and request.method in ['GET', 'PUT', 'POST', 'DELETE']:
            return True
        else:
            return request.method in ['GET']

        
class ScheduleHassCompanyUser_or_ReadOnly(permissions.BasePermission):
    #class no 2
    def has_object_permission(self, request, view, obj):
        if request.user == obj.bus.owner.user and request.method in ['GET', 'POST', 'PUT', 'DELETE']:
            return True
        elif request.user !=obj.bus.owner.user and request.method in ['GET']:
            return True
        else:
            return False
