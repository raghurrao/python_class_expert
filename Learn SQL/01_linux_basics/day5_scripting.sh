#!/usr/bin/env bash
# Day 5: Production-grade Shell Scripting with Traps and Logging

set -euo pipefail

WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"
DATA_DIR="${WORKSPACE_ROOT}/01_linux_basics/sample_data"
mkdir -p "${DATA_DIR}"

LOG_FILE="${DATA_DIR}/etl_pipeline.log"
TEMP_FILE=$(mktemp "${DATA_DIR}/temp_data_XXXXXX.tmp")

# Helper function for logging
log_info() {
    local msg="[$(date '+%Y-%m-%d %H:%M:%S')] [INFO] $1"
    echo "${msg}"
    echo "${msg}" >> "${LOG_FILE}"
}

# Trap cleanup function
cleanup() {
    log_info "Executing exit trap: Removing temporary file '${TEMP_FILE}'"
    rm -f "${TEMP_FILE}"
}
trap cleanup EXIT

echo "=================================================="
echo "    DAY 5: PRODUCTION SHELL PIPELINE PATTERNS     "
echo "=================================================="

log_info "Pipeline Execution Started."
log_info "Created temp workspace file: ${TEMP_FILE}"

# Simulate ETL extraction phase
log_info "Step 1: Simulating data extraction..."
cat <<EOF > "${TEMP_FILE}"
user_id,username,status
1,alice_data,ACTIVE
2,bob_admin,INACTIVE
3,charlie_sql,ACTIVE
EOF

# Process data
ACTIVE_COUNT=$(grep -c "ACTIVE" "${TEMP_FILE}" || true)
log_info "Step 2: Processing completed. Active users found: ${ACTIVE_COUNT}"

log_info "Pipeline Execution Completed Successfully."
echo "--------------------------------------------------"
echo "✅ DAY 5 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
