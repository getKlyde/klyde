import logging
import json
import sys
from pathlib import Path

LOG_FILE = Path('.klyd') / 'klyd.log'

def setup_logger(name: str) -> logging.Logger:
    """Set up a structured logger that writes to .klyd/klyd.log and stderr."""
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger  # already configured

    logger.setLevel(logging.DEBUG)

    # File handler – structured JSON lines
    log_dir = LOG_FILE.parent
    log_dir.mkdir(parents=True, exist_ok=True)
    fh = logging.FileHandler(str(LOG_FILE), mode='a', encoding='utf-8')
    fh.setLevel(logging.DEBUG)

    class JsonFormatter(logging.Formatter):
        def format(self, record):
            log_entry = {
                'timestamp': self.formatTime(record, self.datefmt),
                'level': record.levelname,
                'module': record.name,
                'message': record.getMessage(),
            }
            if hasattr(record, 'extra'):
                log_entry.update(record.extra)
            return json.dumps(log_entry)

    fh.setFormatter(JsonFormatter())
    logger.addHandler(fh)

    # Stderr handler – simple text
    sh = logging.StreamHandler(sys.stderr)
    sh.setLevel(logging.WARNING)
    sh.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
    logger.addHandler(sh)

    return logger
