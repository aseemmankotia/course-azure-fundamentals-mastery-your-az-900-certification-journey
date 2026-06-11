# AZ-900: Beginners in cloud services — Practice Test 2

> **Time Limit:** 90 minutes
> **Questions:** 42
> **Passing Score:** 700/1000 (70%)
> **Generated:** 6/3/2026

---

## Instructions

- Read each question carefully
- Choose the BEST answer
- All questions are equally weighted
- Do not spend too long on any single question

---

## Questions

### Question 1
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** medium

An IT administrator needs to grant a contractor temporary access to view Azure resources and monitor performance metrics, but the contractor should NOT be able to modify any resources or access sensitive data like connection strings. Which built-in RBAC role is MOST appropriate?

- A) Contributor
- B) Reader
- C) Monitoring Reader
- D) Owner

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

The Reader role allows viewing all resources and their configurations but cannot make any changes. This provides visibility for monitoring purposes without modification rights. It doesn't expose secrets like connection strings by default.

**Why not A:** Contributor allows full resource management including creating, modifying, and deleting resources - too much access for viewing only.

**Why not C:** Monitoring Reader only provides access to monitoring data (metrics, logs) but not to the actual resource configurations the contractor needs to view.

**Why not D:** Owner provides full access including the ability to assign roles to others - far more access than needed and a security risk.

**Exam Tip:** Reader = view everything but change nothing. Use least privilege - don't grant more access than necessary

</details>

---

### Question 2
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** easy

What is the term for the financial model where you pay for cloud resources based on actual consumption rather than upfront capacity purchases?

- A) Capital expenditure (CapEx)
- B) Operational expenditure (OpEx)
- C) Fixed cost model
- D) Depreciation model

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Operational expenditure (OpEx) is the pay-as-you-go model where costs are treated as ongoing operational expenses based on actual resource consumption.

**Why not A:** Capital expenditure (CapEx) involves upfront purchases of physical assets, which is the traditional on-premises model.

**Why not C:** Fixed cost model implies consistent costs regardless of usage, which contradicts the consumption-based cloud model.

**Why not D:** Depreciation model relates to accounting for asset value decline over time, not cloud billing.

**Exam Tip:** Cloud shifts IT spending from CapEx to OpEx — this is a fundamental financial benefit tested frequently

</details>

---

### Question 3
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** easy

What is the primary purpose of Azure Virtual Network (VNet)?

- A) To store virtual machine disk images
- B) To provide isolated network environments for Azure resources
- C) To distribute traffic across multiple regions
- D) To monitor network performance metrics

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Virtual Network provides isolated, private network environments where Azure resources can communicate securely with each other, the internet, and on-premises networks.

**Why not A:** Virtual machine disk images are stored in Azure Storage, not in VNets.

**Why not C:** Traffic distribution across regions is handled by services like Traffic Manager or Front Door, not VNets.

**Why not D:** Network performance monitoring is provided by Network Watcher and Azure Monitor, not VNets themselves.

**Exam Tip:** VNet = your private network in Azure. Resources in a VNet can communicate by default; external access requires configuration

</details>

---

### Question 4
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** medium

A financial services company has Azure subscriptions across multiple departments. The compliance team requires that all resources in the 'Production-Finance' resource group must have a 'DataClassification' tag with specific allowed values: 'Public', 'Internal', 'Confidential', or 'Restricted'. Resources without this tag or with invalid values should be prevented from being created. Which Azure service should the compliance team use?

- A) Azure Blueprints with tag requirements
- B) Azure Policy with tag enforcement
- C) Azure Resource Manager templates with conditions
- D) Microsoft Defender for Cloud recommendations

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Policy can enforce tagging requirements with specific allowed values at creation time. A policy can deny resource creation if the required tag is missing or contains an invalid value, ensuring compliance before resources are deployed.

**Why not A:** Azure Blueprints can include policies but is primarily for deploying a repeatable set of governance tools and resources. The actual tag enforcement would still be done through policies within the blueprint.

**Why not C:** ARM templates define infrastructure but cannot prevent other users from creating non-compliant resources through other methods like the portal or CLI.

**Why not D:** Microsoft Defender for Cloud provides recommendations after resources exist but cannot prevent non-compliant resources from being created in real-time.

**Exam Tip:** Azure Policy is the enforcement mechanism for tagging requirements - it can deny, audit, or modify resources based on tag compliance

</details>

---

### Question 5
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** medium

A healthcare organization must comply with strict data residency laws requiring patient data to remain within their country. They also want to leverage cloud services for new applications. Which cloud deployment model should they consider?

- A) Public cloud only with any available region
- B) Private cloud or public cloud with specific regional deployment
- C) Community cloud shared with competitors
- D) Multi-cloud spanning multiple countries for redundancy

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

A private cloud or public cloud deployment in specific regions within their country ensures data residency compliance while still enabling cloud benefits.

**Why not A:** Using any available region may violate data residency laws if data is stored in regions outside the required country.

**Why not C:** Community cloud with competitors raises data isolation concerns and doesn't specifically address residency requirements.

**Why not D:** Multi-cloud spanning multiple countries would violate data residency requirements by potentially storing data outside the required country.

**Exam Tip:** Data residency requirements often drive cloud deployment decisions — know which models address compliance

</details>

---

### Question 6
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** hard

A company has deployed an application using Azure App Service in the West US region. They need to ensure users in Europe and Asia experience low latency. The application serves mostly static content with some dynamic API calls. Which combination of services provides the BEST solution?

- A) Deploy additional App Service instances in each region with Azure Traffic Manager
- B) Use Azure CDN for static content and Azure Front Door for global load balancing
- C) Implement Azure ExpressRoute connections to Europe and Asia
- D) Enable geo-replication on the App Service plan

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure CDN caches static content at edge locations globally, while Azure Front Door provides global HTTP load balancing, SSL offloading, and can route API calls optimally.

