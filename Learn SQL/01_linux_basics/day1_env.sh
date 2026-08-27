#!/usr/bin/env bash
# Day 1: Hands-on Shell Navigation & Environment Script

set -e # Exit immediately if a command exits with a non-zero status

echo "=================================================="
echo "      DAY 1: LINUX TERMINAL FOUNDATIONS          "
echo "=================================================="

# 1. Print current working directory
CURRENT_DIR=$(pwd)
echo "[1] Current Directory: ${CURRENT_DIR}"

# 2. Export Database Environment Variables
export LEARNING_ENV="Linux_SQL_Masterclass"
export DB_ENGINE="SQLite3"
export WORKSPACE_ROOT="/home/raghurao/Learnings/Learn SQL"

echo "[2] Exported Environment Variables:"
echo "    - LEARNING_ENV: ${LEARNING_ENV}"
echo "    - DB_ENGINE: ${DB_ENGINE}"
echo "    - WORKSPACE_ROOT: ${WORKSPACE_ROOT}"

# 3. Create a sample data directory structure
echo "[3] Setting up directory tree..."
mkdir -p "${WORKSPACE_ROOT}/01_linux_basics/sample_data"

# 4. Create a sample config file with environment values
CONFIG_FILE="${WORKSPACE_ROOT}/01_linux_basics/sample_data/db_config.env"
cat <<EOF > "${CONFIG_FILE}"
# Auto-generated DB Configuration
DB_ENGINE=${DB_ENGINE}
LEARNING_ENV=${LEARNING_ENV}
CREATED_AT=$(date '+%Y-%m-%d %H:%M:%S')
EOF

echo "[4] Created configuration file: ${CONFIG_FILE}"
cat "${CONFIG_FILE}"

echo "--------------------------------------------------"
echo "✅ DAY 1 EXERCISE COMPLETED SUCCESSFULLY!"
echo "=================================================="
