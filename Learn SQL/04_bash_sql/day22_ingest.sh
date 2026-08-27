#!/usr/bin/env bash
set -euo pipefail

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DB_FILE="${WORKSPACE_ROOT}/04_bash_sql/pipeline_ingest.db"
DATA_DIR="${WORKSPACE_ROOT}/04_bash_sql/data"
SQLITE_BIN="${WORKSPACE_ROOT}/bin/sqlite3"

mkdir -p "${DATA_DIR}"
RAW_JSON="${DATA_DIR}/api_users.json"
STAGING_CSV="${DATA_DIR}/staging_users.csv"

echo "=================================================="
echo "    DAY 22: STREAMING JSON TO SQL INGESTION       "
echo "=================================================="

# 1. Generate JSON Payload
cat <<EOF > "${RAW_JSON}"
[
  {"id": 501, "username": "alice_ingest", "email": "alice_ingest@data.com", "role": "Engineer"},
  {"id": 502, "username": "bob_ingest", "email": "bob_ingest@data.com", "role": "Architect"},
  {"id": 503, "username": "charlie_ingest", "email": "charlie_ingest@data.com", "role": "Analyst"}
]
EOF

echo "[1] Converting JSON Payload to CSV..."
python3 -c "
import json, csv
with open('${RAW_JSON}') as f:
    data = json.load(f)
with open('${STAGING_CSV}', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'username', 'email', 'role'])
    for r in data:
        writer.writerow([r['id'], r['username'], r['email'], r['role']])
"

echo "[2] Importing CSV Data into Database Table..."
"${SQLITE_BIN}" "${DB_FILE}" "DROP TABLE IF EXISTS ingested_users;"
"${SQLITE_BIN}" "${DB_FILE}" ".import '${STAGING_CSV}' ingested_users"

echo "[3] Ingested Table Records:"
"${SQLITE_BIN}" "${DB_FILE}" "SELECT * FROM ingested_users;"

echo "--------------------------------------------------"
echo "✅ DAY 22 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
