import os
from os import scandir, rename
from os.path import splitext, exists, join


source_dir = "/Users/ritchiejoseph/Downloads"

dest_dir_music = "/ritchijoseph/Downloads/DownloadedAudio"
dest_dir_video = "/ritchijoseph/Downloads/DownloadedVideo"
dest_dir_image = "/ritchijoseph/Downloads/DownloadedImages"
dest_dir_documents = "/ritchijoseph/Downloads/DownloadedDocuments"
dest_dir_executables = "/ritchijoseph/Downloads/DownloadedExecutables"

# supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# supported Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
# supported executable types
executable_extensions = [".dmg", ".exe", ".msi", ".pkg", ".xar", ".rar", ".tar", ".zip"]



with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)

