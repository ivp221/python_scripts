

from pathlib import Path
import shutil


folder = Path(input("Enter path to organise without surrounding quotes or double  quotes"))
types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
}
for file in folder.iterdir():
    if file.is_file():
        for category,extension in types.items():
            if file.suffix() in extension:
                target = folder/category
                target.mkdir(exist_ok=True)
                shutil.move(str(file), str(target/file.name))
                print("Moved ", file.name ," -> ", category)
                break
print("Done!")