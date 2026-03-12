import logging
import sys

def setup_logging(level=logging.INFO):
    """Configures global logging for the utility."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
