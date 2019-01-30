import attr


@attr.s
class Author(object):
    name = attr.ib(type=unicode)
    website = attr.ib(default=None)
