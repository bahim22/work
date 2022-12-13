
# General cmds for apt in Ubu

## Steps for ssh git repo

ssh connects and logs into the specified destination in the form for user, hostname and port:

```sh
[user@]hostname
ssh://[user@]hostname[:port]
ssh -i ~/.ssh/id_ed25519 # identity file (private key)
ssh -l login_name -p port
ssh-keygen -l -f /etc/ssh/ssh_host_rsa_key # determine fingerprints
ssh-keygen -lv -f ~/.ssh/known_hosts #ls fingerpritns and random art for known hosts
ssh-keygen -r host.example.com. # connect client to server and SSHFP resource records should be added to the zonefile for host first
dig -t SSHFP host.example.com check that zone is answering fingerprint querires.
ssh -o "VerifyHostKeyDNS ask" host.example.com # client connects

```

### Steps for keygen

The user creates his/her key pair by running ssh-keygen(1). This stores the pri‐vate key in ~/.ssh/id_dsa (DSA), ~/.ssh/id_ecdsa (ECDSA), ~/.ssh/id_ecdsa_sk (au‐thenticator-hosted ECDSA), ~/.ssh/id_ed25519 (Ed25519), ~/.ssh/id_ed25519_sk (au‐
thenticator-hosted Ed25519), or ~/.ssh/id_rsa (RSA) and stores the public key in
~/.ssh/id_dsa.pub (DSA), ~/.ssh/id_ecdsa.pub (ECDSA), ~/.ssh/id_ecdsa_sk.pub (au‐
thenticator-hosted ECDSA), ~/.ssh/id_ed25519.pub (Ed25519),
~/.ssh/id_ed25519_sk.pub (authenticator-hosted Ed25519), or ~/.ssh/id_rsa.pub (RSA) in the user's home directory.The user should then copy the public key to
~/.ssh/authorized_keys in his/her home directory on the remote machine.  The
authorized_keys file corresponds to the conventional ~/.rhosts file, and has one
key per line, though the lines can be very long.  After this, the user can log in
without giving the password.

### Example ssh connect

The following example would connect client network 10.0.99.0/24 using a point-to-point connection from 10.1.1.1 to 10.1.1.2, provided that the SSH server running on the gateway to the remote network, at 192.168.1.15, allows it.

```sh
# On the client:

ssh -f -w 0:1 192.168.1.15 true
ifconfig tun0 10.1.1.1 10.1.1.2 netmask 255.255.255.252
route add 10.0.99.0/24 10.1.1.2

# On the server:

ifconfig tun1 10.1.1.2 10.1.1.1 netmask 255.255.255.252
route add 10.0.50.0/24 10.1.1.1

# Client access may be more finely tuned via the /root/.ssh/authorized_keys file (see below) and the PermitRootLogin server option.  The following entry would permit connections on tun(4) device 1 from user “jane” and on tun device 2 from user “john”, if PermitRootLogin is set to “forced-commands-only”:

tunnel="1",command="sh /etc/netstart tun1" ssh-rsa ... jane
tunnel="2",command="sh /etc/netstart tun2" ssh-rsa ... john
```

```sh
# edit git config f
git config --global user.name <username>
git config --global user.email <email@mail.com>
ls -al ~/.ssh # list files in .ssh dir
ssh-keygen -t ed25519 -C "email@google.com"
# enter passphrase to use && this creates pub/priv key pair
#  saves to .ssh/id_ed25519 & ''.pub; generates key fingerprint and randomart image
eval "$(ssh-agent -s)" #check if agent is running
ssh-add ~/.ssh/id_ed25519 #add id to ~
cat ~/.ssh/id_ed25519.pub # display pub key then c/v to github acct
ssh -T git@github.com # test connection & clone repo
git clone git@github.com:<username>/<repo>.git
code .
git clone ssh://git@ssh.github.com:443/bahim22/work.git
```

## Apt DESCRIPTION

```sh
    apt [-h] [-o=config_string] [-c=config_file] [-t=target_release] [-a=architecture]
        {list | search | show | update | install pkg[{=pkg_ver_number | /target_release}]... | remove pkg... | upgrade | full-upgrade | edit-sources | {-v --version} |{-h--help}}
```

> apt provides a high-level commandline interface for the package management  system.
>> can also use more advanced apt-get(8) and apt-cache(8)

