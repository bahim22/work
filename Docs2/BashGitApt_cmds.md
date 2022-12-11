
# General cmds for apt in Ubu

```sh
    apt [-h] [-o=config_string] [-c=config_file] [-t=target_release]                       [-a=architecture] {list | search | show | update | install pkg[{=pkg_version_number | /target_release}]... | remove pkg...  | upgrade | full-upgrade | edit-sources | {-v --version} |{-h--help}}                                                         DESCRIPTION                                                                                          apt provides a high-level commandline interface for the package management                    system. It is intended as an end user interface and enables some options                      better suited for interactive usage by default compared to more                               specialized APT tools like apt-get(8) and apt-cache(8).                                                                                                                                     Much like apt itself, its manpage is intended as an end user interface and                    as such only mentions the most used commands and options partly to not                        duplicate information in multiple places and partly to avoid overwhelming                     readers with a cornucopia of options and details.    

    update (apt-get(8))                                                                               update is used to download package information from all configured                            sources. Other commands operate on this data to e.g. perform package                          upgrades or search in and display details about all packages available                        for installation.                                                                                                                                                                       upgrade (apt-get(8))                                                                              upgrade is used to install available upgrades of all packages                                 currently installed on the system from the sources configured via                             sources.list(5). New packages will be installed if required to satisfy                        dependencies, but existing packages will never be removed. If an                              upgrade for a package requires the removal of an installed package the                        upgrade for this package isn't performed.                                                                                                                                               full-upgrade (apt-get(8))                                                                         full-upgrade performs the function of upgrade but will remove                                 currently installed packages if this is needed to upgrade the system                          as a whole.                                                                                                                                                                             install, reinstall, remove, purge (apt-get(8))                                                    Performs the requested action on one or more packages specified via                           regex(7), glob(7) or exact match. The requested action can be                                 overridden for specific packages by appending a plus (+) to the                               package name to install this package or a minus (-) to remove it.                                                                                                                           A specific version of a package can be selected for installation by                           following the package name with an equals (=) and the version of the                          package to select. Alternatively the version from a specific release                          can be selected by following the package name with a forward slash (/)                        and codename (buster, bullseye, sid ...) or suite name (stable,                               testing, unstable). This will also select versions from this release                          for dependencies of this package if needed to satisfy the request.                                                                                                                          Removing a package removes all packaged data, but leaves usually small                        (modified) user configuration files behind, in case the remove was an                         accident. Just issuing an installation request for the accidentally                           removed package will restore its function as before in that case. On                          the other hand you can get rid of these leftovers by calling purge                            even on already removed packages. Note that this does not affect any                          data or configuration stored in your home directory.                                                                                                                                    autoremove (apt-get(8))                                                                           autoremove is used to remove packages that were automatically                                 installed to satisfy dependencies for other packages and are now no                           longer needed as dependencies changed or the package(s) needing them                          were removed in the meantime.                                                                                                                                                               You should check that the list does not include applications you have                         grown to like even though they were once installed just as a                                  dependency of another package. You can mark such a package as manually                        installed by using apt-mark(8). Packages which you have installed                             explicitly via install are also never proposed for automatic removal.                                                                                                                   satisfy (apt-get(8))                                                                              satisfy satisfies dependency strings, as used in Build-Depends. It                            also handles conflicts, by prefixing an argument with "Conflicts: ".                                                                                                                        Example: apt satisfy "foo, bar (>= 1.0)" "Conflicts: baz, fuzz"  

            search (apt-cache(8))                                                                             search can be used to search for the given regex(7) term(s) in the                            list of available packages and display matches. This can e.g. be                              useful if you are looking for packages having a specific feature. If                          you are looking for a package including a specific file try apt-                              file(1).                                                                                                                                                                                show (apt-cache(8))                                                                               Show information about the given package(s) including its                                     dependencies, installation and download size, sources the package is                          available from, the description of the packages content and much more.                        It can e.g. be helpful to look at this information before allowing                            apt(8) to remove a package or while searching for new packages to                             install.                                                                                                                                                                                list                                                                                              list is somewhat similar to dpkg-query --list in that it can display a                        list of packages satisfying certain criteria. It supports glob(7)                             patterns for matching package names as well as options to list                                installed (--installed), upgradeable (--upgradeable) or all available                         (--all-versions) versions.                                                                                                                                                              edit-sources (work-in-progress)                                                                   edit-sources lets you edit your sources.list(5) files in your                                 preferred text editor while also providing basic sanity checks. 

                    apt-get(8), apt-cache(8), sources.list(5), apt.conf(5), apt-config(8), The
    APT User's guide in /usr/share/doc/apt-doc/, apt_preferences(5), the APT Howto.
```

## Git

#
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
#

no    Global default
fi    Normal file
di    Directory
ln    Symbolic link.
bd    Block device
cd    Character device
or    Symbolic link to a non-existent file
ex    Executable file
*.extension   Example, *.mp3

# Steps for ssh into git repo

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

## Cmd Info

# Commands

## CMD, PowerShell, Bash, Git, AZ

### CMD

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
