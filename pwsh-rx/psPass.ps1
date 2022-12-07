$user = (Read-Host "Enter AD SamAccountName");
$newPassword = (Read-Host -Prompt "Provide New Password" -AsSecureString);
    Set-ADAccountPassword -identity $user -NewPassword $newPassword -Reset