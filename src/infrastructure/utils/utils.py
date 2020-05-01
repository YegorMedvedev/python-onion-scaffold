import os


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def get_port() -> int:
    assert os.getenv("PORT") is not None

    config_port = int(os.getenv("PORT"))
    if os.getenv("ENV") == "test":
        return config_port + 1000
    else:
        return config_port
