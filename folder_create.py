import subprocess
subprocess.call('netsh wlan show drivers',shell=True)
wifi_name = "s_wifi"
wifi_password = "abcdefghijk"
subprocess.call(f"netsh wlan set hostednetwork mode=allow ssid={wifi_name} key={wifi_password}",shell=True)
subprocess.call("netsh wlan start hostednetwork",shell=True)