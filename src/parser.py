import os
import json
from scanner import scan_wifi_networks

def filter_and_sort_networks(networks):
    """
    SSID bilgisi None olmayan tüm ağları al, gizli SSID'leri (<Hidden SSID>) dahil et,
    RSSI değerine göre yüksekten düşüğe sırala.
    """
    filtered = [n for n in networks if n["SSID"] is not None]
    sorted_networks = sorted(filtered, key=lambda n: n["RSSI"], reverse=True)
    return sorted_networks

def save_to_json(data, filename="output/networks.json"):
    os.makedirs("output", exist_ok=True)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    raw_networks = scan_wifi_networks()
    print(f"Found {len(raw_networks)} networks before filtering.")

    cleaned_networks = filter_and_sort_networks(raw_networks)
    print(f"{len(cleaned_networks)} networks after filtering and sorting.")

    for net in cleaned_networks:
        print(f'SSID: {net["SSID"]}, BSSID: {net["BSSID"]}, RSSI: {net["RSSI"]}, Channel: {net["Channel"]}')

    save_to_json(cleaned_networks)