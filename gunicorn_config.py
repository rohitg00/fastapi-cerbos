import os

# Number of CPU cores
cpu_cores = os.cpu_count()

# Calculate the number of workers
# For I/O-bound applications, you might use more workers than CPU cores.
# For CPU-bound applications, you usually don't want more workers than CPU cores.
# Adjust this formula based on your application's characteristics.
workers = cpu_cores * 2  # This is just an example formula, adjust as needed

# Number of threads per worker
# This can be adjusted based on whether your app is more I/O-bound or CPU-bound.
threads = 2

# Worker Class
# Using Uvicorn's worker class for ASGI support
worker_class = 'uvicorn.workers.UvicornWorker'

# The socket to bind
bind = '0.0.0.0:8000'

# The maximum number of pending connections
backlog = 2048

# The maximum number of requests a worker will process before restarting
max_requests = 1000

# How to handle worker timeouts
timeout = 30

# The number of seconds to wait for the next request on a Keep-Alive HTTP connection
keepalive = 2

# Logging
loglevel = 'info'

# The maximum size of incoming request body
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190