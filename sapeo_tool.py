from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel

import nmap

class SapeoInput(BaseModel):
  ip: str =  Field(..., description="Analisis de los resultados")

class SapeoTool(BaseTool):

  name = "Nmap Scan Tool"
  description = "Performs a basic Nmap scan on an IP"
  args_schema = SapeoInput
  
  def _execute(self, ip: str):
    
    nm = nmap.PortScanner()
    scan_args = '-Pn -sV'
    target_ip =self.get_tool_config('IP')
    print(target_ip)
    result = nm.scan(target_ip, arguments=scan_args)
    print(result)
    # Process results

    return result
