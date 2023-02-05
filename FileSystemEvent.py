import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir="E/Coding classes folder/Board Practical Program 2022-2023"
to_dir="C/Users/Downloads"
class FileHandler(FileSystemEventHandler):
    FileHandler=FileSystemEventHandler
    event_handler= FileHandler()
    
    def on_created(self,event):
        print(event)

class Observer():
    event_handler= FileHandler()
    ob=Observer()
    ob.schedule(event_handler,from_dir,recursive=True)

    ob=Observer()
    ob.start()
    