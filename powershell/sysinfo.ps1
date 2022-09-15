function getIP{(get-netipaddress).ipv4address | Select-String "192*"}
write-host(getIP)
$IP = getIP
function getUser{(Get-LocalUser).Name | Select-String "Adm*"}
Write-Host(getUser)
$User = getUser
$Hostname = "linhc-win"
function getVersion{(Get-Host).Version | Select-String "5.1*"}
write-host(getVersion)
$Version = getVersion
function getDate{(Get-Date).DateTime}
Write-Host(getDate)
$Date = getDate
Write-Host("This machine's IP is $IP. User is $User. Hostname is $Hostname. PowerShell Version $Version. Today's Date is $Date.")