
# Windows Domain Controller and Group Policy Lab

A small Windows domain built from scratch to learn Active Directory Domain Services and Group Policy hands-on rather than from courseware. One domain controller, one joined client, and a set of Group Policy Objects that standardise the desktop for a specific security group.

## Why

Every Help Desk and NOC posting I read lists Active Directory and Group Policy as a hard requirement. Reading about them is not the same as watching a policy fail to apply and having to work out why. This lab exists so that when someone asks whether I have managed users in AD, the answer is a screenshot instead of a certificate.

## Environment

| Component | Detail |
|---|---|
| Hypervisor | Oracle VirtualBox |
| Domain controller | Windows Server 2025 |
| Client | Windows Pro workstation, joined to the domain |
| Directory service | Active Directory Domain Services, new forest |
| Networking | VirtualBox internal network, static IP on the DC, client resolving the domain through it |

Both machines run on one host. The client uses the domain controller as its DNS server, which is what makes domain join and policy retrieval work at all. It is also the first thing that breaks if you get it wrong.

---

## 1. Domain controller

Installed Windows Server 2025 as a VirtualBox VM, gave it a static address, added the Active Directory Domain Services role and promoted the server to a domain controller, creating a new forest.

Verified the promotion: SYSVOL and NETLOGON shares present, the DC discoverable, the domain resolvable from the client.

> Server Manager with the AD DS role installed
> ![ad ds](./images/ad-ds.png)

## 2. Domain join

Pointed the Windows Pro client at the domain controller for DNS, joined it to the domain, and confirmed login with a domain account rather than a local one.

> Showing the domain name instead of a workgroup.
> ![domain proof](./images/domainproof.png)

## 3. Users and groups

Created domain user accounts and security groups in Active Directory , and managed group membership. The group is the targeting mechanism for policy: membership decides who gets the desktop configuration, not the machine.

> Active Directory with the security group open on the Members tab.
> ![group member](./images/groupmember.png)

## 4. Group Policy

Authored and linked Group Policy Objects applying to one target security group:

- **Enforced desktop wallpaper.** Every member of the group gets the same background, set centrally.
- **Deployed shortcut.** A specific shortcut is placed on each group member's desktop.
- **Machine and account information on the desktop.** Host and account details are displayed on the desktop background, so a support call starts with the user reading what is already on their screen instead of hunting through system properties.

> Group Policy Management showing the GPO linked, with Security Filtering scoped to the target group
> ![GPO sec](./images/GPO_sec.png)

> Group Policy editor - shortcut
> ![GPO shortcut](./images/GPO_shortcut.png)

> Group Policy editor - logon script
> ![GPO logon](./images/GPO_logon.png)

## 5. Verification

Forced a policy refresh on the client with `gpupdate /force`, then confirmed with `gpresult` that the intended GPOs applied to members of the target group, and did not apply to accounts outside it.

> The client desktop as a group member sees it: wallpaper, the deployed shortcut, and the machine and account details on the background.
> ![GPO view](./images/GPO_user_view.png)

> 📸  `gpresult` with the applied GPO visible.
> ![GPO rusults](./images/GPO_results.png)


---

## What broke and what it taught me

**DNS is the whole game.** Before the client used the DC as its DNS server, domain join failed with an unhelpful message. Nothing in Active Directory works until name resolution points at the domain controller.

**Policy scope is not obvious.** A GPO linked at the wrong level reaches more accounts than intended. `gpresult` is the only way to know what actually landed rather than what you think you configured.

**Refresh is not instant.** Group Policy applies on a schedule. `gpupdate /force` is what turns "I changed it" into "it is live" while testing.

## Relevance to Help Desk and NOC work

First-line support is largely this: unlock and reset accounts, add and remove people from groups, work out why a user is missing a mapped drive or a shortcut, and confirm whether a policy reached a machine.

## Next steps

- A second client, to see policy behaviour across more than one machine.
- File shares with group-based NTFS permissions.
- A logon script, compared against Group Policy Preferences as a delivery method.

---

*Part of my IT and security operations portfolio: [github.com/5921189-hash/cybersecurity-portfolio](https://github.com/5921189-hash/cybersecurity-portfolio)*
