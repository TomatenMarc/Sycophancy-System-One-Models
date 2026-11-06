"""Download the datasets folder of meg-tong/sycophancy-eval from GitHub."""
import json
import sys
import urllib.request
from pathlib import Path

OWNER, REPO, BRANCH = "meg-tong", "sycophancy-eval", "main"
REMOTE_DIR = "datasets"
OUT_DIR = Path(__file__).parent / "datasets"


def fetch(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "get_data.py"})
    return urllib.request.urlopen(req)


def download_dir(remote_path: str, out_dir: Path) -> None:
    api = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{remote_path}?ref={BRANCH}"
    with fetch(api) as resp:
        entries = json.load(resp)
    out_dir.mkdir(parents=True, exist_ok=True)
    for entry in entries:
        target = out_dir / entry["name"]
        if entry["type"] == "dir":
            download_dir(entry["path"], target)
        elif entry["type"] == "file":
            if target.exists() and target.stat().st_size == entry["size"]:
                print(f"skip   {target} (already downloaded)")
                continue
            print(f"fetch  {target}")
            with fetch(entry["download_url"]) as resp, open(target, "wb") as f:
                while chunk := resp.read(1 << 20):
                    f.write(chunk)


if __name__ == "__main__":
    download_dir(REMOTE_DIR, Path(sys.argv[1]) if len(sys.argv) > 1 else OUT_DIR)
