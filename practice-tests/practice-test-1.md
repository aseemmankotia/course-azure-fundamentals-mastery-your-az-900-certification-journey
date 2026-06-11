# AZ-900: Beginners in cloud services — Practice Test 1

> **Time Limit:** 90 minutes
> **Questions:** 45
> **Passing Score:** 700/1000 (70%)
> **Generated:** 6/10/2026

---

## Instructions

- Read each question carefully
- Choose the BEST answer
- All questions are equally weighted
- Do not spend too long on any single question

---

## Questions

### Question 1
**Domain:** Data, Storage & Identity: Protecting What Matters Most | **Difficulty:** easy

Which Azure storage service is optimized for storing massive amounts of unstructured data such as text, images, videos, and backups?

- A) Azure Table Storage
- B) Azure Queue Storage
- C) Azure Blob Storage
- D) Azure File Storage

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

Azure Blob Storage is designed for storing large amounts of unstructured data like documents, images, videos, and backups, accessible via HTTP/HTTPS.

**Why not A:** Table Storage is for structured NoSQL data with key-attribute storage, not unstructured binary data.

**Why not B:** Queue Storage is for message queuing between application components, not data storage.

**Why not D:** File Storage provides SMB file shares, primarily for lift-and-shift scenarios requiring shared file access.

**Exam Tip:** Blob = Binary Large Object; think unstructured data like images, videos, documents

</details>

---

### Question 2
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** easy

What is the purpose of Azure Tags?

- A) To control network traffic between Azure resources
- B) To organize resources and enable cost tracking and management
- C) To automatically replicate resources across regions
- D) To define role-based access permissions

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Tags are name-value pairs applied to resources for organization, cost allocation, and management purposes. They enable filtering, grouping, and cost analysis by custom categories like department, project, or environment.

**Why not A:** Network traffic control is managed by Network Security Groups and Azure Firewall, not tags.

**Why not C:** Resource replication is handled by services like geo-replication or Azure Site Recovery, not tags.

**Why not D:** Access permissions are defined through Azure Role-Based Access Control (RBAC), not tags.

**Exam Tip:** Tags are METADATA for organization and cost allocation — they don't affect resource functionality.

</details>

---

### Question 3
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** medium

What is the purpose of an Azure Virtual Network (VNet)?

- A) To provide a public IP address for accessing the internet
- B) To create an isolated network environment for Azure resources to communicate securely
- C) To automatically scale applications based on demand
- D) To store virtual machine disk images

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Virtual Networks provide network isolation and segmentation, enabling Azure resources to securely communicate with each other, the internet, and on-premises networks.

**Why not A:** Public IP addresses are separate resources that can be attached to resources; VNets provide the network itself.

**Why not C:** Automatic scaling is handled by VM Scale Sets or App Service, not VNets.

**Why not D:** VM disk images are stored in Azure Storage or managed disks, not VNets.

**Exam Tip:** VNets are the foundation of Azure networking - required for VMs and many other resources

</details>

---

### Question 4
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** medium

What does the shared responsibility model in cloud computing define?

- A) How cloud costs are split between departments within an organization
- B) The division of security and management tasks between the cloud provider and customer
- C) How multiple tenants share the same physical hardware resources
- D) The process for sharing data between different cloud providers

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

The shared responsibility model clearly defines which security and management responsibilities belong to the cloud provider and which belong to the customer, varying by service model (IaaS/PaaS/SaaS).

**Why not A:** This describes internal cost allocation or chargebacks, not the shared responsibility model.

**Why not C:** This describes multi-tenancy, which is a different cloud concept.

**Why not D:** This describes cloud interoperability or data portability, not shared responsibility.

**Exam Tip:** Customer always responsible for data, accounts, and access management regardless of service model

</details>

---

### Question 5
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** medium

When preparing for the AZ-900 exam, which concept should you associate with the term 'elasticity' in cloud computing?

- A) The ability to recover from failures automatically
- B) The ability to quickly scale resources up or down based on demand
- C) The ability to deploy resources in multiple geographic regions
- D) The ability to secure data with encryption

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Elasticity is the ability to automatically or quickly scale computing resources up or down to match demand, paying only for resources actually used.

**Why not A:** Automatic recovery from failures describes fault tolerance or self-healing, not elasticity.

**Why not C:** Deploying across geographic regions describes geo-distribution or global reach, not elasticity.

**Why not D:** Data encryption describes security capabilities, not elasticity.

**Exam Tip:** Elasticity = Automatic scaling to match demand. Scalability = Ability to handle growth. Both are key cloud benefits.

</details>

---

### Question 6
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** hard

An organization is architecting a solution that requires automatic scaling of virtual machines based on CPU usage, automatic replacement of failed instances, and the ability to apply updates without downtime. Which Azure compute feature provides these capabilities?

- A) Availability Sets with manual scaling
- B) Virtual Machine Scale Sets with autoscale rules
- C) Single VM with Azure Monitor alerts
- D) Reserved Virtual Machine Instances

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

VM Scale Sets provide automatic scaling based on metrics like CPU, automatic instance replacement when failures occur, and support rolling upgrades for zero-downtime updates.

**Why not A:** Availability Sets provide high availability but don't include automatic scaling or rolling updates.

**Why not C:** A single VM with alerts can notify you but doesn't automatically scale or replace failed instances.

**Why not D:** Reserved Instances are a pricing model for cost savings, not a compute feature with scaling capabilities.

**Exam Tip:** Scale Sets = automatic scaling + health monitoring + rolling updates for VMs

</details>

---

### Question 7
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** medium

A practice question asks about Azure's Service Level Agreement (SLA). Which statement accurately describes Azure SLAs?