**Why not A:** This would work but is more complex and costly than needed, especially since most content is static.

**Why not C:** ExpressRoute provides private connectivity, not designed for improving end-user latency from public internet.

**Why not D:** App Service plans don't have a geo-replication feature; you would need to deploy separate instances.

**Exam Tip:** CDN for static content + Front Door for global apps is a common Azure architecture pattern

</details>

---

### Question 7
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** medium

In the shared responsibility model for a PaaS database service, which security responsibility belongs to the CUSTOMER?

- A) Physical security of the data center
- B) Patching the database engine
- C) Securing data stored in the database
- D) Managing the underlying hypervisor

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

In PaaS, customers are responsible for securing their data, including encryption, access controls, and data classification within the database.

**Why not A:** Physical security is always the cloud provider's responsibility regardless of service model.

**Why not B:** In PaaS, the provider manages patching of the platform components including the database engine.

**Why not D:** Hypervisor management is the provider's responsibility in all cloud service models.

**Exam Tip:** Data security is ALWAYS the customer's responsibility regardless of service model — remember 'your data, your responsibility'

</details>

---

### Question 8
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** hard

A company has two virtual networks in different Azure regions that need to communicate. They want traffic to remain on the Microsoft backbone network and avoid the public internet. What should they configure?

- A) Network Security Groups with allow rules
- B) Global VNet Peering
- C) Azure Load Balancer
- D) Public IP addresses on both VNets

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Global VNet Peering connects virtual networks across different Azure regions, with traffic routed through Microsoft's backbone network rather than the public internet.

**Why not A:** NSGs control traffic filtering but don't establish connectivity between separate VNets.

**Why not C:** Load Balancer distributes traffic within a region but doesn't connect VNets across regions.

**Why not D:** Public IPs would route traffic over the internet, not keeping it on Microsoft's backbone.

**Exam Tip:** VNet Peering (regional) and Global VNet Peering (cross-region) both stay on Microsoft's backbone — no internet traversal

</details>

---

### Question 9
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** medium

A manufacturing company needs to run specialized legacy software that requires Windows Server 2012 and has specific hardware driver requirements. The software vendor doesn't support cloud environments. Which Azure compute option would MOST likely work for this scenario?

- A) Azure App Service
- B) Azure Functions
- C) Azure Virtual Machines with dedicated hosts
- D) Azure Kubernetes Service

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

Azure VMs with dedicated hosts provide full control over the server environment, including OS version and can address hardware isolation requirements for unsupported legacy software.

**Why not A:** App Service is a PaaS offering that doesn't allow custom OS installations or driver configurations.

**Why not B:** Azure Functions is serverless compute for event-driven code, not for running legacy Windows applications.

**Why not D:** Kubernetes is for containerized applications, which typically isn't compatible with legacy software requiring specific OS versions and drivers.

**Exam Tip:** Legacy apps with specific OS/driver needs typically require IaaS (VMs) — PaaS abstracts the OS away

</details>

---

### Question 10
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** hard

A global retail company has noticed unexpected Azure charges. Upon investigation, they discover that developers in the 'Dev-Testing' subscription have been deploying expensive GPU-enabled virtual machines for basic web application testing. Management wants to prevent this while still allowing developers to create standard VM sizes. What is the MOST effective solution?

- A) Create an Azure Budget with an action group to alert when GPU VM costs are detected
- B) Apply an Azure Policy that restricts allowed VM SKUs to non-GPU sizes
- C) Remove the Contributor role from developers and require VM requests through IT
- D) Use Cost Management to set a spending limit that automatically stops resources

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Policy with allowed VM SKU restrictions proactively prevents developers from selecting GPU-enabled VM sizes while still allowing them to deploy approved VM types. This addresses the root cause without impacting productivity.

**Why not A:** Budgets with alerts only notify after the expensive VMs have already been deployed and costs incurred - this is reactive, not preventive.

**Why not C:** Removing Contributor access would prevent all VM deployments, creating a bottleneck and reducing developer agility unnecessarily.

**Why not D:** Azure subscriptions don't have automatic spending limits that stop resources - Pay-As-You-Go subscriptions can exceed any soft limits set in Cost Management.

**Exam Tip:** Azure Policy is preventive (stops non-compliant resources), while Budgets and Cost Management are reactive (alert or report after the fact)

</details>

---

### Question 11
**Domain:** Data, Storage & Identity: Protecting What Matters Most | **Difficulty:** medium

A media company needs to store large video files that are frequently accessed during the first week after upload but rarely accessed afterward. They want to optimize costs while maintaining quick access when needed. Which Azure Blob Storage strategy should they implement?

- A) Store all files in Hot tier permanently
- B) Store all files in Archive tier with manual retrieval
- C) Use lifecycle management policies to move blobs from Hot to Cool tier automatically
- D) Store all files in Premium tier for maximum performance

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

Lifecycle management policies can automatically transition blobs from Hot to Cool tier based on age, optimizing costs while keeping data readily accessible.

**Why not A:** Hot tier for all data would be unnecessarily expensive for rarely accessed older files.

**Why not B:** Archive tier requires rehydration time (hours) before access, not suitable when quick access is needed.

**Why not D:** Premium tier is for high-performance workloads and would be the most expensive option.

**Exam Tip:** Lifecycle management automates tier transitions — set rules based on last access or modification time

</details>

---

### Question 12
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** hard

A healthcare organization is deploying a new Azure environment and must ensure compliance with HIPAA regulations. They need to deploy a complete environment including policies for encryption requirements, role assignments for security teams, and resource groups with proper tagging - all as a single, repeatable package that can be versioned and assigned to multiple subscriptions. Which approach should they use?

