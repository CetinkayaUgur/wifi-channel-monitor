import CoreWLAN

def scan_wifi_networks():
    client = CoreWLAN.CWWiFiClient.sharedWiFiClient()
    iface = client.interface()
    networks, error = iface.scanForNetworksWithName_error_(None, None)

    if error:
        print(f"Error scanning networks: {error}")
        return []

    results = []
    for net in networks:
        bssid = net.bssid()
        if bssid is None:
            bssid = "<Hidden BSSID>"
        ssid = net.ssid()
        if ssid is None:
            ssid = "<Hidden SSID>"
        rssi = net.rssiValue()
        channel = net.wlanChannel().channelNumber()
        results.append({"SSID": ssid, "BSSID": bssid, "RSSI": rssi, "Channel": channel})
    return results

if __name__ == "__main__":
    networks = scan_wifi_networks()
    for net in networks:
        print(f'SSID: {net["SSID"]}, BSSID: {net["BSSID"]}, RSSI: {net["RSSI"]}, Channel: {net["Channel"]}')