- A) SLAs guarantee 100% uptime for all Azure services
- B) SLAs define the uptime commitments and compensation if Microsoft fails to meet them
- C) SLAs only apply to Enterprise Agreement customers
- D) SLAs cover both Microsoft's responsibilities and customer application bugs

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure SLAs define Microsoft's commitment to service availability (typically 99.9% to 99.99%) and specify service credits customers receive if Microsoft fails to meet the committed uptime.

**Why not A:** No cloud provider guarantees 100% uptime — Azure SLAs typically range from 99.9% to 99.99% depending on the service and configuration.

**Why not C:** SLAs apply to all Azure customers regardless of their subscription type, not just Enterprise Agreement customers.

**Why not D:** SLAs cover the Azure service availability, not customer application code, configuration issues, or design problems.

**Exam Tip:** SLAs are Microsoft's COMMITMENT — know that higher availability configurations (like Availability Zones) have higher SLAs.

</details>

---

### Question 8
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** hard

A global financial services company has strict data residency requirements mandating that European customer data must remain within EU borders. They also need disaster recovery capabilities. Which Azure capability addresses both requirements?

- A) Availability Zones within a single region
- B) Region pairs with both regions located within the EU geography
- C) Global load balancing across all Azure regions
- D) Edge computing with Azure IoT Edge devices

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure region pairs within the same geography (like EU) provide disaster recovery while ensuring data never leaves the required geographic boundary, meeting data residency requirements.

**Why not A:** Availability Zones provide high availability within a region but don't address disaster recovery for region-wide failures.

**Why not C:** Global load balancing would route data to any region, potentially violating data residency requirements.

**Why not D:** IoT Edge is for edge computing scenarios, not data residency and disaster recovery.

**Exam Tip:** Region pairs within a geography help meet data residency requirements while enabling DR

</details>

---

### Question 9
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** easy

For the AZ-900 exam, what does the 'shared responsibility model' in cloud computing define?

- A) How costs are split between cloud customers
- B) How security and management responsibilities are divided between the cloud provider and customer
- C) How bandwidth is shared among cloud tenants
- D) How support tickets are handled between teams

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

The shared responsibility model defines which security and management tasks are handled by the cloud provider (physical security, infrastructure) versus the customer (data, access management, applications), varying by service model.

**Why not A:** Cost sharing between customers isn't addressed by the shared responsibility model — it's about security and management duties.

**Why not C:** Bandwidth allocation is a resource management topic, not related to the shared responsibility model.

**Why not D:** Support ticket handling is an operational process, not what the shared responsibility model addresses.

**Exam Tip:** Shared responsibility shifts with service model: IaaS = most customer responsibility, SaaS = least customer responsibility.

</details>

---

### Question 10
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** hard

A practice exam question presents this scenario: 'An organization wants to use Microsoft 365 for email and collaboration. They're asking which cloud service model Microsoft 365 represents.' What characteristics should you identify to determine the answer?

- A) The customer manages the email server operating system, so it's IaaS
- B) The customer deploys their own application code, so it's PaaS
- C) Microsoft manages everything including the application; customers only use the service, so it's SaaS
- D) The customer can scale the underlying infrastructure, so it's IaaS

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

Microsoft 365 is SaaS — Microsoft manages the entire stack (infrastructure, platform, and application). Customers simply use the email and collaboration applications through a subscription without managing any underlying components.

**Why not A:** In SaaS like Microsoft 365, customers don't manage any servers or operating systems — everything is managed by Microsoft.

**Why not B:** Customers don't deploy code to Microsoft 365 — they use pre-built applications. PaaS would involve deploying custom applications.

**Why not D:** Customers don't manage or directly scale infrastructure in SaaS — they simply consume the service.

**Exam Tip:** Common SaaS examples: Microsoft 365, Salesforce, Dropbox. If you just USE the application, it's SaaS.

</details>

---

### Question 11
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** medium

A retail company experiences a 500% increase in web traffic during the holiday shopping season but only 20% of that traffic during the rest of the year. Which cloud benefit would provide the MOST cost-effective solution for handling this variable workload?

- A) High availability through redundant systems
- B) Elasticity to automatically scale resources based on demand
- C) Geo-distribution across multiple continents
- D) Predictability through fixed monthly pricing

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Elasticity allows the company to automatically scale up during peak holiday traffic and scale down during normal periods, paying only for resources used.

**Why not A:** High availability ensures uptime but doesn't address the cost optimization for variable workloads.

**Why not C:** Geo-distribution helps with latency and regional availability but doesn't solve the seasonal scaling challenge.

**Why not D:** Fixed monthly pricing would result in either over-provisioning (wasting money) or under-provisioning (poor performance).

**Exam Tip:** Elasticity vs scalability: elasticity is automatic, scalability can be manual

</details>

---

### Question 12
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** medium

A financial services company needs to ensure that all Azure resources across multiple subscriptions are compliant with industry regulations. They want to automatically detect non-compliant resources and prevent the deployment of resources that violate security policies. Which Azure service should they implement?

- A) Azure Security Center
- B) Azure Policy
- C) Azure Advisor
- D) Azure Cost Management

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Policy enables you to create, assign, and manage policies that enforce rules and effects over your resources, ensuring compliance with corporate standards. It can audit existing resources and deny non-compliant deployments.

**Why not A:** Azure Security Center provides security recommendations and threat protection but doesn't enforce deployment policies or prevent non-compliant resource creation.

**Why not C:** Azure Advisor provides recommendations for best practices but cannot enforce compliance or block non-compliant deployments.

**Why not D:** Azure Cost Management focuses on cost optimization and budgeting, not compliance enforcement.

**Exam Tip:** Azure Policy = Enforcement and Compliance. It can both audit AND prevent non-compliant deployments.

</details>

---

### Question 13
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** easy

Which Azure compute service should you use when you need complete control over the operating system, including the ability to install custom software and configure specific OS settings?