- A) Create individual Azure Policies and assign them to each subscription separately
- B) Use Azure Blueprints to package policies, role assignments, and ARM templates together
- C) Deploy resources using Azure Resource Manager templates with nested templates
- D) Configure Microsoft Defender for Cloud regulatory compliance dashboard

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Blueprints allows packaging of policies, role assignments, ARM templates, and resource groups into a single, versioned artifact. This can be assigned to multiple subscriptions ensuring consistent, repeatable compliance deployments.

**Why not A:** Individual policy assignments would work for the policy portion but wouldn't package role assignments and resource templates together as a versioned, repeatable unit.

**Why not C:** ARM templates can deploy resources but cannot assign Azure Policies or RBAC roles directly as part of the template deployment in the same way Blueprints can.

**Why not D:** Microsoft Defender for Cloud's compliance dashboard monitors and reports on compliance but doesn't deploy the governance resources needed to achieve compliance.

**Exam Tip:** Azure Blueprints = governance as code. Packages policies + RBAC + ARM templates into versioned, repeatable assignments

</details>

---

### Question 13
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** hard

A company has a Service Level Agreement (SLA) requiring 99.99% uptime for their customer-facing application. They deploy the application in a single Azure region using a single virtual machine. After experiencing an outage, they file a claim. Why might Microsoft NOT provide SLA credits?

- A) Microsoft doesn't offer SLAs for virtual machines
- B) Single VM deployments may not meet the SLA requirements for the 99.99% tier
- C) SLA credits only apply to Enterprise Agreement customers
- D) The customer must prove the outage was Microsoft's fault

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Single VM deployments typically qualify for lower SLA percentages. To achieve 99.99% SLA, specific deployment configurations like Availability Zones or multiple instances are required.

**Why not A:** Microsoft does offer SLAs for virtual machines, but the percentage depends on the deployment configuration.

**Why not C:** SLA credits apply to all Azure customers with qualifying subscriptions, not just Enterprise Agreement customers.

**Why not D:** While proof of service impact may be needed, the primary issue is the deployment configuration not qualifying for the claimed SLA tier.

**Exam Tip:** Higher SLA percentages require specific architectures — single VMs have lower SLAs than multi-zone deployments

</details>

---

### Question 14
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** medium

A company wants to track all changes made to Azure resources, including who made changes, what was changed, and when changes occurred. They need to retain this information for 90 days for audit purposes. Which Azure feature provides this capability?

- A) Azure Policy compliance reports
- B) Azure Activity Log
- C) Azure Monitor metrics
- D) Microsoft Defender for Cloud security alerts

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Activity Log records all control plane operations (management actions) including who performed actions, what operations were performed, and when they occurred. By default, Activity Log data is retained for 90 days and can be exported for longer retention.

**Why not A:** Azure Policy compliance reports show whether resources are compliant with policies but don't track who made changes or detailed change history.

**Why not C:** Azure Monitor metrics track performance data like CPU usage and memory, not management operations or change history.

**Why not D:** Microsoft Defender for Cloud alerts focus on security threats and vulnerabilities, not general change tracking for audit purposes.

**Exam Tip:** Activity Log = WHO did WHAT and WHEN for Azure management operations. Default retention is 90 days

</details>

---

### Question 15
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** easy

What is the purpose of an Azure Resource Group?

- A) To automatically scale resources based on demand
- B) To serve as a logical container for managing related Azure resources
- C) To provide network isolation between virtual machines
- D) To replicate data across multiple regions

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Resource Groups are logical containers that hold related Azure resources, enabling unified management, access control, and lifecycle management.

**Why not A:** Auto-scaling is handled by services like Virtual Machine Scale Sets, not Resource Groups.

**Why not C:** Network isolation is provided by Virtual Networks and Network Security Groups, not Resource Groups.

**Why not D:** Data replication is handled by storage replication options and specific data services, not Resource Groups.

**Exam Tip:** Resource Groups are LOGICAL containers — they don't provide performance, security, or replication features themselves

</details>

---

### Question 16
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** easy

Which cloud characteristic describes the ability to provision computing resources without requiring human interaction with the service provider?

- A) Broad network access
- B) On-demand self-service
- C) Resource pooling
- D) Measured service

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

On-demand self-service allows consumers to provision computing capabilities automatically without requiring human interaction with each service provider.

**Why not A:** Broad network access refers to capabilities being available over the network and accessed through standard mechanisms.

**Why not C:** Resource pooling describes how provider resources are pooled to serve multiple consumers using a multi-tenant model.

**Why not D:** Measured service refers to resource usage being monitored, controlled, and reported for transparency.

**Exam Tip:** On-demand self-service is a key NIST cloud characteristic — no phone calls or tickets needed to provision

</details>

---

### Question 17
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** hard

A company is evaluating cloud service models. They want to deploy a custom application but don't want to manage operating system patches, runtime updates, or scaling infrastructure. However, they need full control over their application code and configuration. Which service model best fits these requirements?

- A) Infrastructure as a Service (IaaS)
- B) Platform as a Service (PaaS)
- C) Software as a Service (SaaS)
- D) Functions as a Service (FaaS)

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

PaaS provides a managed platform where the cloud provider handles OS patches, runtime, and scaling, while customers maintain full control over their application code and configuration.

**Why not A:** IaaS would require the company to manage OS patches, runtime updates, and scaling infrastructure themselves.

**Why not C:** SaaS provides ready-made software with minimal customization options, not allowing full control over application code.

**Why not D:** FaaS (serverless functions) is event-driven and suited for discrete functions, not full custom applications requiring configuration control.

**Exam Tip:** PaaS sits between IaaS and SaaS — you manage applications and data, provider manages everything below

</details>

---

### Question 18
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** medium

A retail company experiences massive traffic spikes during Black Friday and holiday seasons but has minimal traffic during summer months. They currently maintain servers sized for peak demand year-round. Which cloud benefit would provide the MOST significant cost advantage for this usage pattern?

