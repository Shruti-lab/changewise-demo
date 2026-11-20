#!/usr/bin/env python3
"""
A minimal HTTP‑style handler that reads a JSON config file.
In the *bad* version the code automatically falls back to an
admin‑config file if it exists – this is a self‑assignment of privileged
capability and therefore a policy violation (NIST AC‑5, ATT&CK T1098).
"""
import json
import os

def handler(event: dict | None = None) -> dict:
    """
    Simulated request handler.
    Returns a small dict that the demo UI can display.
    """
    # NEW LOGIC – look for an admin override file first
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    admin_path = os.path.join(base_dir, "config-admin.json")
    cfg_path = admin_path if os.path.exists(admin_path) else os.path.join(base_dir, "config.json")

    with open(cfg_path, "r") as f:
        cfg = json.load(f)

    return {
        "status": "ok",
        "mode": cfg.get("mode", "unknown"),
        "admin_enabled": cfg.get("allow_admin", False)
    }

if __name__ == "__main__":
    print(handler())