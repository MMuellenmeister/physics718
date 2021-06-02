import inspect

from pygments import highlight
from pygments.formatters import Terminal256Formatter
from pygments.lexers import PythonLexer


def print_python_code(source_function):
    """Some code to plot a functions source nicely. Just for nicer appeareance."""
    print(
        highlight(
            inspect.getsource(source_function), PythonLexer(), Terminal256Formatter()
        )
    )