- A) High availability through redundant systems
- B) Elasticity to scale resources based on demand
- C) Disaster recovery capabilities
- D) Global distribution of content

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Elasticity allows the company to scale up during peak seasons and scale down during slow periods, paying only for resources actually needed rather than maintaining peak capacity year-round.

**Why not A:** High availability ensures uptime but doesn't address the cost issue of paying for unused capacity during off-peak months.

**Why not C:** Disaster recovery protects against failures but doesn't help with the seasonal demand variation cost problem.

**Why not D:** Global distribution improves performance for geographically dispersed users but doesn't address seasonal scaling costs.

**Exam Tip:** Elasticity vs Scalability: Elasticity is automatic/dynamic scaling, while scalability is the ability to add resources

</details>

---

### Question 19
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** easy

A company wants to receive an email notification when their monthly Azure spending reaches 80% of their planned budget. Which Azure feature should they configure?

- A) Azure Advisor cost recommendations
- B) Azure Budgets with alert conditions
- C) Azure Pricing Calculator estimates
- D) Cost Management cost analysis reports

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Budgets allow you to set spending thresholds and configure alert conditions at specific percentages (like 80%). When the threshold is reached, notifications are sent via email or action groups.

**Why not A:** Azure Advisor provides recommendations for cost optimization but does not send budget threshold alerts.

**Why not C:** Azure Pricing Calculator is for estimating costs before deployment, not for monitoring actual spending.

**Why not D:** Cost Management cost analysis provides reporting and visualization of spending but doesn't send proactive threshold-based alerts - that's the Budgets feature.

**Exam Tip:** Azure Budgets = threshold alerts for spending. Cost Management = analysis and reporting of costs

</details>

---

### Question 20
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** easy

What is the PRIMARY purpose of Azure Resource Locks?

- A) To encrypt resources and prevent unauthorized data access
- B) To prevent accidental deletion or modification of critical resources
- C) To restrict which users can access specific resources
- D) To limit the regions where resources can be deployed

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Resource Locks (CanNotDelete and ReadOnly) protect resources from accidental deletion or modification. Even users with Owner permissions cannot delete a resource with a CanNotDelete lock until the lock is removed.

**Why not A:** Encryption is handled by features like Azure Storage encryption, Azure Disk Encryption, and Key Vault - not resource locks.

**Why not C:** User access restrictions are managed through RBAC (Role-Based Access Control), not resource locks.

**Why not D:** Regional restrictions are enforced through Azure Policy, not resource locks.

**Exam Tip:** Resource Locks protect against accidents, not security threats. Two types: CanNotDelete (prevents deletion) and ReadOnly (prevents all changes)

</details>

---

### Question 21
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** medium

A startup wants to deploy a web application without managing any servers. They expect unpredictable traffic patterns and want to pay only when their code executes. The application processes HTTP requests and completes within seconds. Which compute option is MOST cost-effective?

- A) Azure Virtual Machines with auto-scaling
- B) Azure Functions with Consumption plan
- C) Azure App Service Basic tier
- D) Azure Container Instances

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

App Service Basic tier charges for the always-running plan regardless of actual traffic.

**Why not A:** VMs require minimum running instances even during zero traffic, increasing costs.

**Why not D:** Container Instances charge while containers are running, not ideal for highly variable workloads.

**Exam Tip:** Functions Consumption plan = pay per execution, scale to zero. Perfect for unpredictable, spiky workloads

</details>

---

### Question 22
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** medium

While taking your AZ-900 exam, you encounter a question with the phrase 'which is the BEST solution' and all four options could technically work for the scenario. What exam-taking strategy should you apply?

- A) Select the first option that could work since they're all valid
- B) Look for the option that BEST matches ALL requirements with the LEAST complexity
- C) Choose the newest Azure service since Microsoft promotes current technology
- D) Select the option you've used personally in your own Azure environment

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

When a question asks for the 'BEST' solution, you must find the option that most completely addresses all requirements while being appropriate for the scenario. Microsoft exams favor solutions that meet requirements efficiently without over-engineering.

**Why not A:** Selecting the first valid option ignores that 'BEST' implies comparison - you must evaluate all options against the requirements.

**Why not C:** Newness isn't a determining factor. The best solution matches requirements, not technology age.

**Why not D:** Personal experience may bias you toward familiar solutions that aren't optimal for the scenario described.

**Exam Tip:** BEST/MOST questions require comparing ALL options. Look for: meets all requirements + simplest solution + most cost-effective + least management

</details>

---

### Question 23
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** medium

A company needs to deploy a critical application that must survive a complete datacenter failure within a region. They want to minimize latency between application tiers. Which Azure feature should they use?

- A) Availability Sets with fault domains
- B) Availability Zones
- C) Azure paired regions
- D) Virtual Machine Scale Sets

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Availability Zones are physically separate datacenters within a region, providing datacenter-level fault tolerance with low latency between zones (typically <2ms).

**Why not A:** Availability Sets protect against rack-level failures within a single datacenter, not complete datacenter failures.

**Why not C:** Paired regions are geographically separated, introducing higher latency than zones within the same region.

**Why not D:** Virtual Machine Scale Sets provide scaling capabilities but don't inherently provide datacenter failure protection without additional configuration.

**Exam Tip:** Availability Zones = datacenter failure protection. Availability Sets = rack failure protection

</details>

---

### Question 24
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** medium

During the AZ-900 exam, you encounter a question: 'Which Azure service provides a fully managed NoSQL database with guaranteed single-digit millisecond response times?' You've narrowed it down to Azure Cosmos DB and Azure SQL Database. You're not entirely sure, but you know Azure SQL Database is relational. What is the BEST exam strategy?