- `update` (apt-get(8)) update is used to download package information from all configured sources. Other commands operate on this data to e.g. perform package upgrades or search in and display details about all packages available for installation
- `upgrade` (apt-get(8)) upgrade is used to install available upgrades of all packages   currently installed on the system from the sources configured via  sources.list(5). New packages will be installed if required to satisfy dependencies, but existing packages will never be removed. If an upgrade for a package requires the removal of an installed package the upgrade for this package isn\'t performed.
- `full-upgrade`: performs the function of upgrade but will remove currently installed packages if this is needed to upgrade the system as a whole.
- `install, reinstall, remove, purge`: Performs the requested action on one or more packages specified via regex(7), glob(7) or exact match. The requested action can be overridden for specific packages by appending a plus (+) to the package name to install this package or a minus (-) to remove it. A specific version of a package can be selected for installation by following the package name with an equals (=) and the version of the package to select. Alternatively the version from a specific release can be selected by following the package name with a forward slash (/) and codename (buster, bullseye, sid ...) or suite name (stable,testing, unstable). This will also select versions from this release for dependencies of this package if needed to satisfy the request. Removing a package removes all packaged data, but leaves usually small (modified) user configuration files behind, in case the remove was an accident. Just issuing an installation request for the accidentally removed package will restore its function as before in that case. On the other hand you can get rid of these leftovers by calling purge even on already removed packages. Note that this does not affect any data or configuration stored in your home directory.
- `autoremove` is used to remove packages that were automatically installed to satisfy dependencies for other packages and are now no longer needed as dependencies changed or the package(s) needing them were removed in the meantime. You should check that the list does not include applications you have grown to like even though they were once installed just as a dependency of another package. You can mark such a package as manually installed by using apt-mark(8). Packages which you have installed explicitly via install are also never proposed for automatic removal.
- `satisfy`: satisfies dependency strings, as used in Build-Depends. It                            also handles conflicts, by prefixing an argument with "Conflicts: ".
- `search`: can be used to search for the given regex(7) term(s) in the list of available packages and display matches. This can e.g. be useful if you are looking for packages having a specific feature. If you are looking for a package including a specific file try apt-file.
- `show`: information about the given package(s) including its dependencies, installation and download size, sources the package is available from, the description of the packages content and much more. It can e.g. be helpful to look at this information before allowing                            apt(8) to remove a package or while searching for new packages to install.
- `list`: is somewhat similar to dpkg-query --list in that it can display a list of packages satisfying certain criteria. It supports glob(7) patterns for matching package names as well as options to list installed (--installed), upgradeable (--upgradeable) or all available (--all-versions) versions.
- `edit-sources`: lets you edit your sources.list(5) files in your preferred text editor while also providing basic sanity checks.
- Also view apt-get, apt-cache, sources.list, apt.conf, apt-config

___

## Git

## git colors for terminal

31  = red 40  = black background  0   = default colour
32  = green   41  = red background    1   = bold
33  = orange  42  = green background  4   = underlined
34  = blue    43  = orange background 5   = flashing text
35  = purple  44  = blue background   7   = reverse field > (exchange foreground and background color)
36  = cyan    45  = purple background 8   = concealed (invisible)
37  = grey    46  = cyan background   0   = default colour
90  = dark grey   47  = grey background   1   = bold
91  = light red   100 = dark grey background
92  = light green 101 = light red background
93  = yellow  102 = light green background
94  = light blue  103 = yellow background
95  = light purple    104 = light blue background
96  = turquoise   105 = light purple background
97  = white   106 = turquoise background
107 = white background

## symbolic rep of data

no    Global default
fi    Normal file
di    Directory
ln    Symbolic link.
bd    Block device
cd    Character device
or    Symbolic link to a non-existent file
ex    Executable file
**.extension  (ex: *.mp3)

## Cmd Info

### Windows CMD

`BCDEDIT`        Sets properties in boot database to control boot loading.
`CACLS`          Displays or modifies access control lists (ACLs) of files.
`CD`             Displays the name of or changes the current directory.
`CHDIR`          Displays the name of or changes the current directory.
`CHKDSK`         Checks a disk and displays a status report.
`CLS`            Clears the screen.
`CONVERT`        Converts FAT volumes to NTFS. Can't convert current drive
`COPY`           Copies one or more files to another location.
`DATE`           Displays or sets the date.
`DEL`            Deletes one or more files.
`DIR`            Displays a list of files and subdirectories in a directory.
`DISKPART`       Displays or configures Disk Partition properties.
`ECHO`           Displays messages, or turns command echoing on or off.
`ERASE`          Deletes one or more files.
`FIND`           Searches for a text string in a file or files.
`FINDSTR`        Searches for strings in files.
`FORMAT`         Formats a disk for use with Windows.
`FSUTIL`         Displays or configures the file system properties.
`FTYPE`          Displays/modifies file types used in file ext assoc.
`GPRESULT`       Displays Group Policy information for machine or user.
`HELP`           Provides Help information for Windows commands.
`ICACLS`         Display, modify, backup, or restore ACLs for files and dir.
`MD`             Creates a directory.
`MKDIR`          Creates a directory.
`MKLINK`         Creates Symbolic Links and Hard Links
`MODE`           Configures a system device.
`MOVE`           Moves one or more files from one directory to another dir.
`PRINT`          Prints a text file.
`RD`             Removes a directory.
`RECOVER`        Recovers readable information from a bad or defective disk.
`REN`            Renames a file or files.
`RENAME`         Renames a file or files.
`RMDIR`          Removes a directory.
`ROBOCOPY`       Advanced utility to copy files and directory trees
`SCHTASKS`       Schedules commands and programs to run on a computer.
`SHUTDOWN`       Allows proper local or remote shutdown of machine.
`SYSTEMINFO`     Displays machine specific properties and configuration.
`TASKLIST`       Displays all currently running tasks including services.
`TASKKILL`       Kill or stop a running process or application.
`TREE`           Graphically displays the dir structure of a drive or path
`VOL`            Displays a disk volume label and serial number.
`XCOPY`          Copies files and directory trees.
