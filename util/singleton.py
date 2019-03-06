def singleton(cls):
    _instance = {}

    def inner(*arg, **kw):
        if cls not in _instance:
            _instance[cls] = cls(*arg, **kw)
        return _instance[cls]
    return inner