- A) Skip the question and return to it at the end of the exam
- B) Select Azure Cosmos DB because SQL Database is relational, not NoSQL
- C) Select Azure SQL Database because it's more commonly used
- D) Leave the question unanswered to avoid losing points for wrong answers

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Use elimination strategy effectively. The question specifically asks for 'NoSQL database' - Azure SQL Database is a relational (SQL) database, not NoSQL. This eliminates it as an option. Azure Cosmos DB is Azure's NoSQL database service with guaranteed low latency.

**Why not A:** While skipping difficult questions can be valid, you've already identified enough information to answer confidently through elimination.

**Why not C:** Popularity doesn't determine correctness. The question requirements (NoSQL) clearly eliminate SQL Database regardless of how common it is.

**Why not D:** AZ-900 has no penalty for wrong answers. Never leave questions unanswered - an educated guess is always better than no answer.

**Exam Tip:** Key exam strategy: Use process of elimination. When a question specifies 'NoSQL', any relational/SQL database is automatically wrong

</details>

---

### Question 25
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** hard

An enterprise with multiple Azure subscriptions wants to analyze costs across all subscriptions, identify spending trends, and receive recommendations for reserved instance purchases based on usage patterns. The finance team needs access to these reports without having access to manage Azure resources. Which solution meets these requirements?

- A) Grant the finance team Reader role on all subscriptions
- B) Configure Azure Cost Management with the Billing Reader role
- C) Create Power BI reports connected to Azure usage APIs
- D) Export cost data to a storage account and share with finance

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Cost Management provides cross-subscription cost analysis, trend identification, and reserved instance recommendations. The Billing Reader role grants access to cost and billing information without any resource management permissions, meeting the separation of duties requirement.

**Why not A:** Reader role provides access to view resource configurations, not optimized for cost analysis, and may expose more information than necessary about technical configurations.

**Why not C:** Power BI integration is possible but requires additional setup and doesn't provide the built-in reserved instance recommendations that Cost Management offers.

**Why not D:** Exporting to storage requires manual processes and doesn't provide the interactive analysis or recommendations available in Cost Management.

**Exam Tip:** Billing Reader role = cost and billing access only. Separates financial visibility from technical resource management

</details>

---

### Question 26
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** easy

You're studying for AZ-900 and see these terms: 'CapEx', 'OpEx', 'elasticity', 'scalability'. Which exam domain do these concepts primarily belong to?

- A) Azure architecture and services
- B) Cloud concepts (describing cloud computing)
- C) Security, privacy, compliance, and trust
- D) Azure pricing and support

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

CapEx vs OpEx, elasticity, and scalability are fundamental cloud computing concepts. These fall under 'Describe cloud concepts' which covers the benefits and characteristics of cloud computing.

**Why not A:** Azure architecture covers specific Azure services, regions, and availability options - not general cloud computing principles.

**Why not C:** Security domain covers compliance frameworks, identity services, and security features - not economic or scaling concepts.

**Why not D:** While CapEx/OpEx relate to costs, these are cloud computing fundamentals, not specific Azure pricing plans or support options.

**Exam Tip:** Know your exam domains: Cloud Concepts (25-30%), Azure Architecture/Services (35-40%), Management/Governance (30-35%)

</details>

---

### Question 27
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** medium

Which statement accurately describes the difference between scalability and elasticity in cloud computing?

- A) Scalability is automatic while elasticity requires manual intervention
- B) Elasticity refers to automatic scaling based on demand while scalability is the ability to add resources
- C) Scalability only applies to storage while elasticity applies to compute
- D) Elasticity is a feature of private clouds while scalability is a public cloud feature

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Elasticity is the ability to automatically scale resources up or down based on demand, while scalability is the broader capability to increase resources (vertically or horizontally) to handle growth.

**Why not A:** This is backwards — elasticity is typically automatic, while manual resource additions fall under general scalability.

**Why not C:** Both scalability and elasticity apply to various resource types including compute, storage, and networking.

**Why not D:** Both concepts apply to all cloud deployment models, not specific to private or public clouds.

**Exam Tip:** Elasticity = automatic + dynamic. Scalability = capability to grow. The exam tests this distinction!

</details>

---

### Question 28
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** easy

A startup wants to use email and productivity software without managing any infrastructure, software updates, or licensing complexity. Which cloud service model should they use?

- A) Infrastructure as a Service (IaaS)
- B) Platform as a Service (PaaS)
- C) Software as a Service (SaaS)
- D) Desktop as a Service (DaaS)

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

SaaS provides ready-to-use software applications like email and productivity tools where the provider manages all infrastructure, updates, and licensing.

**Why not A:** IaaS provides virtual machines and infrastructure, requiring the startup to install and manage their own software.

**Why not B:** PaaS provides a development platform, not ready-to-use business applications like email.

**Why not D:** DaaS provides virtual desktops, which is more than needed for just email and productivity software access.

**Exam Tip:** SaaS = ready-to-use software. Microsoft 365, Salesforce, and Gmail are classic SaaS examples

</details>

---

### Question 29
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** hard

An exam question presents this scenario: 'A company wants to minimize management overhead while running a web application. They don't want to manage operating system updates, scaling, or server maintenance.' The options are Azure VMs, Azure App Service, Azure Kubernetes Service, and Azure Functions. What critical exam skill does this question test?

- A) Knowledge of Azure pricing tiers for each service
- B) Understanding of shared responsibility model and management levels across compute services
- C) Familiarity with Azure Portal navigation
- D) Knowledge of Azure networking requirements for web applications

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

This question tests understanding of how different compute services have different levels of management responsibility. Azure App Service (PaaS) handles OS updates, scaling, and maintenance - matching 'minimize management overhead'. This is the shared responsibility concept applied to compute choices.

**Why not A:** The question focuses on management overhead, not cost. Pricing isn't mentioned in the requirements.

