import subprocess
import json

def detect_drives():
    try:
        result = subprocess.run(
            ["lsblk","-j","-o","NAME","SIZE","TYPE"],
            capture_output=True,
            text=True,
            check=True
        )
        data = json.loads(result.stdout)

        drives=[]
        for device in data["blockdevices"]:
            drives.append({
                "name": device["name"],
                "size": device["size"],
                "type": device["type"]
            })
        return drives
    except Exception as e:
        print("Error detecting drives:",e)
        return []
if__name__=="__main__":
    drives = detect_drives()
    for d in drives:
      print(d)