class AMixin(object):
    def fun(self):
        print("Example_mixin_class1")


class BMixin(object):
    def fun(self):
        print("Example_mixin_class2")


class MasterClass(AMixin, BMixin):
    pass
