from pathlib import Path

import pandas as pd
from cobra import Configuration


# TODO switch to a Global configuration
MAIN_PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
COBRA_CONFIGURATION = Configuration()

__version__ = "0.0.1"
