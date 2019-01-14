import subprocess

subprocess.call("adb devices")
subprocess.call("adb help")
subprocess.call("adb install -r Resources/Wifi.Analyzer.v.3.11.2.b.139.MultiPatch.apk")
input()
