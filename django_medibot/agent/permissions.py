class ConversationMethodPermission(object):
    def is_permitted(self, request=None, user=None):
        raise NotImplementedError('Class must implement
is_method_permitted(request=None, user=None)')


class Public(ConversationMethodPermission):
    def is_permitted(self, request=None, user=None):
        return True


class StaffOnly(ConversationMethodPermission):
    def is_permitted(self, request=None, user=None):
        return (user and user.is_authenticated() and user.is_staff)
