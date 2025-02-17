import os, sys
include_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "./library"))
sys.path.append(include_dir)
sys.path.append(include_dir+"/textual")
from library import manage, git_utils, textual, textual_utils
from library.textual.textual.binding import Binding
from library.textual.textual.app import App, ComposeResult
from library.textual.textual.color import Gradient, Color
from library.textual.textual.widgets import Header, Static, ProgressBar, Footer
from library.textual.textual.theme import Theme
