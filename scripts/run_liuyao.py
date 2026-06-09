#!/usr/bin/env python3
"""Wrapper: run liuyao_pan.py with auto-venv support."""
import sys
import os
from pathlib import Path

SKILLS_DIR = Path(__file__).resolve().parent.parent
VENV_DIR = SKILLS_DIR / "scripts" / ".venv"

# Auto-create venv and install deps if needed
if not VENV_DIR.exists():
    import subprocess
    print("🔧 首次运行，自动创建虚拟环境...")
    subprocess.check_call([sys.executable, "-m", "venv", str(VENV_DIR)])
    pip = str(VENV_DIR / "bin" / "pip")
    req = SKILLS_DIR / "requirements.txt"
    if req.exists():
        subprocess.check_call([pip, "install", "-r", str(req)])
    print("✅ 虚拟环境就绪\n")

# Add venv site-packages to path
site_dir = VENV_DIR / "lib"
for d in site_dir.iterdir():
    sp = d / "site-packages"
    if sp.is_dir():
        sys.path.insert(0, str(sp))
        break

sys.path.insert(0, str(SKILLS_DIR / "liuyao" / "scripts"))

from liuyao_pan import main
main()
