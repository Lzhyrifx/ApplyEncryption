WScript.sleep 120000
Set ws = CreateObject("WScript.Shell")
ws.Run "C:\Users\Lzhyrifx\AppData\Command\Shutdown\Wait.vbs",0
do
msgbox "This application has encountered a critical error:"+chr(13)+chr(13)+"ERROR#274(0x47200094)Fatal exception"+chr(13)+chr(13)+"Reason:unknown"+chr(13)+"ProcessID:9528"+chr(13)+"Exception:MEMORY_CRASH"+chr(13)+chr(13)+"The instruction at 0x00004f7c referenced memory at 0x00004f7c" +chr(13)+"The memory could not be executed"+chr(13)+chr(13)+"The computer needs to save abnormal data and then shut down the computer"+chr(13)+"Please wait...",16,"FatalException"
loop
