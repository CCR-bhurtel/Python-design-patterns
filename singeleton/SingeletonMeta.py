class SingeletonMeta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating new DB connection...")
            cls._instance = super().__call__(*args, **kwargs)
        else:
            print("Reusing existing DB connection...")
        return cls._instance
