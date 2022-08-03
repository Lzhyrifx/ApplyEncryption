set ws=WScript.CreateObject("WScript.Shell")
ws.Run "C:\Users\Lzhyrifx\AppData\Command\Python\kill.py",0
set ws=WScript.CreateObject("WScript.Shell")
ws.Run "C:\Users\Lzhyrifx\AppData\Command\Start\Bandizip.vbs",0
WScript.sleep 5000
Set ws = CreateObject("WScript.Shell")
ws.Run "C:\Users\Lzhyrifx\AppData\Command\Error\Wmic\Bandizip.bat",0