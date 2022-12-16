
# General cmds for apt in Ubu

## Steps for ssh git repo

> ssh connects and logs into the specified destination in the form: user, hostname and port:

```sh
[user@]hostname
ssh://[user@]hostname[:port]
# different format for ssh
ssh://[user@]host.xz[:port]/~[user]/path/to/repo.git/
ssh://[user@]host.xz[:port]/path/to/repo.git/
ssh -i ~/.ssh/id_ed25519 # identity file (private key)
ssh -l login_name -p port
ssh-keygen -l -f /etc/ssh/ssh_host_rsa_key # determine fingerprints
ssh-keygen -lv -f ~/.ssh/known_hosts # ls fingerpritns and random art for known hosts
ssh-keygen -r host.example.com.
# connect client to server; SSHFP resource records should be + to the zonefile for host 1st
dig -t SSHFP host.example.com check that zone is answering fingerprint querires.
ssh -o "VerifyHostKeyDNS ask" host.example.com # client connects
```

### Steps for keygen

- The user creates his/her key pair by running ssh-keygen(1).
  - stores the `private` key in:
    - ~/.ssh/id_dsa (DSA), ~/.ssh/id_ecdsa (ECDSA), ~/.ssh/id_ecdsa_sk (authenticator-hosted ECDSA), ~/.ssh/id_ed25519 (Ed25519), ~/.ssh/id_ed25519_sk (authenticator-hosted Ed25519), or ~/.ssh/id_rsa (RSA)
  - stores the `public` key in the user's home directory w/in subdir of:
    - ~/.ssh/id_dsa.pub (DSA), ~/.ssh/id_ecdsa.pub (ECDSA), ~/.ssh/id_ecdsa_sk.pub (authenticator-hosted ECDSA), ~/.ssh/id_ed25519.pub (Ed25519), ~/.ssh/id_ed25519_sk.pub (authenticator-hosted Ed25519), or ~/.ssh/id_rsa.pub (RSA)
- The user should then copy the public key to ~/.ssh/authorized_keys in his/her home directory on the remote machine.
- The authorized_keys file corresponds to the conventional ~/.rhosts file, and has one
key per line, though the lines can be very long.  After this, the user can log in without giving the password.

### Example ssh connect

> the following example would connect client network 10.0.99.0/24 using a point-to-point connection from 10.1.1.1 to 10.1.1.2
>> provided that the SSH server running on the gateway to the remote network, at 192.168.1.15, allows it

```bash
# On the client:
ssh -f -w 0:1 192.168.1.15 true
ifconfig tun0 10.1.1.1 10.1.1.2 netmask 255.255.255.252
route add 10.0.99.0/24 10.1.1.2

# On the server:
ifconfig tun1 10.1.1.2 10.1.1.1 netmask 255.255.255.252
route add 10.0.50.0/24 10.1.1.1

# Client access may be more finely tuned via the /root/.ssh/authorized_keys file and the PermitRootLogin server option.
# the following entry would permit connections on:
# tun(4) device 1 from user “jane” and on tun device 2 from user “john”, if PermitRootLogin is set to “forced-commands-only”:

tunnel="1",command="sh /etc/netstart tun1" ssh-rsa ... jane
tunnel="2",command="sh /etc/netstart tun2" ssh-rsa ... john
```

___

### initial ssh example

```bash
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

```sh
# Examples from giteveryday help commands

# - Use a tarball as a starting point for a new repository.

tar zxf frotz.tar.gz
cd frotz
git init
git add . (1)
git commit -m "import of frotz source tree."
git tag v2.43 (2)

# 1. add all fi under the cwd.
# 2. make a lightweight, unannotated tag.

# Create a topic branch and develop.

git switch -c alsa-audio (1)
edit/compile/test
git restore curses/ux_audio_oss.c (2)
git add curses/ux_audio_alsa.c (3)
edit/compile/test
git diff HEAD (4)
git commit -a -s (5)
edit/compile/test
git diff HEAD^ (6)
git commit -a --amend (7)
git switch master (8)
git merge alsa-audio (9)
git log --since='3 days ago' (10)
git log v2.43.. curses/ (11)
```

1. create a new topic branch.
2. revert your botched changes in curses/ux_audio_oss.c.
3. you need to tell Git if you added a new file; removal and modification will be caught if you do git commit -a later
4. to see what changes you are committing.
5. commit everything, as you have tested, with your sign-off.
6. look at all your changes including the previous commit.
7. amend the previous commit, adding all your new changes, using original message
8. switch to the master branch.
9. merge a topic branch into your master branch.
10. review commit logs; other forms to limit output can be combined and include -10 (to show up to 10 commits), --until=2005-12-10, etc
11. view only the changes that touch what’s in curses/ directory,
since v2.43 tag.

```sh
# Clone the upstream and work on it. Feed changes to upstream.

