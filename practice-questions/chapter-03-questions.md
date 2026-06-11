## Chapter 3: Data, Storage & Identity: Protecting What Matters Most — Practice Questions

### Multiple Choice

**Q1.** A company needs to store large video files that are rarely accessed but must be retained for 7 years due to compliance requirements. Which Azure Blob Storage tier would be the MOST cost-effective option?

A) Hot tier
B) Cool tier
C) Archive tier
D) Premium tier

<details>
<summary>Answer</summary>

**Correct: C**

The Archive tier is designed for data that is rarely accessed and stored for at least 180 days. It offers the lowest storage costs, making it ideal for long-term retention of compliance data. Hot tier is for frequently accessed data and costs more. Cool tier is for infrequently accessed data stored for at least 30 days but costs more than Archive. Premium tier is for high-performance needs, not cost optimization for rarely accessed data.

</details>

---

**Q2.** Which Azure storage redundancy option stores three copies of your data across multiple data centers in two different Azure regions?

A) Locally Redundant Storage (LRS)
B) Zone-Redundant Storage (ZRS)
C) Geo-Redundant Storage (GRS)
D) Read-Access Geo-Redundant Storage (RA-GRS)

<details>
<summary>Answer</summary>

**Correct: C**

Geo-Redundant Storage (GRS) replicates your data synchronously three times within a single region, then asynchronously to a secondary region. LRS stores three copies within a single data center. ZRS stores three copies across availability zones in one region. RA-GRS is similar to GRS but adds read access to the secondary region, though the question asks specifically about the storage pattern, not read access.

</details>

---

**Q3.** Your organization wants to allow users to access multiple cloud applications using one set of credentials without entering passwords repeatedly. Which authentication feature should you implement?

A) Multi-Factor Authentication (MFA)
B) Single Sign-On (SSO)
C) Conditional Access
D) Passwordless authentication

<details>
<summary>Answer</summary>

**Correct: B**

Single Sign-On (SSO) enables users to sign in once and access multiple applications without re-entering credentials. MFA adds additional verification steps but doesn't reduce sign-in frequency. Conditional Access controls when and how users can access resources. Passwordless authentication eliminates passwords but doesn't address accessing multiple applications with one sign-in.

</details>

---

**Q4.** Which Azure service provides fully managed file shares that can be accessed using the Server Message Block (SMB) protocol?

A) Azure Blob Storage
B) Azure Queue Storage
C) Azure Files
D) Azure Disk Storage

<details>
<summary>Answer</summary>

**Correct: C**

Azure Files provides fully managed file shares accessible via the SMB protocol, making it easy to migrate on-premises file servers to the cloud. Azure Blob Storage is for unstructured data like images and videos. Azure Queue Storage is for messaging between application components. Azure Disk Storage provides block-level storage volumes for virtual machines.

</details>

---

**Q5.** A company wants to require MFA only when users access sensitive applications from outside the corporate network. Which Microsoft Entra ID feature should they configure?

A) Single Sign-On (SSO)
B) Microsoft Entra Domain Services
C) Conditional Access policies
D) Passwordless authentication

<details>
<summary>Answer</summary>

**Correct: C**

Conditional Access policies allow you to define specific conditions (such as location, device state, or application sensitivity) that trigger additional security requirements like MFA. SSO simplifies access but doesn't add conditional security controls. Microsoft Entra Domain Services provides domain services for legacy applications. Passwordless authentication is an authentication method, not a policy engine.

</details>

---

### True / False

**Q6.** Microsoft Entra ID is the same service as on-premises Windows Server Active Directory, just hosted in Azure. — **True / False**

*False. Microsoft Entra ID (formerly Azure AD) is a cloud-based identity and access management service that is fundamentally different from on-premises Active Directory. While both handle identity, Microsoft Entra ID is designed for cloud applications and uses modern protocols like OAuth and SAML. On-premises AD uses protocols like Kerberos and LDAP. They can work together but are not the same service.*

---

**Q7.** Azure Queue Storage is designed to store messages that allow different components of an application to communicate asynchronously. — **True / False**

*True. Azure Queue Storage is specifically designed to store large numbers of messages that can be accessed from anywhere via HTTP or HTTPS. It enables asynchronous communication between application components, helping to decouple different parts of a distributed application and improve scalability and reliability.*

---

### Short Answer

**Q8.** What is the primary difference between Read-Access Geo-Redundant Storage (RA-GRS) and standard Geo-Redundant Storage (GRS)?

<details>
<summary>Answer</summary>

RA-GRS provides read access to data in the secondary region at any time, while standard GRS only allows access to the secondary region during a failover event. With RA-GRS, applications can read from the secondary region for improved availability, even when the primary region is functioning normally.

</details>

---

**Q9.** Name three authentication methods supported by Microsoft Entra ID that are considered passwordless.

<details>
<summary>Answer</summary>

Three passwordless authentication methods supported by Microsoft Entra ID include: (1) Windows Hello for Business, which uses biometrics or PIN tied to a device; (2) Microsoft Authenticator app, which uses push notifications and biometrics; and (3) FIDO2 security keys, which are physical hardware devices. These methods eliminate the need for traditional passwords.

</details>

---

### Scenario-Based

**Q10.** Contoso Ltd. is migrating their on-premises infrastructure to Azure. They have the following requirements:

- Virtual machines need high-performance persistent storage for their operating systems
- Marketing team needs to store promotional images that are accessed frequently
- Finance team needs to store audit logs that must be retained for 10 years and are accessed only during annual audits
- The IT team wants to lift-and-shift their existing file server that uses mapped network drives

Which Azure storage solution should be used for EACH requirement?

<details>
<summary>Answer</summary>

**Virtual machine operating systems:** Azure Disk Storage — This provides block-level storage volumes that attach directly to VMs, offering the high performance needed for OS disks.

**Marketing promotional images (frequently accessed):** Azure Blob Storage with Hot tier — Blob storage is ideal for unstructured data like images, and the Hot tier is optimized for data that is accessed frequently.

**Finance audit logs (10-year retention, rarely accessed):** Azure Blob Storage with Archive tier — The Archive tier offers the lowest storage costs for data that is rarely accessed but must be retained for long periods.

**IT file server with mapped network drives:** Azure Files — This service supports the SMB protocol, allowing users to continue using mapped network drives just as they did with the on-premises file server.

</details>

---