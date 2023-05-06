$color='blue'
Write-Host $color
#condicional if

$serviceName='wuauserv'
$serviceInfo= Get-Service -Name $serviceName
$serviceInfo

if ($serviceInfo.Status -eq "Running")
{
Write-Host $serviceName " esta corriendo"
}

#ciclo

$arreglo = @(1,2,3,4,5,6,7,8,9,10)
foreach($num in $arreglo){
Write-Host $num ","
}