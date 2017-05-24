
"""
客户端接口
"""

import os,sys


dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, dir)

from core import main

if __name__ == "__main__":
    main.run()