**Why not C:** Portal navigation is practical knowledge but the question tests architectural understanding of service characteristics.

**Why not D:** While networking is important, the question specifically focuses on management and maintenance responsibilities, not network configuration.

**Exam Tip:** AZ-900 frequently tests 'management overhead' scenarios. Remember: IaaS = you manage most, PaaS = Azure manages more, SaaS = Azure manages everything

</details>

---

### Question 30
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** medium

An organization has the following Azure hierarchy: Management Group 'Corporate' contains Management Group 'IT-Division', which contains Subscription 'Production-Apps'. A policy denying public IP addresses is assigned at 'Corporate', while a policy allowing public IP addresses is assigned at 'Production-Apps'. What happens when a user tries to create a public IP address in the 'Production-Apps' subscription?

- A) The creation succeeds because subscription-level policies override management group policies
- B) The creation fails because the deny policy at the higher level takes precedence
- C) The creation fails because all policies are evaluated and deny effects always block actions
- D) Azure prompts the user to choose which policy to apply

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

Azure Policy evaluates all applicable policies in the hierarchy. If any policy with a 'deny' effect matches, the action is blocked regardless of other policies that might allow it. Deny effects are absolute - they cannot be overridden by allow policies.

**Why not A:** Subscription-level policies do not override management group policies. All policies in the hierarchy are evaluated together.

**Why not B:** While the outcome is correct (creation fails), the reasoning about 'higher level precedence' is incorrect. It's specifically because deny effects cannot be overridden, not because of hierarchy position.

**Why not D:** Azure Policy evaluation is automatic and deterministic - users are not prompted to choose between conflicting policies.

**Exam Tip:** Remember: In Azure Policy, 'Deny' effects cannot be overridden - if any policy denies an action, it's blocked regardless of other policies

</details>

---

### Question 31
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** medium

A company is concerned about vendor lock-in when migrating to the cloud. Which cloud strategy would BEST address this concern while still gaining cloud benefits?

- A) Moving all workloads to a single cloud provider for simplicity
- B) Using proprietary services for maximum integration
- C) Adopting containerization and open standards where possible
- D) Signing long-term committed contracts for better pricing

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

Containerization (like Docker/Kubernetes) and open standards create portable applications that can move between cloud providers, reducing vendor lock-in.

**Why not A:** Single provider dependency increases lock-in risk, not reduces it.

**Why not B:** Proprietary services often increase lock-in by creating dependencies on provider-specific features.

**Why not D:** Long-term contracts may provide cost benefits but don't address portability and can increase lock-in.

**Exam Tip:** Containers and open standards increase portability — this is a key consideration for cloud architecture

</details>

---

### Question 32
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** easy

An Azure region contains multiple datacenters. What is the term for the physical locations containing these datacenters within a region that provide fault isolation?

- A) Resource Groups
- B) Availability Zones
- C) Management Groups
- D) Subscriptions

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Availability Zones are unique physical locations within an Azure region, each with independent power, cooling, and networking to provide fault isolation.

**Why not A:** Resource Groups are logical containers for organizing resources, not physical locations.

**Why not C:** Management Groups are organizational containers for managing access and policies across subscriptions.

**Why not D:** Subscriptions are billing and access control boundaries, not physical infrastructure locations.

**Exam Tip:** Zones = physical separation within a region. Think of them as separate buildings that could have independent failures

</details>

---

### Question 33
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** medium

A development team needs to run containerized microservices with automatic scaling, rolling updates, and self-healing capabilities. They have Kubernetes expertise and want full control over the orchestration configuration. Which Azure service is MOST appropriate?

- A) Azure Container Instances
- B) Azure App Service for Containers
- C) Azure Kubernetes Service (AKS)
- D) Azure Virtual Machines with Docker

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

AKS provides a managed Kubernetes service with full orchestration capabilities including auto-scaling, rolling updates, and self-healing, while giving teams control over Kubernetes configuration.

**Why not A:** Container Instances is for simple, single-container scenarios without orchestration features.

**Why not B:** App Service for Containers provides simpler container hosting without Kubernetes-level orchestration control.

**Why not D:** VMs with Docker would require manual management of orchestration, updates, and scaling.

**Exam Tip:** AKS = managed Kubernetes. Container Instances = simple, quick container runs without orchestration

</details>

---

### Question 34
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** hard

A financial institution needs dedicated, private network connectivity between their on-premises datacenter and Azure. They require consistent network latency and bandwidth that doesn't traverse the public internet. The connection must support 10 Gbps throughput. Which Azure service meets these requirements?

- A) Azure VPN Gateway with site-to-site VPN
- B) Azure ExpressRoute
- C) Azure Virtual WAN with VPN hub
- D) Azure Peering Service

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure ExpressRoute provides dedicated, private connectivity that doesn't traverse the public internet, with options for 10 Gbps and higher bandwidth with predictable latency.

**Why not A:** VPN Gateway creates encrypted tunnels over the public internet, not meeting the private connectivity requirement.

**Why not C:** Virtual WAN with VPN hub still uses VPN technology over the internet for branch connectivity.

**Why not D:** Azure Peering Service optimizes routing to Microsoft services but doesn't provide dedicated private connectivity.

**Exam Tip:** ExpressRoute = private, dedicated connection (not over internet). VPN Gateway = encrypted tunnel over internet

</details>

---

### Question 35
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** easy

What is the passing score for the AZ-900 certification exam?

- A) 70% (70 out of 100)
- B) 700 out of 1000 points
- C) 80% (80 out of 100)
- D) 650 out of 1000 points

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

The AZ-900 exam requires a passing score of 700 out of 1000 points. Microsoft uses a scaled scoring system where scores range from 100 to 1000, with 700 being the minimum passing score for most exams.

**Why not A:** While 700/1000 is similar to 70%, Microsoft doesn't express the passing score as a percentage.