- A) Azure Functions
- B) Azure App Service
- C) Azure Virtual Machines
- D) Azure Logic Apps

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

Azure Virtual Machines provide IaaS with full control over the operating system, allowing custom software installation, OS configuration, and complete administrative access.

**Why not A:** Azure Functions is serverless - you only deploy code with no access to the underlying OS.

**Why not B:** Azure App Service is PaaS - you deploy applications but don't manage the OS directly.

**Why not D:** Azure Logic Apps is a workflow automation service with no OS access.

**Exam Tip:** VMs = full OS control (IaaS); App Service/Functions = managed platform (PaaS/serverless)

</details>

---

### Question 14
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** hard

You're reviewing a practice exam question that states: 'A company needs to deploy identical environments for development, testing, and production with guaranteed consistency. Which approach should they use?' The options include ARM Templates, Azure Portal, Azure CLI, and Azure PowerShell. What makes ARM Templates the BEST answer?

- A) ARM Templates are faster to execute than other methods
- B) ARM Templates are the only way to deploy resources in Azure
- C) ARM Templates are declarative, idempotent, and version-controllable, ensuring identical deployments
- D) ARM Templates cost less than using other deployment methods

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

ARM Templates provide declarative deployment (specify WHAT, not HOW), are idempotent (same result every time), and can be version-controlled in source repositories — guaranteeing consistent, identical environments across deployments.

**Why not A:** Execution speed isn't the primary advantage — consistency and repeatability are the key benefits for this scenario.

**Why not B:** Azure Portal, CLI, and PowerShell can also deploy resources — ARM Templates aren't the ONLY method.

**Why not D:** All deployment methods use the same underlying Azure Resource Manager API — there's no cost difference in deployment methods.

**Exam Tip:** When questions mention 'consistent,' 'repeatable,' or 'identical' deployments, think Infrastructure as Code (ARM Templates, Bicep).

</details>

---

### Question 15
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** easy

Which consumption-based pricing characteristic is a key benefit of cloud computing?

- A) Customers pay a fixed fee regardless of actual resource usage
- B) Customers pay only for the resources they actually use
- C) Customers must commit to multi-year contracts with no flexibility
- D) Customers purchase hardware upfront and depreciate costs over time

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Consumption-based or pay-as-you-go pricing means customers only pay for resources they actually use, eliminating waste from over-provisioning.

**Why not A:** Fixed fees regardless of usage is the opposite of consumption-based pricing.

**Why not C:** While reserved instances exist, the base cloud model offers flexibility without long-term commitments.

**Why not D:** This describes CapEx/on-premises model, not cloud consumption-based pricing.

**Exam Tip:** Pay-as-you-go means no upfront costs and you stop paying when you stop using

</details>

---

### Question 16
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** easy

What is the primary purpose of Azure Resource Groups?

- A) To provide automatic backup of all resources
- B) To serve as a logical container for managing and organizing related Azure resources
- C) To automatically scale resources based on demand
- D) To encrypt all data stored within Azure resources

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Resource Groups are logical containers that hold related Azure resources, allowing you to manage, organize, and apply policies to them collectively based on lifecycle, permissions, or project.

**Why not A:** Backup is handled by Azure Backup service, not Resource Groups. Resource Groups organize resources but don't provide backup functionality.

**Why not C:** Automatic scaling is configured through services like Virtual Machine Scale Sets or App Service, not through Resource Groups.

**Why not D:** Encryption is managed through Azure Key Vault and individual service encryption settings, not Resource Groups.

**Exam Tip:** Remember: Resource Groups are about ORGANIZATION and MANAGEMENT, not functionality like backup or scaling.

</details>

---

### Question 17
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** easy

On the AZ-900 exam, which type of cloud deployment model would be described as: 'Computing resources owned and operated by a third-party cloud provider, delivered over the internet to multiple organizations'?

- A) Private cloud
- B) Public cloud
- C) Hybrid cloud
- D) Community cloud

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Public cloud is owned and operated by third-party providers (like Microsoft Azure) who deliver computing resources over the internet to multiple customers (organizations) on a shared infrastructure.

**Why not A:** Private cloud is dedicated to a single organization, either on-premises or hosted by a third party exclusively for that organization.

**Why not C:** Hybrid cloud combines public and private clouds, allowing data and applications to move between them.

**Why not D:** Community cloud is shared by several organizations with common concerns — this isn't a commonly tested option on AZ-900.

**Exam Tip:** Public = Shared multi-tenant, Private = Single organization, Hybrid = Combination of both.

</details>

---

### Question 18
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** medium

A startup wants to deploy a web application without managing any infrastructure. They want to upload their code and have it run automatically. Which service model best fits this requirement?

- A) Infrastructure as a Service (IaaS) using virtual machines
- B) Platform as a Service (PaaS) using Azure App Service
- C) Software as a Service (SaaS) using Microsoft 365
- D) On-premises deployment using physical servers

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

PaaS services like Azure App Service allow developers to deploy code without managing servers, operating systems, or infrastructure - just upload code and run.

**Why not A:** IaaS would require the startup to manage VMs, OS patching, and infrastructure, which contradicts their requirement.

**Why not C:** SaaS provides complete applications like email; it's not a platform for deploying custom applications.

**Why not D:** On-premises would require purchasing and managing physical hardware, the opposite of what they want.

**Exam Tip:** PaaS is ideal when developers want to focus on code, not infrastructure

</details>

---

### Question 19
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** easy

On the AZ-900 exam, a question asks about the cloud model where the customer manages the operating system, middleware, and applications while the cloud provider manages virtualization, servers, and networking. Which cloud service model does this describe?

- A) Software as a Service (SaaS)
- B) Platform as a Service (PaaS)
- C) Infrastructure as a Service (IaaS)
- D) Function as a Service (FaaS)

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

