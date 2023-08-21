# nmap_toolkit.py

from superagi.tools.base_toolkit import BaseToolkit
from sapeo_tool import SapeoTool 

class SapeoToolkit(BaseToolkit):

  name = "Sapeo Toolkit"
  description = "Toolkit for Sapeo  Nmap network scanning"

  def get_tools(self):
     return [
        SapeoScanTool()
     ]

  def get_env_keys(self):
     return [ 
             "IP"
     ] 
