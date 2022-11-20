# reset password
<#
$user = Get-ADUser 
 $newPassword = (Read-Host -Prompt "Provide New Password" 
    -AsSecureString); Set-ADAccountPassword -Identity userName -NewPassword $newPassword -Reset
 
 Set-ADAccountPassword -Identity $user -OldPassword 
    (ConvertTo-SecureString -AsPlainText "p@ssw0rd" -Force) -NewPassword 
    (ConvertTo-SecureString -AsPlainText "qwert@12345" -Force)

Set-ADAccountPassword 'CN=last first,OU=Accounts,DC=Fabri,DC=com' -Reset -NewPassword (ConvertTo-SecureString -AsPlainText "p@ssw0rd" -Force)

Set-ADAccountPassword 'CN=last first,OU=Accounts,DC=Fabrik,DC=com' -Reset -NewPassword (ConvertTo-SecureString -AsPlainText "p@ssw0rd" -Force)

PS C:\WINDOWS\system32> Search-adaccount -LockedOut | FT Name, ObjectClass -AutoSize

Set-ADAccountPassword -Identity (Read-Host -Prompt "Enter SamAccountName") -NewPassword $newPassword -Reset

Set-ADAccountPassword 'ha-ibalde' -Reset -NewPassword (ConvertTo-SecureString -AsPlainText "p@ssw0rd" -Force)
#>


Set-ADAccountPassword -Identity (Read-Host -Prompt "Enter SamAccountName") -NewPassword (Read-Host -Prompt "Provide new Password" -AsSecureString) -Reset
 
<#

$user = (Read-Host "Enter AD SamAccountName");
$newPassword = (Read-Host -Prompt "Provide New Password" -AsSecureString);
    

    $newPassword = (Read-Host -Prompt "Provide new Password"  -AsSecureString); 

    Set-ADAccountPassword -identity $user -NewPassword $newPassword -Reset

    Get-ADUser -Identity $user | Set-ADAccountPassword 
#>