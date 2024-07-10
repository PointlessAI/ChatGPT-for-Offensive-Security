# python script provide os information

import platform
import os
import psutil

def get_os_information():
    info = {}
    
    # General OS information
    info['System'] = platform.system()
    info['Node Name'] = platform.node()
    info['Release'] = platform.release()
    info['Version'] = platform.version()
    info['Machine'] = platform.machine()
    info['Processor'] = platform.processor()
    info['Architecture'] = platform.architecture()
    
    # Change PWD to ../../../
    current_pwd = os.getcwd()
    new_pwd = os.path.abspath(os.path.join(current_pwd, "../../../"))
    os.chdir(new_pwd)
    info['PWD'] = new_pwd
    
    # Environment variables
    info['Environment Variables'] = dict(os.environ)
    
    # CPU information
    info['CPU Count'] = psutil.cpu_count(logical=True)
    info['CPU Physical Cores'] = psutil.cpu_count(logical=False)
    info['CPU Frequency'] = psutil.cpu_freq()._asdict()
    info['CPU Times'] = psutil.cpu_times()._asdict()
    
    # Memory information
    virtual_mem = psutil.virtual_memory()._asdict()
    swap_mem = psutil.swap_memory()._asdict()
    info['Virtual Memory'] = virtual_mem
    info['Swap Memory'] = swap_mem
    
    # Disk information
    info['Disk Partitions'] = [disk._asdict() for disk in psutil.disk_partitions()]
    info['Disk Usage'] = {part.mountpoint: psutil.disk_usage(part.mountpoint)._asdict() for part in psutil.disk_partitions()}
    
    # Network information
    info['Network Interfaces'] = {iface: addrs for iface, addrs in psutil.net_if_addrs().items()}
    info['Network Connections'] = [conn._asdict() for conn in psutil.net_connections()]
    
    return info

# Get OS information
os_info = get_os_information()
os_info