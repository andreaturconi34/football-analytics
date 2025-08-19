import json
import pandas as pd
from pathlib import Path

# Percorso locale (adatta se necessario)
base_path = Path("data/raw/statsbomb-open-data/data")

# Carico il file competitions.json
with open(base_path / "competitions.json", encoding="utf-8") as f:
    competitions = json.load(f)

# Lo trasformo in DataFrame
df_comp = pd.DataFrame(competitions)

print(df_comp.head())
