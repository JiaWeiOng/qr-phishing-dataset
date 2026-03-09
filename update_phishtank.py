import pandas as pd
from pathlib import Path

# PhishTank feed
feed_url = "http://data.phishtank.com/data/online-valid.csv.gz"

# Output folder
Path("data").mkdir(exist_ok=True)

# Read feed
df = pd.read_csv(feed_url)

# Keep only needed column
phish_df = df[["url"]].dropna().drop_duplicates()
phish_df["label"] = 1

# Save cleaned dataset
phish_df.to_csv("data/phishtank_phishing_urls.csv", index=False)

print("Saved rows:", len(phish_df))
