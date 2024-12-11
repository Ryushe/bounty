#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ ! -d "$SCRIPT_DIR/venv" ]]; then
  echo "creating venv"
  python -m venv venv
  pip install -r $SCRIPT_DIR/requirements.txt
fi
echo script is in: $SCRIPT_DIR
echo "Sourcing the virtual env"
source $SCRIPT_DIR/venv/bin/activate
echo "running app"
python $SCRIPT_DIR/loxs.py

 