**Why not C:** 80% (or 800/1000) would be a higher threshold than required for AZ-900.

**Why not D:** 650 is below the passing threshold of 700 for Azure fundamentals exams.

**Exam Tip:** Passing score is 700/1000. Not all questions may be weighted equally - some questions may be worth more than others

</details>

---

### Question 36
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** easy

Which Azure tool should you use BEFORE deploying resources to estimate the monthly cost of your planned Azure solution?

- A) Azure Cost Management
- B) Azure Pricing Calculator
- C) Azure Budgets
- D) Azure Advisor

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Pricing Calculator is designed for estimating costs BEFORE deployment. You can configure services, regions, and options to get cost estimates for planning and budgeting purposes.

**Why not A:** Azure Cost Management analyzes actual spending on resources that have already been deployed, not estimates for planned resources.

**Why not C:** Azure Budgets monitors spending against thresholds for existing resources, not cost estimation for new deployments.

**Why not D:** Azure Advisor provides recommendations for existing resources including cost optimization suggestions, but doesn't estimate costs for planned deployments.

**Exam Tip:** Pricing Calculator = estimate BEFORE deployment. Cost Management = analyze AFTER deployment

</details>

---

### Question 37
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** hard

An exam question asks: 'Your company needs to deploy virtual machines that can scale automatically based on demand. Which compute option provides this capability?' The options are: A) Virtual Machine Scale Sets, B) Azure Virtual Machines, C) Azure Container Instances, D) Azure Functions. You know all four can technically 'scale' in some way. How should you approach this question?

- A) Select Azure Functions because it's serverless and scales automatically
- B) Select Virtual Machine Scale Sets because the question specifically mentions 'virtual machines' and 'scale automatically'
- C) Select Azure Virtual Machines because it's the most flexible option
- D) Select Azure Container Instances because containers are more efficient than VMs

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

The question specifically mentions TWO requirements: 'virtual machines' AND 'scale automatically based on demand'. Virtual Machine Scale Sets is specifically designed for automatic scaling of identical VMs. Always match ALL keywords in the question to the answer.

**Why not A:** Azure Functions does scale automatically but doesn't deploy 'virtual machines' - it's serverless compute. The question explicitly asks about VMs.

**Why not C:** Standard Azure Virtual Machines require manual scaling intervention or additional configuration - they don't inherently 'scale automatically based on demand'.

**Why not D:** Container Instances are containers, not virtual machines. The question specifically asks for virtual machines.

**Exam Tip:** Match ALL keywords in the question. When multiple requirements are listed (VMs + auto-scale), the answer must satisfy both

</details>

---

### Question 38
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** medium

Which statement about the AZ-900 exam format is TRUE?

- A) The exam has a time limit of 120 minutes and includes hands-on lab exercises
- B) You can mark questions for review and navigate back to them before submitting
- C) The exam penalizes incorrect answers, so you should skip questions you're unsure about
- D) Once you answer a question, you cannot change your answer

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

The AZ-900 exam allows you to mark questions for review and navigate back to any question before final submission. This lets you manage time effectively and reconsider difficult questions.

**Why not A:** AZ-900 is typically 60 minutes (with possible additional time for non-native English speakers) and does NOT include hands-on labs - it's multiple choice and scenario-based questions only.

**Why not C:** There is NO penalty for wrong answers on AZ-900. You should always answer every question, even if guessing.

**Why not D:** You CAN change answers before final submission. The exam allows full navigation until you click the final submit button.

**Exam Tip:** AZ-900 format: ~45 minutes, ~40-60 questions, no hands-on labs, no penalty for guessing. Always answer every question!

</details>

---

### Question 39
**Domain:** Cloud Computing Foundations: The 'Why' Behind the Cloud | **Difficulty:** hard

A financial services firm uses an on-premises trading application that requires sub-millisecond latency. They want to move analytics workloads to the cloud while keeping the trading application on-premises due to latency requirements. The analytics need access to trading data. Which architecture best describes this approach?

- A) Public cloud only
- B) Private cloud only
- C) Hybrid cloud
- D) Multi-cloud

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: C**

Hybrid cloud combines on-premises infrastructure (for latency-sensitive trading) with cloud services (for analytics), with data flowing between them.

**Why not A:** Public cloud only would require moving the latency-sensitive trading application, which doesn't meet requirements.

**Why not B:** Private cloud only doesn't leverage public cloud benefits for the analytics workloads.

**Why not D:** Multi-cloud refers to using multiple public cloud providers, not combining on-premises with cloud.

**Exam Tip:** Hybrid cloud = on-premises + cloud working together. Multi-cloud = multiple cloud providers

</details>

---

### Question 40
**Domain:** Azure's Global Backbone: Architecture, Compute & Networking | **Difficulty:** medium

A network administrator needs to allow web traffic (HTTP/HTTPS) to reach a web server VM while blocking all other inbound traffic from the internet. Which Azure resource should they configure?

- A) Azure Firewall
- B) Network Security Group (NSG)
- C) Azure DDoS Protection
- D) Azure Private Link

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Network Security Groups filter network traffic to and from Azure resources, allowing you to create rules that permit HTTP (port 80) and HTTPS (port 443) while denying other traffic.

**Why not A:** Azure Firewall provides advanced filtering but is more complex and costly than needed for basic port-based filtering.

**Why not C:** Azure DDoS Protection guards against distributed denial of service attacks, not general traffic filtering.

**Why not D:** Azure Private Link provides private connectivity to services, not inbound traffic filtering.

**Exam Tip:** NSGs are the basic firewall for Azure VMs — free and simple. Azure Firewall is for advanced scenarios

</details>

---

### Question 41
**Domain:** Governance, Cost Control & Monitoring: Running Azure Like a Pro | **Difficulty:** medium

