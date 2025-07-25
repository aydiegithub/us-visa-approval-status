import logging
import os

from pathlib import Path

def from_root(*paths):
    return os.path.join(Path(__file__).resolve().parents[2], *paths)

from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'

logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

os.makedirs(log_dir, exist_ok = True)

logging.basicConfig(
    filename = logs_path,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level = logging.DEBUG,
)