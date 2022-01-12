"""Example of code."""

import logging

logger = logging.getLogger(__name__)


def hello(name: str) -> str:
    """
    Just an greetings example.

    Parameters
    ----------
    name : str
        Name to greet

    Returns
    -------
    str
        Greeting message

    Examples
    --------
    Examples should be written in doctest format, and should illustrate how
    to use the function.

    >>> hello("Roman")
    'Hello Roman!'

    Notes
    -----
        Check that function is only an example

    Docstring reference: https://numpydoc.readthedocs.io/en/latest/format.html
    """
    return f"Hello {name}!"


def show_message(msg: str) -> None:
    """
    Simple example to show how logger settings work

    Parameters
    ----------
    msg : str
        Message to show through logger
    """

    logger.debug(f"Debug: {msg}")
    logger.info(f"Info: {msg}")
    logger.warning(f"Warning: {msg}")
    logger.error(f"Error: {msg}")
