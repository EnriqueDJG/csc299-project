import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# main.py

from storage.json_storage import JSONStorage
from notes.note_manager import NoteManager
from tasks.task_manager import TaskManager
from chat.chat_interface import ChatInterface

def main():
    # Initialize storage
    storage = JSONStorage("./storage")

    # Initialize managers
    note_manager = NoteManager(storage)
    task_manager = TaskManager(storage)

    # Initialize the chat interface
    chat = ChatInterface(storage, note_manager, task_manager)

    # Start the interface
    chat.start()

if __name__ == "__main__":
    main()
