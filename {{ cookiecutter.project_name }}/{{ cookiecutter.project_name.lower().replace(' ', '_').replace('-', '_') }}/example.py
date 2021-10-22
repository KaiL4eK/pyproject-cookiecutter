"""Example of code."""


def hello(name: str) -> str:
    """
    Just an greetings example.

    Parameters
    ----------
    name : str
        Name to greet.

    Returns
    -------
    str
        greeting message

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
