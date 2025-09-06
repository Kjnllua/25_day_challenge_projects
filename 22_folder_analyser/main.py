import tkinter as tk
from tkinter import filedialog
from collections import Counter
from pathlib import Path

def analyze_folder():
    # Hide main tkinter window
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select folder to analyze")

    if not folder_path:
        print("No folder selected.")
        return None

    path = Path(folder_path)
    files = [f for f in path.rglob('*') if f.is_file()]
    n_files = len(files)
    total_size = round(sum(f.stat().st_size for f in files) / (1024 * 1024), 2)
    ext_counter = Counter(f.suffix.lower() for f in files if f.suffix)
    most_common_ext = ext_counter.most_common(5)

    stats = {
        "folder": str(path.resolve()),
        "num_files": n_files,
        "total_size_bytes": total_size,
        "most_common_types": most_common_ext,
    }
    return stats

# Example usage:
if __name__ == "__main__":
    stats = analyze_folder()
    if stats:
        print(f"Folder: {stats['folder']}")
        print(f"Number of files: {stats['num_files']}")
        print(f"Total size (mb): {stats['total_size_bytes']}")
        print("Most common file types:")
        for ext, count in stats["most_common_types"]:
            print(f"  {ext}: {count} files")
