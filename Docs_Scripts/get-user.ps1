# net user /domain $env:USERNAME

Get-ADUser $env:USERNAME -Properties *

Get-ADUser -identity -Identity (Read-Host -Prompt "Enter SamAccountName")
Get-ADUser -identity -Identity (Read-Host -Prompt "Enter SamAccountName") -Properties *

# Get-ADGroup -Identity Administrators -Properties * | Get-Member

# Get-ADDCCloningExcludedApplicationList -GenerateXml -Path 

net user -Identity (Read-Host -Prompt "Enter SamAccountName") -properties *

<# NET USER
[username [password | *] [options]] [/DOMAIN]
         username {password | *} /ADD [options] [/DOMAIN]
         username [/DELETE] [/DOMAIN]
         username [/TIMES:{times | ALL}]
         username [/ACTIVE: {YES | NO}]
#>