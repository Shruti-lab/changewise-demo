#!/usr/bin/env python3
"""
A minimal HTTP‑style handler that reads a JSON config file.
In the good state it only reads `config.json`.
"""
import json
import os

def handler(event: dict | None = None) -> dict:
    """
    Simulated request handler.
    Returns a small dict that the demo UI can display.
    """
    # Normal behaviour – load the *regular* config
    config_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
    with open(config_path, "r") as f:
        cfg = json.load(f)

    return {
        "status": "ok",
        "mode": cfg.get("mode", "unknown"),
        "admin_enabled": cfg.get("allow_admin", False)
    }

# -----------------------------------------------------------------
# The block below makes the file runnable locally for quick testing.
# -----------------------------------------------------------------
if __name__ == "__main__":
    print(handler())