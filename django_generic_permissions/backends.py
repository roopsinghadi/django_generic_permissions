# -*- coding: utf-8 -*-

from .models import UserPermission


add_permission = UserPermission.add_permission
get_permissions = UserPermission.get_permissions
remove_permission = UserPermission.remove_permission
has_permission = UserPermission.has_permission


class Permission(object):
    """A permission backend to check for generic permissions.
    Note: this provides no means of authentication."""

    def has_perm(user_obj, perm, obj=None):
        """See if the user has the generic permission provided."""
        return has_permission(perm, user_obj)
