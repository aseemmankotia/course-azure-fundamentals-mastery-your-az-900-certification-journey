## Chapter 3: Data, Storage & Identity: Protecting What Matters Most — Quick Reference

### Core Concepts
| Concept | One-line explanation |
|---------|---------------------|
| Azure Storage Account | Container that groups all Azure storage services (Blobs, Files, Queues, Disks) |
| Blob Storage | Object storage for unstructured data (images, videos, backups) |
| Hot/Cool/Archive Tiers | Access tiers balancing storage cost vs. retrieval cost based on frequency |
| Azure Files | Fully managed SMB/NFS file shares accessible from cloud or on-premises |
| Azure Queue Storage | Message queue service for async communication between app components |
| Azure Disk Storage | Block-level storage volumes for Azure VMs (managed disks) |
| Microsoft Entra ID | Cloud-based identity and access management service (formerly Azure AD) |
| Single Sign-On (SSO) | One login grants access to multiple applications |
| Multi-Factor Authentication | Requires 2+ verification methods (something you know/have/are) |
| Conditional Access | Policies that evaluate signals to enforce access decisions |

### Key Redundancy Options
```
LRS  - 3 copies in ONE datacenter (lowest cost)
ZRS  - 3 copies across 3 availability zones (same region)
GRS  - LRS + async copy to secondary region
RA-GRS - GRS + READ access to secondary region
GZRS - ZRS + async copy to secondary region (highest durability)
```

### Common Patterns
**Pattern 1: Tiered Storage Strategy**
Hot tier for active data → Cool tier after 30 days → Archive tier for compliance/long-term

**Pattern 2: Zero-Trust Identity**
Entra ID + MFA + Conditional Access = verify explicitly, least privilege, assume breach

### Things to Remember
✅ Archive tier has lowest storage cost but highest retrieval cost/latency (hours)
✅ Entra Domain Services provides managed domain join without domain controllers
✅ Passwordless options: Windows Hello, FIDO2 keys, Microsoft Authenticator app
❌ Don't confuse GRS (failover only) with RA-GRS (read access to secondary anytime)

### Quick Quiz
1. Which tier for rarely accessed data needing immediate access? → **Cool tier**
2. How many copies does ZRS maintain? → **3 copies across 3 zones**
3. What enforces "block access from unknown locations"? → **Conditional Access policies**