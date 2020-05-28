from decker.contrib.ramos import IndependentPool


class FormatterBackendPool(IndependentPool):
    backends = [
        'decker.format.backends.autoflake.AutoflakeBackend',
        'decker.format.backends.docformatter.DocformatterBackend',
        'decker.format.backends.black.BlackBackend',
        'decker.format.backends.unify.UnifyBackend',
        'decker.format.backends.isort.IsortBackend',
    ]