IaaS provides virtualized computing resources where customers manage OS, middleware, runtime, and applications, while the provider manages physical infrastructure, virtualization, servers, storage, and networking.

**Why not A:** SaaS provides fully managed applications where the provider manages everything including the application — customers only manage their data and access.

**Why not B:** PaaS manages the runtime and middleware in addition to infrastructure — customers only manage their applications and data.

**Why not D:** FaaS (serverless) manages everything except the function code — even more abstracted than PaaS.

**Exam Tip:** Remember the shared responsibility: IaaS = You manage OS up. PaaS = You manage apps up. SaaS = You manage data only.

</details>

---

### Question 20
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** medium

A company needs to ensure their mission-critical application remains available even if an entire data center within a region experiences an outage. The application cannot tolerate data replication latency to another region. What should they implement?

- A) Deploy to multiple Azure regions using Traffic Manager
- B) Deploy across Availability Zones within a single region
- C) Deploy multiple instances in a single data center
- D) Use Azure Backup to create point-in-time recovery points

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Availability Zones are physically separate data centers within a region, providing protection against data center failures while maintaining low latency for synchronous replication.

**Why not A:** Multi-region deployment would introduce replication latency, which the scenario states is not acceptable.

**Why not C:** Multiple instances in a single data center don't protect against data center-level failures.

**Why not D:** Azure Backup is for data recovery, not high availability during outages.

**Exam Tip:** Availability Zones = data center failure protection; Region pairs = regional disaster protection

</details>

---

### Question 21
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** hard

A manufacturing company needs to run containerized microservices with automatic scaling, self-healing, and rolling updates. They have a dedicated DevOps team experienced with Kubernetes. Which Azure service is MOST appropriate?

- A) Azure Virtual Machines with Docker installed
- B) Azure Container Instances (ACI)
- C) Azure Kubernetes Service (AKS)
- D) Azure App Service with container support

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

AKS provides managed Kubernetes with all the orchestration features requested: automatic scaling, self-healing, rolling updates, and the team already has Kubernetes expertise.

**Why not A:** VMs with Docker provides containers but without orchestration features like automatic scaling and self-healing.

**Why not B:** ACI is for simple, single-container scenarios without orchestration; it lacks the advanced features needed.

**Why not D:** App Service containers work for simpler web apps but don't provide full Kubernetes orchestration capabilities.

**Exam Tip:** AKS = complex orchestration with Kubernetes; ACI = simple, quick container runs

</details>

---

### Question 22
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** medium

During the AZ-900 exam, you encounter a question with two answers that both seem correct. The question asks which Azure service provides 'high availability' for virtual machines. One option mentions Availability Zones and another mentions Availability Sets. How should you approach this?

- A) Choose the first option that appears correct
- B) Identify the specific requirement in the question — datacenter-level vs. rack-level protection
- C) Skip the question and return to it later
- D) Select 'All of the above' if available

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

When multiple options seem correct, look for specific qualifiers in the question. Availability Zones protect against datacenter failures, while Availability Sets protect against rack/hardware failures within a datacenter — the question's context determines the best answer.

**Why not A:** Choosing the first seemingly correct option without analysis may lead to incorrect answers when there's a more specific or better fit.

**Why not C:** While returning later is valid, you should still apply analytical techniques to differentiate between options.

**Why not D:** 'All of the above' should only be selected if explicitly available and truly applicable — don't assume this option exists.

**Exam Tip:** SCOPE matters: Look for words like 'datacenter failure' (Zones) vs. 'hardware failure' (Sets) to identify the correct answer.

</details>

---

### Question 23
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** medium

Your operations team needs to create dashboards showing real-time performance metrics, set up alerts when virtual machine CPU exceeds 80%, and query logs for troubleshooting. Which Azure service provides all these capabilities?

- A) Azure Service Health
- B) Azure Monitor
- C) Azure Advisor
- D) Azure Activity Log

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Monitor is a comprehensive monitoring solution that collects metrics and logs, enables alerting based on thresholds, provides log querying through Log Analytics, and supports custom dashboards.

**Why not A:** Azure Service Health shows Azure platform health and service incidents but doesn't monitor your specific resource performance or enable custom alerts.

**Why not C:** Azure Advisor provides best practice recommendations but doesn't offer real-time monitoring, alerting, or log querying capabilities.

**Why not D:** Azure Activity Log records subscription-level events but doesn't provide resource metrics, custom alerts, or comprehensive monitoring dashboards.

**Exam Tip:** Azure Monitor = Central monitoring hub for metrics, logs, alerts, and dashboards. It's the foundation of Azure observability.

</details>

---

### Question 24
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** hard

A company is evaluating cloud migration and wants to understand the financial model difference. Which statement accurately describes the shift from Capital Expenditure (CapEx) to Operational Expenditure (OpEx) in cloud computing?

- A) CapEx involves monthly subscription fees while OpEx requires upfront hardware purchases
- B) OpEx allows deducting expenses in the year incurred, while CapEx must be depreciated over the asset's useful life
- C) CapEx provides better cash flow management because costs are predictable monthly amounts
- D) OpEx requires larger upfront investments but provides lower total cost of ownership

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

OpEx (operational expenditure) expenses are fully deductible in the year they occur, while CapEx (capital expenditure) must be capitalized and depreciated over time, affecting financial statements differently.

**Why not A:** This is reversed - CapEx is upfront purchases, OpEx is ongoing/subscription fees.

**Why not C:** OpEx provides predictable monthly costs, not CapEx. CapEx has large irregular expenses.

**Why not D:** OpEx typically requires no upfront investment - this describes CapEx characteristics.

**Exam Tip:** CapEx = buy it (depreciate over time), OpEx = rent it (expense immediately)

</details>

---

### Question 25
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** medium

