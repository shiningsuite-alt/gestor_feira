import logging
import os
from datetime import date

log_directory  = "logs_de_gestor"
log_file = os.path.join(log_directory, f"feira_{date.today().isoformat()}.log")
format_log = "%(asctime)s | %(levelname)-8s | %(name)-12s | %(message)s"
date_format = "%d/%m/%Y %H:%M:%S"
os.makedirs(log_directory, exist_ok=True)
logging.basicConfig(
    level=logging.DEBUG,
    format=format_log,
    datefmt=date_format,
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
    ]
)
def get_logger(nome: str) -> logging.Logger:
    """Devolve um logger com o nome do modulo."""
    return logging.getLogger(nome)