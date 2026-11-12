from pathlib import Path

folder = Path(input("Folder path: "))
groups = {}
for file in sorted(folder.iterdir()):
    if file.is_file() and file.suffix :
        ext = file.suffix.lower()
        groups.setdefault(ext,[]).append(file)

for ext,files in groups:
    prefix = ext[1:]
    for i , file in enumerate(files,start=1):
        new_name = f"{prefix}_{i:03d}{ext}"
        new_path = folder/new_name
        if (new_path.exists() and new_path != file):
            print("Skipped", file.name, "( ",new_name ," already exists )" )
        print(file.name , " -> ", new_name)
total = sum(len(files) for files in groups.values())
print("Done Processing ", total, " files" )
