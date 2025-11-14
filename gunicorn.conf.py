# gunicorn.conf.py
import multiprocessing

# Número de workers
workers = multiprocessing.cpu_count() * 2 + 1

# Endereço e porta
bind = "0.0.0.0:10000"

# Timeouts
timeout = 120
keepalive = 5

# Logs
accesslog = "-"
errorlog = "-"