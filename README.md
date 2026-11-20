# CHANGEWISE Demo Repository

A tiny Python micro‑service that reads a JSON configuration file.
The second commit adds an “admin” configuration and modifies the code to
load it automatically – this is the change the CHANGEWISE MVP will
detect as a privileged‑access violation.

Only the `service/` package and `config.json` are version‑controlled.
Policy documents are stored in IBM Cloud Object Storage and are used by
the MVP ingestion job.