## Chapter 2: Azure's Global Backbone: Architecture, Compute & Networking — Practice Questions

### Multiple Choice

**Q1.** Your company requires that data remains within a specific geographic boundary due to regulatory compliance. Which Azure concept helps ensure data residency requirements are met?

A) Availability Zones
B) Resource Groups
C) Regions
D) Management Groups

<details>
<summary>Answer</summary>

**Correct: C**

Regions are specific geographic locations where Azure datacenters are located. Selecting a region ensures your data is stored in that geographic area, helping meet data residency requirements. Availability Zones provide redundancy within a region but don't address geographic location. Resource Groups and Management Groups are organizational tools, not geographic concepts.

</details>

---

**Q2.** A startup wants to deploy a simple web application without managing the underlying servers or infrastructure. Which Azure service would be MOST appropriate?

A) Azure Virtual Machines
B) Azure App Service
C) VM Scale Sets
D) Azure Virtual Desktop

<details>
<summary>Answer</summary>

**Correct: B**

Azure App Service is a Platform as a Service (PaaS) offering that allows you to host web applications without managing underlying infrastructure. Virtual Machines require you to manage the OS and infrastructure. VM Scale Sets are for scaling VMs, still requiring infrastructure management. Azure Virtual Desktop is for desktop virtualization, not web hosting.

</details>

---

**Q3.** What is the primary purpose of Azure Resource Manager (ARM)?

A) To monitor the performance of Azure resources
B) To provide a consistent management layer for deploying and managing Azure resources
C) To connect on-premises networks to Azure
D) To automatically scale virtual machines

<details>
<summary>Answer</summary>

**Correct: B**

Azure Resource Manager (ARM) is the deployment and management service for Azure. It provides a consistent management layer that enables you to create, update, and delete resources using templates, RBAC, tags, and policies. Monitoring is handled by Azure Monitor, networking by VPN Gateway/ExpressRoute, and scaling by VM Scale Sets.

</details>

---

**Q4.** Which Azure networking option provides the HIGHEST bandwidth and most reliable private connection between an on-premises datacenter and Azure?

A) VPN Gateway
B) Azure DNS
C) ExpressRoute
D) Virtual Networks

<details>
<summary>Answer</summary>

**Correct: C**

ExpressRoute provides a private, dedicated connection between on-premises infrastructure and Azure that doesn't traverse the public internet, offering higher bandwidth, lower latency, and more reliability. VPN Gateway uses encrypted connections over the public internet. Azure DNS is for domain name resolution. Virtual Networks are for organizing resources within Azure.

</details>

---

**Q5.** Your organization has multiple Azure subscriptions across different departments. You need to apply consistent policies and access controls across all subscriptions. Which resource organization level should you use?

A) Resource Groups
B) Management Groups
C) Availability Zones
D) Region Pairs

<details>
<summary>Answer</summary>

**Correct: B**

Management Groups allow you to organize multiple subscriptions and apply governance conditions like policies and access controls that are inherited by all subscriptions within the group. Resource Groups organize resources within a subscription. Availability Zones and Region Pairs are infrastructure availability concepts, not organizational tools.

</details>

---

### True / False

**Q6.** Availability Zones within an Azure region are physically separate datacenters with independent power, cooling, and networking. — **True / False**

*True. Availability Zones are unique physical locations within an Azure region. Each zone consists of one or more datacenters equipped with independent power, cooling, and networking. This design protects applications and data from datacenter failures by allowing you to distribute resources across multiple zones.*

---

**Q7.** Azure Functions require you to provision and manage virtual machines to run your code. — **True / False**

*False. Azure Functions is a serverless compute service that allows you to run code without provisioning or managing infrastructure. You only pay for the compute time when your code is running. Azure automatically handles all infrastructure management, scaling, and maintenance.*

---

### Short Answer

**Q8.** What is the relationship between Azure Region Pairs, and why are they important for disaster recovery?

<details>
<summary>Answer</summary>

Azure Region Pairs are two regions within the same geography that are paired together for disaster recovery purposes. They are typically located at least 300 miles apart. If one region experiences an outage, services can automatically failover to the paired region. Azure prioritizes recovery of one region in each pair during widespread outages, and updates are rolled out sequentially to paired regions to minimize downtime risk.

</details>

---

**Q9.** Explain the difference between Azure Container Instances (ACI) and Azure Kubernetes Service (AKS).

<details>
<summary>Answer</summary>

Azure Container Instances (ACI) is the simplest way to run containers in Azure without managing servers. It's ideal for simple applications, task automation, or short-lived workloads. Azure Kubernetes Service (AKS) is a managed container orchestration service for deploying, scaling, and managing complex containerized applications across multiple containers. AKS is better suited for large-scale, production applications requiring advanced features like load balancing, auto-scaling, and self-healing capabilities.

</details>

---

### Scenario-Based

**Q10.** Contoso Manufacturing runs a legacy inventory application that requires Windows Server 2019 with specific custom software installed. They need full control over the operating system for patching schedules and must be able to connect the application to their on-premises SQL Server database through a secure private connection. They also want to ensure high availability within a single Azure region.

Based on these requirements, which combination of Azure services should Contoso use?

A) Azure App Service, VPN Gateway, and Resource Groups
B) Azure Virtual Machines, ExpressRoute, and Availability Zones
C) Azure Functions, Azure DNS, and Management Groups
D) Azure Container Instances, VPN Gateway, and Region Pairs

<details>
<summary>Answer</summary>

**Correct: B**

Azure Virtual Machines provide full control over the Windows Server operating system, allowing installation of custom software and control over patching schedules. ExpressRoute provides a private, dedicated connection to the on-premises SQL Server database without traversing the public internet. Availability Zones ensure high availability within a single region by distributing VMs across physically separate datacenters.

Azure App Service and Functions don't provide OS-level control. Azure Container Instances don't support Windows-specific legacy applications with custom software easily. Region Pairs address cross-region disaster recovery, not single-region high availability.

</details>