A company running production workloads on Azure VMs experiences an outage during a weekend. The operations team wants to be automatically notified via SMS and email whenever VM CPU usage exceeds 90% for more than 5 minutes or when a VM becomes unavailable. Which Azure service should they configure?

- A) Azure Advisor with high availability recommendations
- B) Azure Monitor with alert rules and action groups
- C) Azure Service Health notifications
- D) Log Analytics workspace with saved queries

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

Azure Monitor allows creating metric alert rules (CPU > 90% for 5 minutes) and availability alerts. Action groups can be configured to send SMS and email notifications when alerts fire, providing real-time operational awareness.

**Why not A:** Azure Advisor provides recommendations for improving availability but doesn't monitor real-time metrics or send alerts for threshold breaches.

**Why not C:** Azure Service Health notifies about Azure platform issues affecting your resources, not about performance metrics or thresholds within your own VMs.

**Why not D:** Log Analytics with saved queries can analyze data but doesn't provide real-time alerting - you need Azure Monitor alerts configured on top of the data.

**Exam Tip:** Azure Monitor alerts = real-time notification when metrics cross thresholds. Action groups define WHO gets notified and HOW

</details>

---

### Question 42
**Domain:** Exam Day Victory: Strategies, Practice Tests & Final Review | **Difficulty:** medium

You're taking the AZ-900 exam and have 15 minutes remaining with 8 questions left, including 3 marked for review. What is the BEST time management strategy?

- A) Spend equal time on all 8 questions (about 1.5 minutes each)
- B) Answer the 5 unmarked questions quickly, then use remaining time for the 3 marked questions
- C) Focus only on the 3 marked questions since those are the ones you found difficult
- D) Submit the exam immediately since you've already answered most questions

<details>
<summary>📖 Answer & Explanation</summary>

**Correct Answer: B**

First ensure all questions have answers (remember: no penalty for guessing). Complete the 5 remaining questions efficiently, then return to the 3 marked questions with your remaining time for careful review. Never leave questions unanswered.

**Why not A:** Equal time allocation doesn't account for question difficulty - unmarked questions should be faster since you didn't flag them as problematic.

**Why not C:** Ignoring the 5 remaining questions risks leaving them unanswered. All questions must be answered before focusing on review.

**Why not D:** With 15 minutes and 8 questions, there's adequate time to complete all questions thoughtfully. Premature submission wastes valuable review time.

**Exam Tip:** Time management: Answer ALL questions first (even with guesses), THEN review marked questions. Never leave blanks!

</details>

---

## Answer Key

| Q | Answer | Domain | Difficulty |
|---|--------|--------|-----------|
| 1 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | medium |
| 2 | B | Cloud Computing Foundations: The 'Why' Behind the Cloud | easy |
| 3 | B | Azure's Global Backbone: Architecture, Compute & Networking | easy |
| 4 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | medium |
| 5 | B | Cloud Computing Foundations: The 'Why' Behind the Cloud | medium |
| 6 | B | Azure's Global Backbone: Architecture, Compute & Networking | hard |
| 7 | C | Cloud Computing Foundations: The 'Why' Behind the Cloud | medium |
| 8 | B | Azure's Global Backbone: Architecture, Compute & Networking | hard |
| 9 | C | Azure's Global Backbone: Architecture, Compute & Networking | medium |
| 10 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | hard |
| 11 | C | Data, Storage & Identity: Protecting What Matters Most | medium |
| 12 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | hard |
| 13 | B | Cloud Computing Foundations: The 'Why' Behind the Cloud | hard |
| 14 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | medium |
| 15 | B | Azure's Global Backbone: Architecture, Compute & Networking | easy |
| 16 | B | Cloud Computing Foundations: The 'Why' Behind the Cloud | easy |
| 17 | B | Cloud Computing Foundations: The 'Why' Behind the Cloud | hard |
| 18 | B | Cloud Computing Foundations: The 'Why' Behind the Cloud | medium |
| 19 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | easy |
| 20 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | easy |
| 21 | B | Azure's Global Backbone: Architecture, Compute & Networking | medium |
| 22 | B | Exam Day Victory: Strategies, Practice Tests & Final Review | medium |
| 23 | B | Azure's Global Backbone: Architecture, Compute & Networking | medium |
| 24 | B | Exam Day Victory: Strategies, Practice Tests & Final Review | medium |
| 25 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | hard |
| 26 | B | Exam Day Victory: Strategies, Practice Tests & Final Review | easy |
| 27 | B | Cloud Computing Foundations: The 'Why' Behind the Cloud | medium |
| 28 | C | Cloud Computing Foundations: The 'Why' Behind the Cloud | easy |
| 29 | B | Exam Day Victory: Strategies, Practice Tests & Final Review | hard |
| 30 | C | Governance, Cost Control & Monitoring: Running Azure Like a Pro | medium |
| 31 | C | Cloud Computing Foundations: The 'Why' Behind the Cloud | medium |
| 32 | B | Azure's Global Backbone: Architecture, Compute & Networking | easy |
| 33 | C | Azure's Global Backbone: Architecture, Compute & Networking | medium |
| 34 | B | Azure's Global Backbone: Architecture, Compute & Networking | hard |
| 35 | B | Exam Day Victory: Strategies, Practice Tests & Final Review | easy |
| 36 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | easy |
| 37 | B | Exam Day Victory: Strategies, Practice Tests & Final Review | hard |
| 38 | B | Exam Day Victory: Strategies, Practice Tests & Final Review | medium |
| 39 | C | Cloud Computing Foundations: The 'Why' Behind the Cloud | hard |
| 40 | B | Azure's Global Backbone: Architecture, Compute & Networking | medium |
| 41 | B | Governance, Cost Control & Monitoring: Running Azure Like a Pro | medium |
| 42 | B | Exam Day Victory: Strategies, Practice Tests & Final Review | medium |

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