A company's legal department requires that all Azure resources be deployed only in the United States and Europe. Resources deployed in any other region should be automatically denied. Which Azure feature enforces this requirement?

- A) Azure Blueprints
- B) Azure Policy
- C) Role-Based Access Control (RBAC)
- D) Management Groups

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Policy can enforce rules such as allowed locations, automatically denying resource creation in non-compliant regions. This directly addresses the requirement.

**Why not A:** Azure Blueprints package policies, roles, and templates but the enforcement mechanism is Azure Policy.

**Why not C:** RBAC controls who can do what, not what configurations are allowed. It can't restrict regions.

**Why not D:** Management Groups organize subscriptions but don't enforce compliance rules themselves.

**Exam Tip:** Azure Policy enforces WHAT can be done; RBAC enforces WHO can do it

</details>

---

### Question 26
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** easy

What is an Azure Region?

- A) A single data center containing Azure servers
- B) A geographical area containing one or more data centers connected with low-latency network
- C) A virtual network that spans multiple countries
- D) A billing boundary for Azure subscriptions

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

An Azure Region is a geographical area containing at least one, but often multiple, data centers that are nearby and networked together with a low-latency network.

**Why not A:** A region typically contains multiple data centers, not just one, for redundancy and capacity.

**Why not C:** Virtual networks are customer-created networking resources, not Azure's infrastructure organization.

**Why not D:** Billing boundaries are subscriptions and management groups, not regions.

**Exam Tip:** Regions are where you deploy resources; choose based on proximity to users and compliance

</details>

---

### Question 27
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** easy

What does a Resource Lock in Azure prevent?

- A) Unauthorized users from accessing the resource
- B) Accidental deletion or modification of critical resources
- C) Resources from exceeding budget thresholds
- D) Network attacks on the resource

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Resource Locks protect resources from accidental deletion (Delete lock) or any modifications including deletion (ReadOnly lock), regardless of user permissions.

**Why not A:** Access control is managed through RBAC, not Resource Locks. Locks prevent actions even for authorized users.

**Why not C:** Budget controls are managed through Azure Cost Management, not Resource Locks.

**Why not D:** Network security is handled by NSGs, Azure Firewall, and DDoS Protection, not Resource Locks.

**Exam Tip:** Resource Locks override RBAC — even Owners can't delete a locked resource without first removing the lock.

</details>

---

### Question 28
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** medium

A company has two virtual networks in Azure: VNet-A in East US containing their web servers, and VNet-B in East US containing their database servers. By default, can resources in VNet-A communicate with resources in VNet-B?

- A) Yes, all VNets in the same region automatically communicate
- B) Yes, all VNets in the same subscription automatically communicate
- C) No, VNets are isolated by default and require VNet peering or a gateway to communicate
- D) No, cross-VNet communication is not possible in Azure

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

Virtual networks are isolated by design. To enable communication between VNets, you must configure VNet peering or use a VPN/ExpressRoute gateway.

**Why not A:** VNets in the same region are still isolated; they don't automatically communicate.

**Why not B:** VNets in the same subscription are also isolated; subscription doesn't enable connectivity.

**Why not D:** Cross-VNet communication is definitely possible but requires explicit configuration.

**Exam Tip:** VNet isolation is a security feature; peering enables controlled communication between VNets

</details>

---

### Question 29
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** medium

A company needs to connect their on-premises data center to Azure with a dedicated private connection that doesn't traverse the public internet, providing consistent network performance for latency-sensitive applications. Which service should they use?

- A) Azure VPN Gateway with site-to-site VPN
- B) Azure ExpressRoute
- C) Azure Virtual WAN
- D) Azure Bastion

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

ExpressRoute provides a dedicated, private connection from on-premises to Azure through a connectivity provider, bypassing the public internet for consistent, low-latency performance.

**Why not A:** VPN Gateway uses encrypted tunnels over the public internet, which doesn't meet the 'private connection' requirement.

**Why not C:** Virtual WAN is a networking service that can include ExpressRoute but isn't the connection type itself.

**Why not D:** Azure Bastion provides secure RDP/SSH access to VMs, not datacenter connectivity.

**Exam Tip:** ExpressRoute = private, dedicated connection; VPN Gateway = encrypted over internet

</details>

---

### Question 30
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** medium

While taking the AZ-900 exam, you encounter a question asking about scaling. The scenario describes adding more virtual machines to handle increased website traffic. Which type of scaling does this describe?

- A) Vertical scaling (scale up)
- B) Horizontal scaling (scale out)
- C) Auto-scaling threshold
- D) Load balancing

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Horizontal scaling (scale out) involves adding more instances (VMs) to distribute workload. Adding more VMs to handle increased traffic is the definition of scaling out.

**Why not A:** Vertical scaling (scale up) means increasing the capacity of existing resources (more CPU, RAM) — not adding more instances.

**Why not C:** Auto-scaling threshold is a configuration setting that triggers scaling actions, not a type of scaling itself.

**Why not D:** Load balancing distributes traffic across existing resources but doesn't describe the scaling action of adding resources.

**Exam Tip:** Scale OUT = Add more instances (horizontal). Scale UP = Bigger instances (vertical). Both can be automated.

</details>

---

### Question 31
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** hard

A software development company wants to provide their enterprise application to customers without those customers needing to install, maintain, or update anything. Customers should access the application through a web browser and pay a monthly subscription. Which cloud service model describes this offering?

- A) Infrastructure as a Service (IaaS)
- B) Platform as a Service (PaaS)
- C) Software as a Service (SaaS)
- D) Desktop as a Service (DaaS)

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

SaaS delivers complete applications over the internet where the provider manages everything and customers simply use the software through a browser, paying subscription fees.

**Why not A:** IaaS provides virtualized computing resources, not complete applications - customers build their own solutions.