git clone git://git.kernel.org/pub/scm/.../torvalds/linux-2.6
my2.6
cd my2.6
git switch -c mine master (1)
edit/compile/test; git commit -a -s (2)
git format-patch master (3)
git send-email --to="person <email@example.com>" 00*.patch (4)
git switch master (5)
git pull (6)
git log -p ORIG_HEAD.. arch/i386 include/asm-i386 (7)
git ls-remote --heads http://git.kernel.org/.../jgarzik/libata
-dev.git (8)
git pull git://git.kernel.org/pub/.../jgarzik/libata-dev.git A
LL (9)
git reset --hard ORIG_HEAD (10)
git gc (11)
```

1. checkout a new branch mine from master.
2. repeat as needed.
3. extract patches from your branch, relative to master,
4. and email them.
5. return to master, ready to see what’s new
6. git pull fetches from origin by default and merges into the current branch.
7. immediately after pulling, look at the changes done upstream since last time we checked, only in the area we are interested in.
8. check the branch names in an external repository (if not known).
9. fetch from a specific branch ALL from a specific repo & merge
10. revert the pull.
11. garbage collect leftover objects from reverted pull.

```sh
# Push into another repository.

# from satellite machine
git clone mothership:frotz frotz (1)
cd frotz
git config --get-regexp '^(remote|branch)\.' (2)
remote.origin.url mothership:frotz
remote.origin.fetch refs/heads/*:refs/remotes/origin/*
branch.master.remote origin
branch.master.merge refs/heads/master
git config remote.origin.push \
  +refs/heads/*:refs/remotes/satellite/* (3)
edit/compile/test/commit
git push origin (4)

# from mothership machine
cd frotz
git switch master
git merge satellite/master (5)
```

1. mothership machine has a frotz repository under your home
directory; clone from it to start a repository on the satellite
machine.
1. clone sets these configuration variables by default. It
arranges git pull to fetch and store the branches of mothership
machine to local remotes/origin/* remote-tracking branches.
1. arrange git push to push all local branches to their
corresponding branch of the mothership machine.
1. push will stash all our work away on remotes/satellite/*
remote-tracking branches on the mothership machine. You could use
this as a back-up method. Likewise, you can pretend that
mothership "fetched" from you (useful when access is one sided).
1. on mothership machine, merge the work done on the satellite
machine into the master branch.

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
- `install, reinstall, remove, purge`: Performs the requested action on one or more packages specified via regex(7), glob(7) or exact match. The requested action can be overridden for specific packages by appending a plus (+) to the package name to install this package or a minus (-) to remove it.
  - A specific version of a package can be selected for installation by following the package name with an equals (=) and the version of the package to select. Alternatively the version from a specific release can be selected by following the package name with a forward slash (/) and codename (buster, bullseye, sid ...) or suite name (stable,testing, unstable). This will also select versions from this release for dependencies of this package if needed to satisfy the request.
  - Removing a package removes all packaged data, but leaves usually small (modified) user configuration files behind, in case the remove was an accident. Just issuing an installation request for the accidentally removed package will restore its function as before in that case.
  - On the other hand you can get rid of these leftovers by calling purge even on already removed packages. Note that this does not affect any data or configuration stored in your home directory.
- `autoremove` is used to remove packages that were automatically installed to satisfy dependencies for other packages and are now no longer needed as dependencies changed or the package(s) needing them were removed in the meantime.
  - You should check that the list does not include applications you have grown to like even though they were once installed just as a dependency of another package. You can mark such a package as manually installed by using apt-mark(8). Packages which you have installed explicitly via install are also never proposed for automatic removal.
- `satisfy`: satisfies dependency strings, as used in Build-Depends. It also handles conflicts, by prefixing an argument with "Conflicts: <(value)>".
- `search`: can be used to search for the given regex(7) term(s) in the list of available packages and display matches. This can e.g. be useful if you are looking for packages having a specific feature. If you are looking for a package including a specific file try apt-file.
- `show`: information about the given package(s) including its dependencies, installation and download size, sources the package is available from, the description of the packages content and much more
- `list`: is somewhat similar to dpkg-query --list in that it can display a list of packages satisfying certain criteria. It supports glob patterns for matching package names as well as options to list installed (--installed), upgradeable (--upgradeable) or all available (--all-versions) versions.
- `edit-sources`: lets you edit your sources.list(5) files in your preferred text editor while also providing basic sanity checks.
- Also view apt-get, apt-cache, sources.list, apt.conf, apt-config

___

## example commands

```sh
echo $BASH
# /usr/bin/bash

init $PATH

. # current working dir
.. # parent dir
~ $HOME # home dir of user
ls -a -@ -l
ls -C -l

# remove dir & files
rm -r /folder/want-deleted # remove dir & content recursively
rm -rp # ignore permissions & errors
sudo rm -rf path/to/folder
su - user -c 'ls' #switch user and run cmd
mount -uw # mount with write permissions
mount -o update /
diskutil list
df -h
find / -size +50000 -print

whereis [exe,cmd]
whatis <cmdname>
uname -a # show system info
free -gh #show memory usage --lohi -l from /proc/meminfo
service ssh status # check service status
ssh -l username hostname
top -u ib-ub
ps -ef | more # view running processes
ps -ef grep code
kill -9 PID # killall, pkill, xkill to terminate unix process

grep -i "word" file.txt # find str in fi
find -iname "file.txt" # find fi
find /home/ib-ub -name *.md -type f

gzip file.md, gzip -d file.md # zip & unzip .gz fi
unzip fi.zip && unzip -l fi.zip #extract or view w/o unzipping fi
shutdown -h now #shutdown now or -r to restart now
cat -n /home/ib-ub/flow/work/Docs2/requirements3.txt # print file to stdout
chmod ug+rwx file.txt # change permissions of fi/dir [-R u-rwx ex. will remove access recursively]
chown ib-ub:group_name file.txt # change owner
passwd username # change password; use sudo to reset w/o old pass
man 3 free # bring up section 3 of free cmd
tail -n 10 file.txt # show last 10 lines of fi
less large_file.txt # efficient view of log fi (CTRL+F/B forward/backward 1 window)
diff -w file1.md file2.md # compare, ignore whitespace fi1 to fi2
ps top vmstat brk mmap wget, systemctl, init
```

## Shell command info

- ctrl + \ = Quit (SIGQUIT)
  - fquit a running instance
- open path/to/app.app
  - open an app from sh
- escape special chars:
  - prepending with \
  - wrapping it in single quotes

## git colors for terminal

| foreground('') k => int = v => str | background(bg) {k:'v'}| style |
| --- | :--- | ---  |
| 31  = red |40  = black bg | 0   = default colour|
| 32  = green  | 41  = red bg   | 1   = bold|
| 33  = orange | 42  = green bg | 4   = underlined|
| 34  = blue   | 43  = orange bg| 5   = flashing text|
| 35  = purple | 44  = blue bg  | 7   = reverse field > (flip fore/bg color)|
| 36  = cyan  |  45  = purple bg |8   = concealed (invisible)|
| 37  = grey| 46  = cyan bg | 0 = default colour|
| 90  = dark grey  | 47  = grey bg  | 1   = bold|
| 91  = light red  | 100 = dark grey bg|
| 92  = light green| 101 = light red bg|
| 93  = yellow | 102 = light green bg|
| 94  = light blue | 103 = yellow bg|
| 95  = light purple  |104 = light blue bg|
| 96  = turquoise |  105 = light purple bg|
| 97  = white |  106 = turquoise bg | |
| | 107 = white bg| |

## symbolic rep of data

| abbrev | value |
| --- | --- |
|**no**  |  Global default|
|fi  |  Normal file|
|di  |  Directory|
|ln  |  Symbolic link.|
|bd  |  Block device|
|cd  |  Character device|
|or  |  Symbolic link to a non-existent file|
|ex  |  Executable file|
|**.extension | (ex: *.mp3)|

## linux permissions

```py
# permission terms
r, w, x = read, write, execute | 4, 2, 1
u, g, o = user, group, others | first, sec., third (chars.)
```

```sh
chmod u+x file.txt
chmod u+r,g+x file.txt
chmod u-rx file.txt # remove permissions
chmod -R 775 dir_name/ # change permissions of all fi in dir
chmode -R,a-x,u+X *
# recursively remove exec perm from all under dir & add exec for user
  # other solution
for f in 'ls -R'; do [! -d"$f"] && chmod a-x "$f"; done
```
