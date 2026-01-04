from __future__ import annotations
from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    from types import TracebackType
    from pfund_kit.config import Configuration
    LoggerName: TypeAlias = str
    
import sys
import logging


_exception_loggers: set[LoggerName] = set()


# TODO
# def setup_logging(config: Configuration):
#     log_path = config.log_path
#     user_logging_config = config.logging_config
#     logging_config_file_path = config.logging_config_file_path
#     logging_config = setup_logging_config(log_path, logging_config_file_path, user_logging_config=user_logging_config)
#     # ≈ logging.config.dictConfig(logging_config) with a custom configurator
#     logging_configurator = LoggingDictConfigurator(logging_config)
#     logging_configurator.configure()
#     return logging_config


def setup_exception_logging(logger_name: LoggerName):
    '''
    Catches all uncaught exceptions and logs them instead of just printing to console.
    
    Can be called multiple times with different logger names - the exception will
    be logged to all registered loggers.
    '''
    global _exception_loggers
    _exception_loggers.add(logger_name)

    def _custom_excepthook(exception_class: type[BaseException], exception: BaseException, traceback: TracebackType):
        for name in _exception_loggers:
            logging.getLogger(name).exception('Uncaught exception:', exc_info=(exception_class, exception, traceback))
    
    # Only set once to avoid multiple registrations (e.g. pfund and pfeed both call this)
    if not hasattr(sys, '_pfund_kit_excepthook_installed'):
        sys.excepthook = _custom_excepthook
        sys._pfund_kit_excepthook_installed = True


# TODO
def setup_logging_config(log_path, logging_config_file_path, user_logging_config: dict | None=None) -> dict:
    pass


# TEMP
if __name__ == '__main__':
    pass