**Why not B:** PaaS provides a development platform, not end-user applications. Developers use PaaS to build applications.

**Why not D:** DaaS provides virtual desktops, not specific applications. The scenario describes application delivery, not desktop virtualization.

**Exam Tip:** SaaS examples: Microsoft 365, Salesforce, Dropbox - complete applications you subscribe to

</details>

---

### Question 32
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** medium

A company wants to implement a consistent naming convention and ensure that all deployed resources include specific metadata tags for owner and cost center. They want non-compliant deployments to be blocked. Which Azure Policy effect should they use?

- A) Audit
- B) AuditIfNotExists
- C) Deny
- D) DeployIfNotExists

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

The Deny effect prevents resource creation or updates that don't comply with the policy rules. This ensures non-compliant resources cannot be deployed.

**Why not A:** Audit creates a warning event in the activity log but allows non-compliant resources to be created — it doesn't block deployments.

**Why not B:** AuditIfNotExists evaluates if a related resource exists and audits if it doesn't, but doesn't block deployments.

**Why not D:** DeployIfNotExists automatically deploys a related resource if it doesn't exist but doesn't block non-compliant primary resource creation.

**Exam Tip:** Policy effects: Deny = Block, Audit = Log only, DeployIfNotExists = Auto-remediate by adding resources.

</details>

---

### Question 33
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** easy

In which cloud service model does the cloud provider manage the operating system, middleware, and runtime, while the customer only manages applications and data?

- A) Infrastructure as a Service (IaaS)
- B) Platform as a Service (PaaS)
- C) Software as a Service (SaaS)
- D) Functions as a Service (FaaS)

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

PaaS provides a platform where customers deploy their applications without managing underlying infrastructure, OS, or runtime - the provider handles everything except applications and data.

**Why not A:** IaaS requires customers to manage the OS, middleware, runtime, and applications - provider only manages virtualization, servers, storage, and networking.

**Why not C:** SaaS is fully managed by the provider; customers only use the application and manage their data within it.

**Why not D:** FaaS is a subset of PaaS focused on serverless functions, but the question describes PaaS characteristics.

**Exam Tip:** Memorize the shared responsibility model layers for IaaS, PaaS, and SaaS

</details>

---

### Question 34
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** medium

Your organization wants to receive alerts when Azure spending approaches a predefined threshold and analyze cost trends across different departments using tags. Which Azure service provides these capabilities?

- A) Azure Pricing Calculator
- B) Azure Cost Management + Billing
- C) Azure Advisor
- D) Azure Resource Manager

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Cost Management + Billing provides cost analysis, budgets with alerts, and the ability to analyze spending by tags, resource groups, or other dimensions to understand cost trends across departments.

**Why not A:** Azure Pricing Calculator estimates costs for new Azure solutions but doesn't monitor actual spending or provide alerts.

**Why not C:** Azure Advisor provides cost optimization recommendations but doesn't offer budget alerts or detailed cost analysis by tags.

**Why not D:** Azure Resource Manager is the deployment and management layer for Azure but doesn't provide cost monitoring or analysis.

**Exam Tip:** Cost Management + Billing = Real-time cost monitoring, budgets, alerts, and analysis. Pricing Calculator = Pre-deployment estimates.

</details>

---

### Question 35
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** easy

Which Azure tool provides personalized recommendations to help optimize your Azure deployment for high availability, security, performance, and cost?

- A) Azure Monitor
- B) Azure Advisor
- C) Azure Service Health
- D) Azure Policy

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Advisor is a personalized cloud consultant that analyzes your resource configuration and usage telemetry to provide recommendations across five categories: Reliability, Security, Performance, Cost, and Operational Excellence.

**Why not A:** Azure Monitor collects and analyzes telemetry data for monitoring but doesn't provide optimization recommendations.

**Why not C:** Azure Service Health provides information about Azure service incidents and planned maintenance, not optimization recommendations.

**Why not D:** Azure Policy enforces organizational standards and compliance but doesn't provide optimization recommendations.

**Exam Tip:** Azure Advisor = Your FREE cloud consultant providing actionable recommendations across 5 pillars.

</details>

---

### Question 36
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** easy

Which cloud computing benefit ensures that resources and applications remain accessible even when individual components fail?

- A) Scalability
- B) High availability
- C) Agility
- D) Elasticity

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

High availability ensures systems remain operational and accessible even during component failures through redundancy and failover mechanisms.

**Why not A:** Scalability refers to the ability to increase capacity to handle growing workloads, not fault tolerance.

**Why not C:** Agility refers to the speed of deploying and configuring resources, not availability during failures.

**Why not D:** Elasticity is the automatic scaling of resources based on demand, not maintaining uptime during failures.

**Exam Tip:** High availability is measured in 'nines' - 99.9% (8.76 hours downtime/year) vs 99.99% (52 minutes/year)

</details>

---

### Question 37
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** easy

What is an Azure Resource Group?

- A) A collection of virtual machines running the same application
- B) A logical container that holds related Azure resources for management and organization
- C) A pricing tier that determines the cost of Azure services
- D) A network security feature that groups firewall rules

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

A Resource Group is a logical container used to group related resources together for unified management, access control, billing tracking, and lifecycle management.

**Why not A:** This describes a VM Scale Set or availability set, not a resource group.

**Why not C:** Pricing tiers are service-specific configurations, not resource groups.

**Why not D:** Network Security Groups (NSGs) manage firewall rules, not resource groups.

**Exam Tip:** Every Azure resource must belong to exactly one resource group; deleting the group deletes all resources in it

</details>

---

### Question 38
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** easy

What is the primary characteristic that distinguishes cloud computing from traditional on-premises data centers?

