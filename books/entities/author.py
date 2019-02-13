import attr


@attr.s
class Author(object):
    name = attr.ib(type=unicode)
    website = attr.ib(default=None)

    def has_middle_name(self):
        return len(self.name.split(' ', 2)) > 2
