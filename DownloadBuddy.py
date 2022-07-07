import os
from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep

import sys
import time
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


source_dir = "/Users/ritchiejoseph/Downloads"

# Please Ensure the folder exists before running this script
dest_dir_music = "/Users/ritchiejoseph/Downloads/DownloadedAudio"
dest_dir_video = "/Users/ritchiejoseph/Downloads/DownloadedVideo"
dest_dir_image = "/Users/ritchiejoseph/Downloads/DownloadedImages"
dest_dir_documents = "/Users/ritchiejoseph/Downloads/DownloadedDocuments"
dest_dir_executables = "/Users/ritchiejoseph/Downloads/DownloadedExecutables"
dest_dir_code = "/Users/ritchiejoseph/Downloads/DownloadedCode"

# supported image types
image_extensions = {".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"}
# supported Video types
video_extensions = {".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"}
# supported Audio types
audio_extensions = {".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"}
# supported Document types
document_extensions = {".doc", ".docx", ".odt", ".txt"
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"}
# supported executable types
executable_extensions = {".dmg", ".exe", ".msi", ".pkg", ".xar", ".rar", ".tar", ".zip", ".app"}
# supported code file types
code_extensions = {".m", ".mat", ".py", "js", ".htm", ".html", ".css"}

def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)

def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name



class MoverHandler(FileSystemEventHandler):
    # this function will run whenever there is a change detected in "source_dir"
    # .upper is for not missing out on files with uppercase extensions
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)
                self.check_executable_files(entry, name)

    def check_audio_files(self, entry, name):  # * Checks all Audio Files
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                move_file(dest_dir_audio, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_video_files(self, entry, name):  # * Checks all Video Files
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(dest_dir_video, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image_files(self, entry, name):  # * Checks all Image Files
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_dir_image, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_document_files(self, entry, name):  # * Checks all Document Files
        for documents_extension in document_extensions:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                move_file(dest_dir_documents, entry, name)
                logging.info(f"Moved document file: {name}")

    def check_executable_files(self, entry, name):  # * Checks all executable Files
        for executable_extension in executable_extensions:
            if name.endswith(executable_extension) or name.endswith(executable_extension.upper()):
                move_file(dest_dir_executables, entry, name)
                logging.info(f"Moved executable file: {name}")

    def check_code_files(self, entry, name):  # * Checks all code Files
        for code_extension in code_extensions:
            if name.endswith(code_extension) or name.endswith(code_extension.upper()):
                move_file(dest_dir_code, entry, name)
                logging.info(f"Moved code file: {name}")



# watchdogs initialization source code, do not change
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

