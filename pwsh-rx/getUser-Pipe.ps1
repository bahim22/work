# Prompt for user info and pipe through to Get-ADUser command

$user = (Read-Host -Prompt "Enter AD SamAccountName"); Get-ADUser -Identity $user;

Write-Output "ibalde" | Get-ADUserResultantPasswordPolicy

<# 

Get-childitem: The `Get-ChildItem` cmdlet gets the items in one or more specified locations. 
If the item is a container, it gets the items inside the container, known as child items. 

#>

Get-ChildItem -Path C:\Users\Ibalde\moon

Get-ChildItem -Path C:\Test\*.txt -Recurse -Force