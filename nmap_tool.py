from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type

import nmap

class NmapInput(BaseModel):
  ip: str  =  Field(..., description="IP address from host")

class NmapTool(BaseTool):
  """
    Nmap Tool
  """
  name: str = "Nmap Scan Tool"
  args_schema: Type[BaseModel] = NmapInput
  description: str = "Performs a basic Nmap scan on a IP"
  
  def _execute(self, ip: str = "127.0.0.1"):
    output = self.scan()
    return output + ip

  def scan(self):
    nm = nmap.PortScanner()
    scan_args = '-F'
    target_ip = self.get_tool_config('IP')
    result = nm.scan(target_ip, arguments=scan_args)
    print(result)
    return result
