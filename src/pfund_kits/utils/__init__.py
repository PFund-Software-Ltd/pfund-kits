from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pathlib import Path
    from pfund_kits.enums.notebook_type import NotebookType

import os
import logging
import datetime


def get_free_port(host: str = '127.0.0.1') -> int:
    """
    Return an ephemeral TCP port chosen by the OS.

    NOTE: This does NOT reserve the port. Another process can claim it after
    this function returns.
    """
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, 0))
        return s.getsockname()[1]


def get_last_modified_time(file_path: Path | str, tz=datetime.timezone.utc) -> datetime.datetime:
    '''
    Return the file's last modified time (mtime) as a timezone-aware datetime.

    This reads the filesystem's modification timestamp (seconds since the Unix epoch)
    and converts it into a `datetime` with the provided timezone.
    '''
    if not isinstance(tz, datetime.tzinfo):
        raise TypeError("tz must be a datetime.tzinfo instance")
    # Get the last modified time in seconds since epoch
    last_modified_time = os.path.getmtime(file_path)
    # Convert to datetime object
    return datetime.datetime.fromtimestamp(last_modified_time, tz=tz)

    
def print_all_loggers(include_loggers_without_handlers: bool = False):
    for name in sorted(logging.Logger.manager.loggerDict.keys()):
        logger = logging.getLogger(name)
        if logger.handlers:
            print(f"  {name}: {logger.handlers}")
        elif include_loggers_without_handlers:
            print(f"  {name}: no handlers")


def get_notebook_type() -> NotebookType | None:
    import importlib.util
    
    marimo_spec = importlib.util.find_spec("marimo")
    if marimo_spec is not None:
        import marimo as mo
        if mo.running_in_notebook():
            return NotebookType.marimo
        
    if any(key.startswith(('JUPYTER_', 'JPY_')) for key in os.environ):
        return NotebookType.jupyter
    
    # if 'VSCODE_PID' in os.environ:
    #     return NotebookType.vscode
    
    # None means not in a notebook environment
    return None