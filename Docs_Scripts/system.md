# System Admin, Config, Install and Maintainence.

## VM

1. create VM in AZ
2. choose image
3. select connection type and create key
4. save private key on local system and chmod 400 keyname.pem

## Remote machine

When each user logs in, they generate instances of Firewall Rules for all the various services, like Cortana, Xbox, etc, and they remain when the user logs out. If the same user logs in, it generates these rules again, creating a problem where the firewall rules are bogging down the machine performance.

- when users login to terminal server, Firewall Rules instances are generated for services (Cortana, Xbox, ...). These rules remain upon logout and are regenerated upon login, which hinders PC performance.
- Solution:
  - create registry key to delete instances on logout
    - batch file in SCCM drive: `Scripts\TerminalServerRegKey-ProfileFix`
      - REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy" /t REG_DWORD /v DeleteUserAppContainersOnLogoff /d 1 /f
  - run pwsh script to remove stale firewall rule instances (this can also be used to fix broken start menu and software reinstall issues)
    - Scripts dir: `TerminalServerFirewallFix` && `Scripts\TerminalServerSearchBarFix`

### MacOS Jamf

```sh
hostname=$1
su casper # switches user; prompts for passwrd

sudo jamf recon # forces the machine to check into Jamf and pick up undeployed policies

sudo profiles renew -type enrollment

This forces the machine to renew the MDM profile, if for some reason it has not done so automatically as it is supposed to.

sudo jamf policy -trigger $trigger

# runs specific policy, (if setup w/ a trigger). Policy name is in Jamf; use to force imaging scripts, trigger installs, push config profile...

sudo jamf policy -trigger installOffice365 # Calls the Office 365 install policy

sudo scutil --set Hostname $hostname

sudo scutil --set ComputerName $hostname

sudo scutil --set LocalHostName $hostname # create new PC name from terminal w/ 3 cmds

sudo scutil --set Hostname pc-hostname-02

sudo jamf enroll -prompt
```

- This forces a machine to start enrollment, after entering the credentials in for the prompts.
- Done for many reasons, but mainly after a recon gets an error mentioning a Device Signature Error, which requires re-enrollment
  - forcing an enroll this way will run all policies that trigger on Enrollment Complete, including imaging scripts.
  - May display a pop-up similar to one during new machine imaging, w/ error alert, but it can be disregarded and killed via Activity Monitor kill DEPNotify.