- A) Cloud computing requires purchasing physical servers upfront
- B) Cloud computing provides on-demand access to computing resources over the internet
- C) Cloud computing eliminates the need for any security measures
- D) Cloud computing only supports Windows-based applications

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Cloud computing is defined by its on-demand, self-service nature where resources are accessed over the internet without requiring direct management of physical infrastructure.

**Why not A:** This describes traditional on-premises computing, not cloud computing. Cloud eliminates upfront hardware purchases.

**Why not C:** Cloud computing still requires security measures; the shared responsibility model defines security obligations.

**Why not D:** Cloud computing supports multiple operating systems and platforms, not just Windows.

**Exam Tip:** Understand the five essential characteristics of cloud computing from NIST definition

</details>

---

### Question 39
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** hard

A multinational corporation has Azure subscriptions managed by different departments. The central IT team needs to ensure that all subscriptions inherit certain governance policies, including required tags for cost allocation and restrictions on which regions resources can be deployed to. The policies must apply automatically to any new subscriptions created in the future. What should they implement?

- A) Apply Azure Policies directly to each subscription individually
- B) Create Management Groups and assign Azure Policies at the Management Group level
- C) Configure Azure Blueprints for each department
- D) Set up Azure Cost Management budgets with policy enforcement

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Management Groups provide a governance scope above subscriptions. Policies assigned at the Management Group level automatically inherit to all subscriptions within that group, including new subscriptions added later.

**Why not A:** Applying policies individually to each subscription doesn't ensure new subscriptions inherit the policies and creates administrative overhead.

**Why not C:** Azure Blueprints help package policies, role assignments, and templates but must still be assigned at a scope; Management Groups provide the inheritance hierarchy needed.

**Why not D:** Azure Cost Management budgets help control spending but don't enforce tagging requirements or region restrictions.

**Exam Tip:** Management Groups enable HIERARCHICAL policy inheritance — policies flow DOWN to all subscriptions and child management groups.

</details>

---

### Question 40
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** hard

A healthcare organization runs critical patient management systems in Azure. They need to be notified immediately if any Azure infrastructure issues could affect their deployed services, view planned maintenance schedules, and access root cause analysis after incidents. Which Azure service should they configure?

- A) Azure Monitor with Application Insights
- B) Azure Service Health
- C) Azure Security Center
- D) Azure Advisor

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Service Health provides personalized alerts about Azure service issues affecting your resources, planned maintenance notifications, and Post-Incident Reviews (PIR) with root cause analysis for past incidents.

**Why not A:** Azure Monitor and Application Insights monitor YOUR applications and resources, not the underlying Azure platform health and maintenance schedules.

**Why not C:** Azure Security Center focuses on security posture and threat protection, not Azure infrastructure incidents or maintenance.

**Why not D:** Azure Advisor provides optimization recommendations but doesn't notify about Azure service incidents or maintenance.

**Exam Tip:** Service Health = Azure platform issues affecting YOUR resources. Monitor = Your application and resource performance.

</details>

---

### Question 41
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** medium

A healthcare organization needs to keep sensitive patient data on their own servers due to strict regulatory requirements, but wants to use cloud services for their public-facing appointment booking website. Which cloud deployment model should they implement?

- A) Public cloud for all workloads
- B) Private cloud for all workloads
- C) Hybrid cloud combining private and public resources
- D) Community cloud shared with other healthcare providers

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

Hybrid cloud allows the organization to keep regulated patient data on-premises while leveraging public cloud benefits for less sensitive workloads like the booking website.

**Why not A:** Public cloud alone may not meet regulatory compliance requirements for sensitive healthcare data.

**Why not B:** Private cloud for everything would work but eliminates the cost and scalability benefits for the public website.

**Why not D:** Community cloud doesn't address the specific requirement of keeping data on their own servers.

**Exam Tip:** Hybrid cloud scenarios often involve regulatory compliance or data sovereignty requirements

</details>

---

### Question 42
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** easy

Which Azure compute option is BEST suited for running code in response to events without provisioning or managing servers?

- A) Azure Virtual Machines
- B) Azure Functions
- C) Azure Dedicated Host
- D) Azure Batch

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Functions is a serverless compute service that runs code in response to events (HTTP requests, queue messages, timers) without requiring server management.

**Why not A:** Virtual Machines require provisioning and managing servers, the opposite of serverless.

**Why not C:** Dedicated Host provides isolated physical servers, requiring significant management.

**Why not D:** Azure Batch is for large-scale parallel computing jobs, not event-driven serverless execution.

**Exam Tip:** Serverless = you only pay for execution time and don't manage any infrastructure

</details>

---

### Question 43
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** easy

Which benefit of cloud computing allows a company to convert large upfront capital expenses for hardware into smaller, ongoing operational expenses?

- A) High availability
- B) Capital expenditure (CapEx) to operational expenditure (OpEx)
- C) Geo-distribution
- D) Fault tolerance

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Cloud computing shifts the cost model from CapEx (buying and owning hardware) to OpEx (paying for services as you use them), improving cash flow and financial flexibility.

**Why not A:** High availability refers to systems being operational and accessible, not the financial model.

**Why not C:** Geo-distribution refers to deploying resources across multiple geographic locations, not cost structure.

**Why not D:** Fault tolerance refers to a system's ability to continue operating despite component failures, not financial considerations.

**Exam Tip:** CapEx to OpEx is a KEY cloud benefit — exam frequently tests this financial advantage of cloud adoption.

</details>

---

### Question 44
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** hard

An enterprise is deploying a new Azure environment and needs to ensure that every new subscription starts with a standard set of policies, role assignments, and resource configurations. They want a repeatable, version-controlled approach that can be updated and redeployed. Which Azure feature best meets this requirement?

- A) Azure Resource Manager Templates alone
- B) Azure Blueprints
- C) Azure Management Groups
- D) Azure Policy Initiatives

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Blueprints enable you to define a repeatable set of Azure resources, policies, role assignments, and ARM templates that can be versioned and deployed to subscriptions consistently, ensuring standard governance.

