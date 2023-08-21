from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from nmap_tool import NmapTool

class NmapToolkit(BaseToolkit, ABC):

  name: str = "Nmap Toolkit"
  description: str = "Toolkit for Sapeo  Nmap network scanning"

  def get_tools(self) -> List[BaseTool]:
     return [NmapTool()]

  def get_env_keys(self) -> List[str]:
     return ["IP"] 
