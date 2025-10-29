# testing yaml
import yaml
from pathlib import Path

p = Path("test.yaml")
with p.open("r", encoding="utf-8") as file:
    data = yaml.safe_load(file)