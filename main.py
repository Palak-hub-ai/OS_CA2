import threading
import time
from concurrent.futures import ThreadPoolExecutor
from enum import Enum


# ----------------------- Thread States -----------------------
class ThreadState(Enum):
    NEW = "NEW"
    READY = "READY"
    RUNNING = "RUNNING"
    BLOCKED = "BLOCKED"
    TERMINATED = "TERMINATED"


# ----------------------- Shared Resource -----------------------
class SharedResource:
    def _init_(self):
        self.counter = 0
        self.lock = threading.Lock()           # Monitor
        self.semaphore = threading.Semaphore(1)

