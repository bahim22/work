 <#
 $R = Invoke-WebRequest -uri https://www.google.com?q=pointpark+university

 $R.AllElements | Where-Object {
 $_.name -like "* Value"
 -and $_.tagName -eq "INPUT" 
 } | Select-Object Name, Value

 #>

  $R = Invoke-WebRequest -uri https://www.google.com?q=pointpark+university

 $R.AllElements | Where-Object {
 $_.name -like "* Value"
 -and $_.tagName -eq "INPUT" 
 } | Select-Object Name, Value