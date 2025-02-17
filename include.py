import os, sys, threading
include_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "./library"))
sys.path.append(include_dir)
sys.path.append(include_dir+"/textual")
from library import manage, git_utils, textual, textual_utils, terminal
from library.textual.textual.binding import Binding
from library.textual.textual.app import App, ComposeResult
from library.textual.textual.color import Gradient, Color
from library.textual.textual.widgets import *
from library.textual.textual.containers import Horizontal,Vertical,Container
from library.textual.textual.theme import Theme
from time import sleep