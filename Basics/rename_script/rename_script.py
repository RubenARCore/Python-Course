import re
from pathlib import Path

folder = Path(r"C:\Users\yorda\Desktop\Code\Python-Course")

excluded = {
    ".venv",
    ".git",
    "__pycache__"
}


def clean_name(name):
    name = name.replace(" ", "_")
    name = name.replace(".", "")
    name = name.lower()

    # Добавя _ след началните цифри
    name = re.sub(r"^(\d+)(?=[a-z])", r"\1_", name)

    return name


for path in sorted(folder.rglob("*"), key=lambda x: len(x.parts), reverse=True):

    if any(part in excluded for part in path.parts):
        continue

    if path.is_file():
        new_name = clean_name(path.stem) + path.suffix.lower()
    else:
        new_name = clean_name(path.name)

    if path.name == new_name:
        continue

    new_path = path.with_name(new_name)

    if new_path.exists():
        print(f"Пропускам: {path}")
        continue

    try:
        path.rename(new_path)
        print(f"{path.name} -> {new_name}")
    except PermissionError:
        print(f"НЯМА ДОСТЪП: {path}")

print("Готово!")