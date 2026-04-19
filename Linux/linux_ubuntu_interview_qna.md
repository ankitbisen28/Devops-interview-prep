# 🐧 Linux & Ubuntu Interview Questions (with Answers)

## 🔹 1–10: Basic Linux Commands

### 1. What is Linux?
Linux is an open-source, Unix-like operating system kernel created by Linus Torvalds. Distributions like Ubuntu use this kernel along with tools and packages.

### 2. What is a Linux distribution?
A Linux distribution (distro) is a complete OS built using the Linux kernel + software packages.
Examples: Ubuntu, CentOS, Debian.

### 3. Difference between Linux and Unix?
- Linux → Open source
- Unix → Mostly proprietary
- Linux is Unix-like but not Unix itself

### 4. What is the root user?
The root user is the superuser with full administrative privileges.

### 5. What is a shell?
A shell is a command-line interface to interact with the OS.
Examples: bash, zsh

### 6. Common Linux commands?
- ls → list files
- cd → change directory
- pwd → current directory
- cp, mv, rm

### 7. What is `man` command?
Used to view manual pages:
```bash
man ls
```

### 8. What is `sudo`?
Allows a normal user to execute commands as root.

### 9. What is `grep`?
Used to search text in files:
```bash
grep "error" file.txt
```

### 10. What is `find`?
Used to search files:
```bash
find / -name file.txt
```

## 🔹 11–20: File System & Permissions

### 11. What is Linux file system structure?
Top directories:
- / → root
- /home → user data
- /etc → config files
- /var → logs
- /bin → binaries

### 12. What is inode?
Stores metadata of a file (permissions, owner, size).

### 13. File permissions in Linux?
Format: rwx
- r → read
- w → write
- x → execute

### 14. What is chmod?
Change file permissions:
```bash
chmod 755 file.sh
```

### 15. What is chown?
Change file ownership:
```bash
chown user:group file.txt
```

### 16. What is umask?
Default permission mask for new files.

### 17. Difference: hard link vs soft link?
- Hard link → same inode
- Soft link → pointer (shortcut)

### 18. What is df command?
Shows disk usage:
```bash
df -h
```

### 19. What is du command?
Shows directory size:
```bash
du -sh folder/
```

### 20. What is mount?
Attach filesystem:
```bash
mount /dev/sdb1 /mnt
```

## 🔹 21–30: Process Management

### 21. What is a process?
A running instance of a program.

### 22. How to check running processes?
```bash
ps aux
```

### 23. What is top command?
Real-time system monitoring.

### 24. What is kill command?
Terminate process:
```bash
kill -9 PID
```

### 25. What is nice value?
Priority of process (-20 to 19).

### 26. What is background process?
Runs without blocking terminal:
```bash
command &
```

### 27. What is foreground process?
Runs directly in terminal.

### 28. What is cron job?
Used to schedule tasks:
```bash
crontab -e
```

### 29. What is systemctl?
Manages services in modern Linux (systemd):
```bash
systemctl start nginx
```

### 30. What is daemon?
Background service (e.g., sshd, nginx).

## 🔹 31–40: Networking

### 31. What is IP address?
Unique identifier for devices in a network.

### 32. What is ping?
Check connectivity:
```bash
ping google.com
```

### 33. What is netstat?
Shows network connections.

### 34. What is ss command?
Modern alternative to netstat.

### 35. What is SSH?
Secure remote login protocol:
```bash
ssh user@ip
```

### 36. What is scp?
Secure file copy:
```bash
scp file user@ip:/path
```

### 37. What is curl?
Used to call APIs:
```bash
curl http://example.com
```

### 38. What is wget?
Download files from internet.

### 39. What is firewall in Linux?
Controls network traffic. Example: ufw in Ubuntu.

### 40. What is DNS?
Maps domain name to IP address.

## 🔹 41–50: Advanced & DevOps Concepts

### 41. What is package manager in Ubuntu?
Ubuntu uses apt.

### 42. Difference between apt and apt-get?
- apt → user-friendly
- apt-get → scripting

### 43. What is log file location?
/var/log/

### 44. What is environment variable?
Stores system-wide values:
```bash
export VAR=value
```

### 45. What is PATH variable?
Defines directories to search executables.

### 46. What is disk partition?
Dividing disk into sections.

### 47. What is swap memory?
Used when RAM is full.

### 48. What is kernel?
Core of OS managing hardware/resources.

### 49. What is shell scripting?
Automating tasks using shell commands.

### 50. What is load average?
System load over time (1, 5, 15 min).
