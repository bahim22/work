$a= "Provide path for list of user in txt doc"
foreach($b in $a){
$g= get-aduser -Identity $b -Properties Name,pwdlastset
$date= [datetime]$g.pwdLastSet
$pwdlast = $date.AddYears(1600).ToLocalTime()
"$b,$pwdlast"}

# export info to csv f
Get-adcomputer -properties * -filter * |export-csv "give path"