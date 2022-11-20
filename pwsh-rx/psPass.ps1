$user = (Read-Host "Enter AD SamAccountName");
$newPassword = (Read-Host -Prompt "Provide New Password" -AsSecureString);
    Set-ADAccountPassword -identity $user -NewPassword $newPassword -Reset
   

   <# $newPassword = (Read-Host -Prompt "Provide new Password"  -AsSecureString); 

    Set-ADAccountPassword -identity $user -NewPassword $newPassword -Reset

    #Get-ADUser -Identity $user | Set-ADAccountPassword 
    #>
    