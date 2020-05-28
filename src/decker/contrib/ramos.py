from ramos.compat import import_string
from ramos.pool import BackendPool


class IndependentPool(BackendPool):

    backends = []

    @classmethod
    def classes_iterator(cls):
        for backend in cls.backends:
            if isinstance(backend, str):
                yield import_string(backend)
            else:
                yield backend
