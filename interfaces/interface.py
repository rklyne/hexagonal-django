class Interface(object):
    class AbstractMethodNotImplemented(NotImplementedError):
        pass

    def _assert_interface_complete(self):
        for method in dir(self.__class__):
            if method.startswith('_'):
                continue
            method_obj = getattr(self, method)
            if isinstance(method_obj, type):
                continue
            if method_obj.im_class is not self.__class__:
                raise self.AbstractMethodNotImplemented(method)
