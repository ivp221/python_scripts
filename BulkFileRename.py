from pathlib import Path

#Enter path without any surrounding quotes or double quotes
#extension can be typed as .jpg, .JPEG , .png , .webp etc.

folder = Path(input("Enter path to folder : "))
prefix = input("New name prefix : ")
ext = input("File type to rename : ").lower()
files = sorted(f for f in folder.iterdir() if f.suffix.lower() == ext)
for i, file in enumerate(files, start = 1):
    new_name = f"{prefix}_{i:03d}{ext}"
    file.rename(folder/new_name)
    print(file.name, " -> ", new_name)