**Why not A:** ARM Templates deploy resources but don't natively include policy assignments, role assignments, and versioning in a single governance package.

**Why not C:** Management Groups organize subscriptions and enable policy inheritance but don't package resources, roles, and policies together as a deployable artifact.

**Why not D:** Policy Initiatives group multiple policies but don't include resource deployment or role assignments.

**Exam Tip:** Azure Blueprints = Complete governance PACKAGE (policies + roles + templates + artifacts) with versioning and tracking.

</details>

---

### Question 45
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** hard

During your AZ-900 exam, you have 15 minutes remaining and 8 questions left, including 2 that you flagged for review. What is the most effective time management strategy?

- A) Spend equal time (about 2 minutes) on each remaining question
- B) Answer the 6 unflagged questions quickly, then dedicate remaining time to the 2 flagged questions
- C) Skip to the flagged questions first since they need the most attention
- D) Submit the exam immediately to avoid making changes to correct answers

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Answering unflagged questions quickly ensures you capture points for questions you're confident about, then dedicating remaining time to flagged questions maximizes your opportunity to correctly answer challenging questions.

**Why not A:** Equal time distribution doesn't account for question difficulty — confident answers shouldn't take as long as challenging ones.

**Why not C:** Starting with flagged questions risks running out of time before answering easier questions you could have gotten correct quickly.

**Why not D:** Submitting early wastes valuable time that could improve your score on challenging questions.

**Exam Tip:** Never leave questions unanswered — there's no penalty for guessing. Use remaining time strategically on flagged questions.

</details>

---

## Answer Key

| Q | Answer | Domain | Difficulty |
|---|--------|--------|-----------|
| 1 | C | Data, Storage & Identity: Protecting What Matters Most | easy |
| 2 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | easy |
| 3 | B | Azure's Global Backbone: Architecture, Compute & Networking | medium |
| 4 | B | Cloud Computing Foundations: The 'Why' Behind the Cloud | medium |
| 5 | B | Exam Day Victory: Strategies, Practice Tests & Final Review | medium |
| 6 | B | Azure's Global Backbone: Architecture, Compute & Networking | hard |
| 7 | B | Exam Day Victory: Strategies, Practice Tests & Final Review | medium |
| 8 | B | Cloud Computing Foundations: The 'Why' Behind the Cloud | hard |
| 9 | B | Exam Day Victory: Strategies, Practice Tests & Final Review | easy |
| 10 | C | Exam Day Victory: Strategies, Practice Tests & Final Review | hard |
| 11 | B | Cloud Computing Foundations: The 'Why' Behind the Cloud | medium |
| 12 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | medium |
| 13 | C | Azure's Global Backbone: Architecture, Compute & Networking | easy |
| 14 | C | Exam Day Victory: Strategies, Practice Tests & Final Review | hard |
| 15 | B | Cloud Computing Foundations: The 'Why' Behind the Cloud | easy |
| 16 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | easy |
| 17 | B | Exam Day Victory: Strategies, Practice Tests & Final Review | easy |
| 18 | B | Cloud Computing Foundations: The 'Why' Behind the Cloud | medium |
| 19 | C | Exam Day Victory: Strategies, Practice Tests & Final Review | easy |
| 20 | B | Azure's Global Backbone: Architecture, Compute & Networking | medium |
| 21 | C | Azure's Global Backbone: Architecture, Compute & Networking | hard |
| 22 | B | Exam Day Victory: Strategies, Practice Tests & Final Review | medium |
| 23 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | medium |
| 24 | B | Cloud Computing Foundations: The 'Why' Behind the Cloud | hard |
| 25 | B | Azure's Global Backbone: Architecture, Compute & Networking | medium |
| 26 | B | Azure's Global Backbone: Architecture, Compute & Networking | easy |
| 27 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | easy |
| 28 | C | Azure's Global Backbone: Architecture, Compute & Networking | medium |
| 29 | B | Azure's Global Backbone: Architecture, Compute & Networking | medium |
| 30 | B | Exam Day Victory: Strategies, Practice Tests & Final Review | medium |
| 31 | C | Cloud Computing Foundations: The 'Why' Behind the Cloud | hard |
| 32 | C | Governance, Cost Control & Monitoring: Running Azure Like a Pro | medium |
| 33 | B | Cloud Computing Foundations: The 'Why' Behind the Cloud | easy |
| 34 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | medium |
| 35 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | easy |
| 36 | B | Cloud Computing Foundations: The 'Why' Behind the Cloud | easy |
| 37 | B | Azure's Global Backbone: Architecture, Compute & Networking | easy |
| 38 | B | Cloud Computing Foundations: The 'Why' Behind the Cloud | easy |
| 39 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | hard |
| 40 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | hard |
| 41 | C | Cloud Computing Foundations: The 'Why' Behind the Cloud | medium |
| 42 | B | Azure's Global Backbone: Architecture, Compute & Networking | easy |
| 43 | B | Exam Day Victory: Strategies, Practice Tests & Final Review | easy |
| 44 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | hard |
| 45 | B | Exam Day Victory: Strategies, Practice Tests & Final Review | hard |

---

## Domain Score Tracker

| Domain | Questions | Your Score |
|--------|-----------|------------|
| Cloud Computing Foundations: The 'Why' Behind the Cloud | 11 | /11 |
| Azure's Global Backbone: Architecture, Compute & Networking | 11 | /11 |
| Data, Storage & Identity: Protecting What Matters Most | 11 | /11 |
| Governance, Cost Control & Monitoring: Running Azure Like a Pro | 11 | /11 |
| Exam Day Victory: Strategies, Practice Tests & Final Review | 11 | /11 |

*Fill in as you check your answers*
