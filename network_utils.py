import subprocess
import sys

def connect_to_drone_wifi(ssid):
    """
    Attempts to connect to the specified Wi-Fi network (drone's network).

    This function uses system-specific commands to connect to the given Wi-Fi network.
    It supports macOS and Windows operating systems.

    Args:
        ssid (str): The SSID (name) of the Wi-Fi network to connect to.

    Returns:
        bool: True if the connection was successful, False otherwise.

    Raises:
        subprocess.CalledProcessError: If the system command to connect fails.

    Note:
        For unsupported operating systems, it will print a message asking the user
        to connect manually and return False.
    """
    try:
        if sys.platform == "darwin":  # macOS
            subprocess.run(["networksetup", "-setairportnetwork", "en0", ssid], check=True)
        elif sys.platform == "win32":  # Windows
            subprocess.run(["netsh", "wlan", "connect", "name=" + ssid], check=True)
        else:
            print("Unsupported operating system. Please connect to the drone's Wi-Fi manually.")
            return False
        print(f"Successfully connected to {ssid}")
        return True
    except subprocess.CalledProcessError:
        print(f"Failed to connect to {ssid}. Please check the SSID and try again.")
        return False
