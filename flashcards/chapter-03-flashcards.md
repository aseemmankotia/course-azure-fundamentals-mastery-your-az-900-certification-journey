## Chapter 3: Data, Storage & Identity: Protecting What Matters Most — Flashcards

| # | Front (Question) | Back (Answer) |
|---|-----------------|---------------|
| 1 | What is an Azure Storage account? | A container that groups Azure Storage services (Blobs, Files, Queues, Tables, Disks) under a unique namespace accessible worldwide over HTTP/HTTPS |
| 2 | What are the three access tiers for Azure Blob Storage? | Hot (frequent access, highest storage cost), Cool (infrequent access, 30-day minimum), Archive (rare access, lowest storage cost, 180-day minimum) |
| 3 | What type of data is Azure Blob Storage optimized for? | Unstructured data such as images, videos, documents, backups, and log files |
| 4 | What is Azure Files used for? | Providing fully managed file shares in the cloud accessible via SMB and NFS protocols, replacing or extending on-premises file servers |
| 5 | What is the purpose of Azure Queue Storage? | Storing large numbers of messages for asynchronous processing and communication between application components |
| 6 | What does LRS (Locally Redundant Storage) provide? | Three synchronous copies of data within a single datacenter in one region, protecting against server/drive failures |
| 7 | How does GRS differ from LRS? | GRS replicates data to a secondary region hundreds of miles away, providing 16 nines durability versus LRS which stays in one datacenter |
| 8 | What does RA-GRS add beyond standard GRS? | Read Access to the secondary region, allowing applications to read data from the backup region even when primary is available |
| 9 | What is Microsoft Entra ID (formerly Azure AD)? | Microsoft's cloud-based identity and access management service for signing in and accessing resources |
| 10 | What is Single Sign-On (SSO)? | An authentication method allowing users to sign in once and access multiple applications without re-entering credentials |
| 11 | What is Multi-Factor Authentication (MFA)? | A security method requiring two or more verification factors: something you know, have, or are |
| 12 | What are examples of passwordless authentication in Azure? | Windows Hello for Business, Microsoft Authenticator app, and FIDO2 security keys |
| 13 | What are Conditional Access policies? | Rules that evaluate signals (user, location, device, app) to make access decisions: allow, block, or require additional verification |
| 14 | What is Microsoft Entra Domain Services? | A managed service providing domain join, group policy, LDAP, and Kerberos/NTLM authentication without deploying domain controllers |
| 15 | What does GZRS (Geo-Zone-Redundant Storage) combine? | ZRS in the primary region (3 availability zones) plus GRS replication to a secondary region for maximum durability |

### Key Terms

| Term | Definition |
|------|-----------|
| Blob Storage | Azure service for storing massive amounts of unstructured data like text or binary data |
| Storage Redundancy | Data replication strategy determining how many copies exist and where they're stored |
| ZRS (Zone-Redundant Storage) | Replicates data across three availability zones in one region for high availability |
| Microsoft Entra ID | Cloud identity platform providing authentication, SSO, and access management for Azure and other services |
| Conditional Access | Zero-trust security approach using if-then policies to control resource access based on conditions |
| MFA | Security requiring multiple verification methods to prove identity before granting access |
| Azure Disk Storage | Block-level storage volumes for Azure VMs, available as HDD, Standard SSD, Premium SSD, or Ultra Disk |

### Memory Tricks
- **"HAC" for Blob tiers**: Hot (frequently touched), Archive (ancient/rarely touched), Cool (in between) - think of temperature matching access frequency
- **"LZG" redundancy ladder**: Local → Zone → Geo - each step adds geographic distance for better protection
- **"SMP" for passwordless**: Something you have (Security key), Microsoft Authenticator, Physical presence (Windows Hello) - no passwords needed
- **MFA's three factors**: "Know-Have-Are" - Password (know), Phone (have), Fingerprint (are)
- **"BFQD" Storage types**: Blobs (objects), Files (shares), Queues (messages), Disks (VMs) - "Big Files Queue Daily"