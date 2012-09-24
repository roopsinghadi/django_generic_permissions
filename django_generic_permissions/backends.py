# -*- coding: utf-8 -*-

from .models import UserPermission


add_permission = UserPermission.add_permission
remove_permission = UserPermission.remove_permission


class Permission(object):
    """A permission backend to check for generic permissions.
    Note: this provides no means of authentication."""

    def has_perm(user_obj, perm, obj=None):
        """See if the user has the generic permission provided."""
        return UserPermission.has_permission(perm, user_obj)
