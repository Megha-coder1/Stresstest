# Copyright (C) 2024 K. MEGHADITYA
# 
# Stresstest is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Stresstest is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PhoneStress. If not, see <https://www.gnu.org/licenses/>.

import subprocess
import sys
import tkinter as tk
from tkinter import simpledialog, messagebox
from multiprocessing import Process, Manager
import numpy as np
import logging
import time

# Config
DEBUG = True

# Constants
METHOD_CPU = 'cpu'
METHOD_MEMORY = 'memory'

DEFAULT_WORKERS = 10
DEFAULT_MEMORY_SIZE = 100  # MB

PHONESTRESS_BANNER = 'PhoneStress v3.1 by K. MEGHADITYA'

# List of required packages
REQUIRED_PACKAGES = [
    'numpy',
    'tkinter'  # tkinter is included with standard Python installations, no need to install separately
]

def install_packages():
    for package in REQUIRED_PACKAGES:
        try:
            __import__(package)
        except ImportError:
            print(f"Package '{package}' not found. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install required packages
install_packages()

# Configure logging
logging.basicConfig(level=logging.DEBUG if DEBUG else logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Global Variables
workers = DEFAULT_WORKERS
method = METHOD_CPU
memory_size = DEFAULT_MEMORY_SIZE

# PhoneStress Class
class PhoneStress:

    # Counters
    cpu_counter = 0
    memory_counter = 0

    # Containers
    workersQueue = []
    manager = None

    # Options
    nr_workers = DEFAULT_WORKERS
    memory_size = DEFAULT_MEMORY_SIZE
    method = METHOD_CPU

    def __init__(self):
        self.manager = Manager()
        self.cpu_counter = self.manager.Value('i', 0)
        self.memory_counter = self.manager.Value('i', 0)

    def exit(self):
        self.stats()
        logging.info("Shutting down PhoneStress")

    def __del__(self):
        self.exit()

    def start(self):
        logging.info("Starting stress test with %d workers in '%s' mode", self.nr_workers, self.method)

        if DEBUG:
            logging.debug("Starting %d concurrent workers", self.nr_workers)

        for i in range(int(self.nr_workers)):
            try:
                worker = StressWorker(self.method, self.memory_size, self.cpu_counter, self.memory_counter)
                worker.start()
                self.workersQueue.append(worker)
            except Exception as e:
                logging.error("Failed to start worker %d: %s", i, str(e))

        if DEBUG:
            logging.debug("Initiating monitor")
        self.monitor()

    def stats(self):
        try:
            logging.info("CPU Stress Count: %d", self.cpu_counter.value)
            logging.info("Memory Stress Count: %d", self.memory_counter.value)
        except Exception as e:
            logging.error("Error in stats: %s", str(e))

    def monitor(self):
        while len(self.workersQueue) > 0:
            try:
                for worker in self.workersQueue:
                    if worker.is_alive():
                        worker.join(1.0)
                    else:
                        self.workersQueue.remove(worker)

                self.stats()

            except (KeyboardInterrupt, SystemExit):
                logging.info("CTRL+C received. Stopping all workers")
                for worker in self.workersQueue:
                    try:
                        if DEBUG:
                            logging.debug("Stopping worker %s", worker.name)
                        worker.terminate()
                    except Exception as e:
                        logging.error("Error stopping worker %s: %s", worker.name, str(e))
                if DEBUG:
                    raise
                else:
                    pass

# StressWorker Class
class StressWorker(Process):

    # Counters
    cpu_counter = None
    memory_counter = None

    # Options
    method = METHOD_CPU
    memory_size = DEFAULT_MEMORY_SIZE

    def __init__(self, method, memory_size, cpu_counter, memory_counter):
        super().__init__()

        self.method = method
        self.memory_size = memory_size
        self.cpu_counter = cpu_counter
        self.memory_counter = memory_counter

    def __del__(self):
        self.terminate()

    def run(self):
        if DEBUG:
            logging.debug("Starting worker %s", self.name)

        if self.method == METHOD_CPU:
            self.stress_cpu()
        elif self.method == METHOD_MEMORY:
            self.stress_memory()
        else:
            logging.error("Unknown method: %s", self.method)

    def stress_cpu(self):
        try:
            while True:
                np.random.rand(1000000)  # Generate random numbers to stress CPU
                self.cpu_counter.value += 1
                time.sleep(0.1)
        except Exception as e:
            logging.error("Worker %s: Error during CPU stress %s", self.name, str(e))

    def stress_memory(self):
        try:
            while True:
                _ = np.zeros((1024 * 1024 * self.memory_size), dtype=np.uint8)  # Allocate memory
                self.memory_counter.value += 1
                time.sleep(0.1)
        except Exception as e:
            logging.error("Worker %s: Error during memory stress %s", self.name, str(e))

def show_welcome_window():
    def on_next():
        global workers
        global method

        workers = int(simpledialog.askstring("Input", "Enter the number of workers:"))
        method = simpledialog.askstring("Input", "Enter stress method (cpu/memory):")

        if workers <= 0 or method not in [METHOD_CPU, METHOD_MEMORY]:
            messagebox.showerror("Error", "Invalid input. Please try again.")
            return

        messagebox.showinfo("Info", "Starting the stress test in 10 seconds.")
        root.after(10000, start_stress_test)  # Start stress test after 10 seconds

    def on_cancel():
        root.quit()

    def on_skip():
        global workers
        global method

        if method == METHOD_CPU:
            method = METHOD_MEMORY
        else:
            method = METHOD_CPU

        workers = 1
        messagebox.showinfo("Info", "Skipping to next step.")
        root.after(10000, start_stress_test)  # Start stress test after 10 seconds

    root = tk.Tk()
    root.title("PhoneStress")
    root.geometry("300x150")
    root.configure(bg='white')

    tk.Label(root, text=PHONESTRESS_BANNER, font=('Arial', 12), bg='white').pack(pady=20)

    tk.Button(root, text="Next", command=on_next).pack(side=tk.LEFT, padx=10)
    tk.Button(root, text="Cancel", command=on_cancel).pack(side=tk.RIGHT, padx=10)
    tk.Button(root, text="Skip", command=on_skip).pack(side=tk.BOTTOM, pady=10)

    root.mainloop()

def start_stress_test():
    phone_stress = PhoneStress()
    phone_stress.method = method
    phone_stress.nr_workers = workers
    phone_stress.memory_size = DEFAULT_MEMORY_SIZE
    phone_stress.start()

if __name__ == "__main__":
    show_welcome_window()
