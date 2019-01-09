import urllib3

http = urllib3.PoolManager()
allSteamApps = http.request("GET", "https://api.steampowered.com/ISteamApps/GetAppList/v2/")

print(allSteamApps.status)
print("=============")
print(allSteamApps.data)
