# fedora.md

## About
**Name:** Fedora (named after the type of hat featured in the Red Hat logo, reflecting its sponsorship by Red Hat)

**Created:** Launched in 2003 by the Fedora Project and sponsored by Red Hat, Fedora was created as a free, community-driven Linux distribution. Its purpose is to provide the latest open-source software in a stable, secure, and innovative operating system.

**Similar Technologies:** Ubuntu, Debian, openSUSE, Arch Linux, CentOS

**Plain Language Definition:**
Fedora is a free Linux operating system that gives you the newest open-source software and tools, making it great for developers and everyday users alike.

---

## Package Management - DNF

```bash
sudo dnf update             # Update all packages
sudo dnf upgrade            # Upgrade system (same as update)
sudo dnf install package    # Install a package
sudo dnf remove package     # Remove a package
dnf search keyword          # Search for packages
dnf list installed          # List installed packages
dnf info package            # Show package information
sudo dnf autoremove         # Remove orphaned packages
sudo dnf clean all          # Clean package cache
```

## System Services - Systemctl

```bash
sudo systemctl start service     # Start a service
sudo systemctl stop service      # Stop a service
sudo systemctl restart service   # Restart a service
sudo systemctl enable service    # Enable service at boot
sudo systemctl disable service   # Disable service at boot
systemctl status service         # Check service status
systemctl list-units --type=service # List all services
```

## System Information

```bash
hostnamectl                 # Show system information
cat /etc/fedora-release     # Show Fedora version
uname -a                    # Show kernel information
lscpu                       # Show CPU information
free -h                     # Show memory usage
df -h                       # Show disk usage
lsblk                       # Show block devices
```

## Firewall - Firewalld

```bash
sudo firewall-cmd --state           # Check firewall status
sudo firewall-cmd --list-all        # List all firewall rules
sudo firewall-cmd --add-port=80/tcp      # Add port rule (temporary)
sudo firewall-cmd --add-port=80/tcp --permanent # Add port rule (permanent)
sudo firewall-cmd --reload           # Reload firewall rules
```

## Selinux Basics

```bash
getenforce                   # Check SELinux status
sudo setenforce 0            # Temporarily disable SELinux
sudo setenforce 1            # Re-enable SELinux
ls -Z file                   # Show SELinux context of file
sudo restorecon -R /path     # Restore SELinux contexts
```

## Quick Setup Tasks

```bash
# 1. Update system
sudo dnf update && sudo dnf upgrade

# 2. Install essential tools
sudo dnf install vim git curl wget

# 3. Enable SSH service
sudo systemctl enable --now sshd

# 4. Allow SSH through firewall
sudo firewall-cmd --add-service=ssh --permanent
```
