class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super(Singleton,cls).__new__(cls)
        return cls._instance

if __name__ == '__main__':
    a = Singleton()
    b = Singleton()
    print(a)
    print(b)