import platform
import psutil
import subprocess
import os


def get_windows_hardware_info():
    try:
        import wmi
    except ImportError:
        print("wmi module is required for detailed hardware info on Windows. Install it using 'pip install WMI'.")
        return {}

    c = wmi.WMI()

    info = {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": psutil.cpu_count(logical=False),
        "cpu_count_logical": psutil.cpu_count(logical=True),
        "memory": psutil.virtual_memory(),
        "disks": psutil.disk_partitions(),
        "gpu": [gpu.Name for gpu in c.Win32_VideoController()],
        "network": [net.Description for net in c.Win32_NetworkAdapter() if net.NetEnabled]
    }

    return info


def get_linux_hardware_info():
    info = {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": psutil.cpu_count(logical=False),
        "cpu_count_logical": psutil.cpu_count(logical=True),
        "memory": psutil.virtual_memory(),
        "disks": psutil.disk_partitions(),
        "gpu": None,
        "network": None
    }

    try:
        with open("/proc/cpuinfo") as f:
            info["cpu_info"] = f.read()
    except FileNotFoundError:
        info["cpu_info"] = "Not available"

    try:
        with open("/proc/meminfo") as f:
            info["mem_info"] = f.read()
    except FileNotFoundError:
        info["mem_info"] = "Not available"

    try:
        with open("/sys/class/dmi/id/board_name") as f:
            info["motherboard"] = f.read().strip()
    except FileNotFoundError:
        info["motherboard"] = "Not available"

    try:
        lspci_output = subprocess.check_output(["lspci"]).decode()
        info["gpu"] = [line for line in lspci_output.split('\n') if 'VGA' in line or '3D' in line]
    except (FileNotFoundError, subprocess.CalledProcessError):
        info["gpu"] = "Not available"

    try:
        info["network"] = subprocess.check_output(["ifconfig"]).decode()
    except (FileNotFoundError, subprocess.CalledProcessError):
        info["network"] = "Not available"

    return info


def get_mac_hardware_info():
    info = {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": psutil.cpu_count(logical=False),
        "cpu_count_logical": psutil.cpu_count(logical=True),
        "memory": psutil.virtual_memory(),
        "disks": psutil.disk_partitions(),
        "gpu": None,
        "network": None
    }

    try:
        system_profiler = subprocess.run(["system_profiler", "SPHardwareDataType"], capture_output=True, text=True)
        info["system_profiler"] = system_profiler.stdout
    except FileNotFoundError:
        info["system_profiler"] = "Not available"

    try:
        gpu_info = subprocess.run(["system_profiler", "SPDisplaysDataType"], capture_output=True, text=True)
        info["gpu"] = gpu_info.stdout
    except FileNotFoundError:
        info["gpu"] = "Not available"

    try:
        network_info = subprocess.run(["networksetup", "-listallhardwareports"], capture_output=True, text=True)
        info["network"] = network_info.stdout
    except FileNotFoundError:
        info["network"] = "Not available"

    return info


def get_hardware_info():
    current_platform = platform.system().lower()
    if current_platform == "windows":
        return get_windows_hardware_info()
    elif current_platform == "linux":
        return get_linux_hardware_info()
    elif current_platform == "darwin":  # macOS is identified as 'Darwin'
        return get_mac_hardware_info()
    else:
        return {"error": "Unsupported platform"}


if __name__ == "__main__":
    hardware_info = get_hardware_info()
    for key, value in hardware_info.items():
        print(f"{key}: {value}")
