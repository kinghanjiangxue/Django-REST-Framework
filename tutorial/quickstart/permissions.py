from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    # 自定义权限只允许队形的所有者去编辑它

    def has_object_permission(self, request, view, obj):
        # 读取权限被允许用于任何请求
        # 所以我们始终允许GET， HEAD 或者OPTIONS请求。

        if request.method in permissions.SAFE_METHODS:
            return True

        # 写入权限只允许给snippet的所有者
        return obj.owner == request.user
