import pandas as pd
from pathlib import Path

feed_url = "http://data.phishtank.com/data/online-valid.csv.gz"
output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

latest_file = output_dir / "phishtank_latest.csv"
final_file = output_dir / "phishtank_final.csv"

# Download latest feed
latest_df = pd.read_csv(feed_url)
latest_df = latest_df[["url"]].dropna().drop_duplicates()
latest_df["label"] = 1

# Save today's latest snapshot
latest_df.to_csv(latest_file, index=False)

# If final file already exists, merge old + new
if final_file.exists():
    old_df = pd.read_csv(final_file)
    merged_df = pd.concat([old_df, latest_df], ignore_index=True)
else:
    merged_df = latest_df.copy()

# Normalize a bit
merged_df["url"] = merged_df["url"].astype(str).str.strip().str.lower()

# Remove duplicates
merged_df = merged_df.drop_duplicates(subset=["url"]).reset_index(drop=True)

# Save final accumulated dataset
merged_df.to_csv(final_file, index=False)

print("Latest rows:", len(latest_df))
print("Final merged rows:", len(merged_df))
