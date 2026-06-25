# Linux VPS Hardening And Secure SSH Architecture

## 1. Executive Summary
Exposing management interfaces (such as SSH) directly to the public internet invites constant automated brute-force attacks and vulnerability scanning. This technical document outlines the hardening process implemented on a cloud virtual private server (VPS) to achieve a resilient, zero-trust administrative workflow. By combining SSH daemon hardening with a private Mesh VPN (Tailscale), the attack surface for remote management was effectively reduced to zero.

---

## 2. Environment And Architecture Overview
* **Cloud Provider:** DigitalOcean
* **Operating System:** Ubuntu Linux
* **Core Security Architecture:** Defense-in-Depth, Least Privilege, Zero-Trust Network Access (ZTNA)

---


## 3. Technical Implementation Details And Command Log

### Phase 1: Safe User Provisioning And SSH Daemon Hardening

To eliminate the risk of an accidental lockout while disabling the `root` account, the following strict chronological workflow was executed:

1. **Low-Privileged User Creation:**
   
   Created a standard user account and granted administrative capabilities via the `sudo` group, adhering to the Principle of Least Privilege (PoLP):
   
   ```bash
   # Add the new standard user
   sudo adduser secops
   
   # Add the user to the sudo group for administrative privileges
   sudo usermod -aG sudo secops
   ```
3. **Cryptographic Key Generation And Deployment:**
   
   Generated a secure asymmetric key pair on the local client machine and manually deployed the public key to the VPS, ensuring strict file permissions:
   
    ```bash
    # Executed on LOCAL machine
    # Generate a secure Ed25519 key pair
    ssh-keygen -t ed25519 -C "vps-management-key"
    
    # Executed on VPS as 'secops' user
    # Create directory and set secure permissions
    mkdir -p ~/.ssh
    chmod 700 ~/.ssh
    
    # Append your local public key content into authorized_keys
    echo "ssh-ed25519 AAAAC3NzaC1lZ... vps-management-key" >> ~/.ssh/authorized_keys
    
    # Enforce strict file permissions on the authorized_keys file
    chmod 600 ~/.ssh/authorized_keys
    ```
3. **Pre-Lockout Verification:**
   
   Critical Operational Step: Before modifying global SSH daemon configurations or closing the active root session, a parallel terminal window was opened to test and verify successful key-based login for the new secops user:

   ```bash
   # Executed on LOCAL machine
   # Verify access without closing the current root session
   ssh -i ~/.ssh/id_ed25519 secops@<vps_ip>
   ```
4. **Enforcing Hardening Policies, Executed On VPS (`/etc/ssh/sshd_config`):**

   Once key-based access was fully validated, the global configuration file was modified to block automated brute-force attacks and direct root exposure:
    ```bash

    # Open the SSH daemon configuration file
    sudo nano /etc/ssh/sshd_config
    ```

    The following directives were updated/appended:
    ```config
    # Shift from default port 22 to reduce automated scan noise
    Port 44588

    # Disable direct root access via SSH
    PermitRootLogin no
    
    # Disable acces with password    
    PasswordAuthentication no

    # Explicitly allow public key authentication
    PubkeyAuthentication yes   
    ```
    Tested the configuration file for errors before applying changes to prevent service failure:
    ```bash
    # Test sshd configuration syntax for errors
    sudo sshd -t
    
    # If no errors are returned, restart the SSH daemon to apply changes
    sudo systemctl restart ssh
    ```
### Phase 2: Network Layer Security And Tailscale Mesh VPN Architecture

To implement a strict Zero-Trust Network Access  model, the management plane (SSH) was completely decoupled from the public internet and routed through a private, encrypted WireGuard-based mesh overlay network (Tailscale).

#### Step 1: VPS Node Provisioning And Tailnet Authentication
1. Installed the Tailscale daemon on the Ubuntu VPS using the official repository script:
   ```bash
   curl -fsSL [https://tailscale.com/install.sh](https://tailscale.com/install.sh) | sh
   ```
2. Initiated the authentication process to register the VPS into the private Tailnet (coordination server):
   ```bash
   sudo tailscale up
   ```
   _Operational Detail_: This command generates a unique interactive login URL. I authenticated the machine by logging into the Tailscale Admin Console via a web browser.

#### Step 2: Client-Side Mesh Configuration (Local Machine)
1. Installed the Tailscale client on the local machine
2. Authenticated the local machine into the same account, instantly building an encrypted WireGuard tunnel directly between the local client and the cloud VPS without needing a centralized VPN gateway.

#### Step 3: Firewall Enforcement via UFW
With the private overlay network active, the host firewall (UFW) was configured to drop all traffic from the public network interface (`eth0`) and explicitly whitelist SSH traffic coming only from the virtual Tailscale interface (`tailscale0`):

   ```bash
   # Disable the firewall just not to block myself
   sudo ufw disable

   # Reset UFW to a secure baseline
   sudo ufw default deny incoming
   sudo ufw default allow outgoing
   
   # Allow SSH (Port 44588) ONLY over the Tailscale interface
   sudo ufw allow in on tailscale0 to any port 44588 proto tcp comment 'Restrict SSH to Tailscale VPN'
   
   # Enable the firewall
   sudo ufw enable
   ```
#### Step 4: Verifying the Network Isolation Posture
To confirm that the attack surface was successfully minimized, I verified the UFW rules and performed an external port scan:

```bash
# Check UFW verbose status
sudo ufw status verbose

# Expected Output snippet:
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), deny (routed)
New profiles: skip
To                         Action      From
--                         ------      ----
44588/tcp on tailscale0     ALLOW IN    Anywhere                 
```
Verification Outcome: An external scan (using `nmap -p 44588 <vps_public_ip>`) from an unauthenticated internet IP returns `filtered`, completely hiding the management interface from unauthorized malicious actors and automated internet background noise.

### Phase 3: Client-Side Optimization
To simplify operations while maintaining maximum security, a local configuration block was created on the management machine to map security controls to a seamless single-command login.

1. **Client Configuration** (`~/.ssh/config`):
   Opene ssh config (`nano ~/.ssh/config`), appended the following  block:
   ```text
   Host vps
    HostName 100.X.Y.Z              # Private internal Tailscale IP address of the VPS
    User secops                     # Hardened standard user account
    Port 44588                      # Custom obfuscated SSH port
    IdentityFile ~/.ssh/id_ed25519  # Local path to the passphrase-protected private key
   ```
2. **Operational Workflow**
   Administrative access to the remote cloud environment is now securely initiated via a streamlined shortcut, which automatically utilizes the private key, custom port, and VPN routing table: `ssh prod-vps`


   
