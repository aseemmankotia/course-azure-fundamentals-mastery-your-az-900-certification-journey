# AZ-900: Beginners in cloud services — Practice Test 2 Answer Key

| Q | Answer | Domain | Difficulty | Commonly Missed |
|---|--------|--------|-----------|----------------|
| 1 | **B** | Governance, Cost Control & Monitoring: Running Azure Like a Pro | medium | No |
| 2 | **B** | Cloud Computing Foundations: The 'Why' Behind the Cloud | easy | No |
| 3 | **B** | Azure's Global Backbone: Architecture, Compute & Networking | easy | No |
| 4 | **B** | Governance, Cost Control & Monitoring: Running Azure Like a Pro | medium | ⚠️ Yes |
| 5 | **B** | Cloud Computing Foundations: The 'Why' Behind the Cloud | medium | ⚠️ Yes |
| 6 | **B** | Azure's Global Backbone: Architecture, Compute & Networking | hard | ⚠️ Yes |
| 7 | **C** | Cloud Computing Foundations: The 'Why' Behind the Cloud | medium | ⚠️ Yes |
| 8 | **B** | Azure's Global Backbone: Architecture, Compute & Networking | hard | ⚠️ Yes |
| 9 | **C** | Azure's Global Backbone: Architecture, Compute & Networking | medium | No |
| 10 | **B** | Governance, Cost Control & Monitoring: Running Azure Like a Pro | hard | ⚠️ Yes |
| 11 | **C** | Data, Storage & Identity: Protecting What Matters Most | medium | No |
| 12 | **B** | Governance, Cost Control & Monitoring: Running Azure Like a Pro | hard | ⚠️ Yes |
| 13 | **B** | Cloud Computing Foundations: The 'Why' Behind the Cloud | hard | ⚠️ Yes |
| 14 | **B** | Governance, Cost Control & Monitoring: Running Azure Like a Pro | medium | No |
| 15 | **B** | Azure's Global Backbone: Architecture, Compute & Networking | easy | No |
| 16 | **B** | Cloud Computing Foundations: The 'Why' Behind the Cloud | easy | No |
| 17 | **B** | Cloud Computing Foundations: The 'Why' Behind the Cloud | hard | ⚠️ Yes |
| 18 | **B** | Cloud Computing Foundations: The 'Why' Behind the Cloud | medium | ⚠️ Yes |
| 19 | **B** | Governance, Cost Control & Monitoring: Running Azure Like a Pro | easy | No |
| 20 | **B** | Governance, Cost Control & Monitoring: Running Azure Like a Pro | easy | No |
| 21 | **B** | Azure's Global Backbone: Architecture, Compute & Networking | medium | No |
| 22 | **B** | Exam Day Victory: Strategies, Practice Tests & Final Review | medium | ⚠️ Yes |
| 23 | **B** | Azure's Global Backbone: Architecture, Compute & Networking | medium | ⚠️ Yes |
| 24 | **B** | Exam Day Victory: Strategies, Practice Tests & Final Review | medium | No |
| 25 | **B** | Governance, Cost Control & Monitoring: Running Azure Like a Pro | hard | ⚠️ Yes |
| 26 | **B** | Exam Day Victory: Strategies, Practice Tests & Final Review | easy | No |
| 27 | **B** | Cloud Computing Foundations: The 'Why' Behind the Cloud | medium | ⚠️ Yes |
| 28 | **C** | Cloud Computing Foundations: The 'Why' Behind the Cloud | easy | No |
| 29 | **B** | Exam Day Victory: Strategies, Practice Tests & Final Review | hard | ⚠️ Yes |
| 30 | **C** | Governance, Cost Control & Monitoring: Running Azure Like a Pro | medium | ⚠️ Yes |
| 31 | **C** | Cloud Computing Foundations: The 'Why' Behind the Cloud | medium | No |
| 32 | **B** | Azure's Global Backbone: Architecture, Compute & Networking | easy | No |
| 33 | **C** | Azure's Global Backbone: Architecture, Compute & Networking | medium | No |
| 34 | **B** | Azure's Global Backbone: Architecture, Compute & Networking | hard | ⚠️ Yes |
| 35 | **B** | Exam Day Victory: Strategies, Practice Tests & Final Review | easy | No |
| 36 | **B** | Governance, Cost Control & Monitoring: Running Azure Like a Pro | easy | No |
| 37 | **B** | Exam Day Victory: Strategies, Practice Tests & Final Review | hard | ⚠️ Yes |
| 38 | **B** | Exam Day Victory: Strategies, Practice Tests & Final Review | medium | No |
| 39 | **C** | Cloud Computing Foundations: The 'Why' Behind the Cloud | hard | ⚠️ Yes |
| 40 | **B** | Azure's Global Backbone: Architecture, Compute & Networking | medium | No |
| 41 | **B** | Governance, Cost Control & Monitoring: Running Azure Like a Pro | medium | No |
| 42 | **B** | Exam Day Victory: Strategies, Practice Tests & Final Review | medium | No |

---

## Explanations

### Q1. An IT administrator needs to grant a contractor temporary access to view Azure resources and monitor performance metrics, but the contractor should NOT be able to modify any resources or access sensitive data like connection strings. Which built-in RBAC role is MOST appropriate?

**Correct: B** — The Reader role allows viewing all resources and their configurations but cannot make any changes. This provides visibility for monitoring purposes without modification rights. It doesn't expose secrets like connection strings by default.

> 💡 Reader = view everything but change nothing. Use least privilege - don't grant more access than necessary

### Q2. What is the term for the financial model where you pay for cloud resources based on actual consumption rather than upfront capacity purchases?

**Correct: B** — Operational expenditure (OpEx) is the pay-as-you-go model where costs are treated as ongoing operational expenses based on actual resource consumption.

> 💡 Cloud shifts IT spending from CapEx to OpEx — this is a fundamental financial benefit tested frequently

### Q3. What is the primary purpose of Azure Virtual Network (VNet)?

**Correct: B** — Azure Virtual Network provides isolated, private network environments where Azure resources can communicate securely with each other, the internet, and on-premises networks.

> 💡 VNet = your private network in Azure. Resources in a VNet can communicate by default; external access requires configuration

### Q4. A financial services company has Azure subscriptions across multiple departments. The compliance team requires that all resources in the 'Production-Finance' resource group must have a 'DataClassification' tag with specific allowed values: 'Public', 'Internal', 'Confidential', or 'Restricted'. Resources without this tag or with invalid values should be prevented from being created. Which Azure service should the compliance team use?

**Correct: B** — Azure Policy can enforce tagging requirements with specific allowed values at creation time. A policy can deny resource creation if the required tag is missing or contains an invalid value, ensuring compliance before resources are deployed.

> 💡 Azure Policy is the enforcement mechanism for tagging requirements - it can deny, audit, or modify resources based on tag compliance

### Q5. A healthcare organization must comply with strict data residency laws requiring patient data to remain within their country. They also want to leverage cloud services for new applications. Which cloud deployment model should they consider?

**Correct: B** — A private cloud or public cloud deployment in specific regions within their country ensures data residency compliance while still enabling cloud benefits.

> 💡 Data residency requirements often drive cloud deployment decisions — know which models address compliance

### Q6. A company has deployed an application using Azure App Service in the West US region. They need to ensure users in Europe and Asia experience low latency. The application serves mostly static content with some dynamic API calls. Which combination of services provides the BEST solution?

**Correct: B** — Azure CDN caches static content at edge locations globally, while Azure Front Door provides global HTTP load balancing, SSL offloading, and can route API calls optimally.

> 💡 CDN for static content + Front Door for global apps is a common Azure architecture pattern

### Q7. In the shared responsibility model for a PaaS database service, which security responsibility belongs to the CUSTOMER?

**Correct: C** — In PaaS, customers are responsible for securing their data, including encryption, access controls, and data classification within the database.

> 💡 Data security is ALWAYS the customer's responsibility regardless of service model — remember 'your data, your responsibility'

### Q8. A company has two virtual networks in different Azure regions that need to communicate. They want traffic to remain on the Microsoft backbone network and avoid the public internet. What should they configure?

**Correct: B** — Global VNet Peering connects virtual networks across different Azure regions, with traffic routed through Microsoft's backbone network rather than the public internet.

> 💡 VNet Peering (regional) and Global VNet Peering (cross-region) both stay on Microsoft's backbone — no internet traversal

### Q9. A manufacturing company needs to run specialized legacy software that requires Windows Server 2012 and has specific hardware driver requirements. The software vendor doesn't support cloud environments. Which Azure compute option would MOST likely work for this scenario?

**Correct: C** — Azure VMs with dedicated hosts provide full control over the server environment, including OS version and can address hardware isolation requirements for unsupported legacy software.

> 💡 Legacy apps with specific OS/driver needs typically require IaaS (VMs) — PaaS abstracts the OS away

### Q10. A global retail company has noticed unexpected Azure charges. Upon investigation, they discover that developers in the 'Dev-Testing' subscription have been deploying expensive GPU-enabled virtual machines for basic web application testing. Management wants to prevent this while still allowing developers to create standard VM sizes. What is the MOST effective solution?

**Correct: B** — Azure Policy with allowed VM SKU restrictions proactively prevents developers from selecting GPU-enabled VM sizes while still allowing them to deploy approved VM types. This addresses the root cause without impacting productivity.

> 💡 Azure Policy is preventive (stops non-compliant resources), while Budgets and Cost Management are reactive (alert or report after the fact)

### Q11. A media company needs to store large video files that are frequently accessed during the first week after upload but rarely accessed afterward. They want to optimize costs while maintaining quick access when needed. Which Azure Blob Storage strategy should they implement?

**Correct: C** — Lifecycle management policies can automatically transition blobs from Hot to Cool tier based on age, optimizing costs while keeping data readily accessible.

> 💡 Lifecycle management automates tier transitions — set rules based on last access or modification time

### Q12. A healthcare organization is deploying a new Azure environment and must ensure compliance with HIPAA regulations. They need to deploy a complete environment including policies for encryption requirements, role assignments for security teams, and resource groups with proper tagging - all as a single, repeatable package that can be versioned and assigned to multiple subscriptions. Which approach should they use?

**Correct: B** — Azure Blueprints allows packaging of policies, role assignments, ARM templates, and resource groups into a single, versioned artifact. This can be assigned to multiple subscriptions ensuring consistent, repeatable compliance deployments.

> 💡 Azure Blueprints = governance as code. Packages policies + RBAC + ARM templates into versioned, repeatable assignments

### Q13. A company has a Service Level Agreement (SLA) requiring 99.99% uptime for their customer-facing application. They deploy the application in a single Azure region using a single virtual machine. After experiencing an outage, they file a claim. Why might Microsoft NOT provide SLA credits?

**Correct: B** — Single VM deployments typically qualify for lower SLA percentages. To achieve 99.99% SLA, specific deployment configurations like Availability Zones or multiple instances are required.

> 💡 Higher SLA percentages require specific architectures — single VMs have lower SLAs than multi-zone deployments

### Q14. A company wants to track all changes made to Azure resources, including who made changes, what was changed, and when changes occurred. They need to retain this information for 90 days for audit purposes. Which Azure feature provides this capability?

**Correct: B** — Azure Activity Log records all control plane operations (management actions) including who performed actions, what operations were performed, and when they occurred. By default, Activity Log data is retained for 90 days and can be exported for longer retention.

> 💡 Activity Log = WHO did WHAT and WHEN for Azure management operations. Default retention is 90 days

### Q15. What is the purpose of an Azure Resource Group?

**Correct: B** — Resource Groups are logical containers that hold related Azure resources, enabling unified management, access control, and lifecycle management.

> 💡 Resource Groups are LOGICAL containers — they don't provide performance, security, or replication features themselves

### Q16. Which cloud characteristic describes the ability to provision computing resources without requiring human interaction with the service provider?

**Correct: B** — On-demand self-service allows consumers to provision computing capabilities automatically without requiring human interaction with each service provider.

> 💡 On-demand self-service is a key NIST cloud characteristic — no phone calls or tickets needed to provision

### Q17. A company is evaluating cloud service models. They want to deploy a custom application but don't want to manage operating system patches, runtime updates, or scaling infrastructure. However, they need full control over their application code and configuration. Which service model best fits these requirements?

**Correct: B** — PaaS provides a managed platform where the cloud provider handles OS patches, runtime, and scaling, while customers maintain full control over their application code and configuration.

> 💡 PaaS sits between IaaS and SaaS — you manage applications and data, provider manages everything below

### Q18. A retail company experiences massive traffic spikes during Black Friday and holiday seasons but has minimal traffic during summer months. They currently maintain servers sized for peak demand year-round. Which cloud benefit would provide the MOST significant cost advantage for this usage pattern?

**Correct: B** — Elasticity allows the company to scale up during peak seasons and scale down during slow periods, paying only for resources actually needed rather than maintaining peak capacity year-round.

> 💡 Elasticity vs Scalability: Elasticity is automatic/dynamic scaling, while scalability is the ability to add resources

### Q19. A company wants to receive an email notification when their monthly Azure spending reaches 80% of their planned budget. Which Azure feature should they configure?

**Correct: B** — Azure Budgets allow you to set spending thresholds and configure alert conditions at specific percentages (like 80%). When the threshold is reached, notifications are sent via email or action groups.

> 💡 Azure Budgets = threshold alerts for spending. Cost Management = analysis and reporting of costs

### Q20. What is the PRIMARY purpose of Azure Resource Locks?

**Correct: B** — Azure Resource Locks (CanNotDelete and ReadOnly) protect resources from accidental deletion or modification. Even users with Owner permissions cannot delete a resource with a CanNotDelete lock until the lock is removed.

> 💡 Resource Locks protect against accidents, not security threats. Two types: CanNotDelete (prevents deletion) and ReadOnly (prevents all changes)

### Q21. A startup wants to deploy a web application without managing any servers. They expect unpredictable traffic patterns and want to pay only when their code executes. The application processes HTTP requests and completes within seconds. Which compute option is MOST cost-effective?

**Correct: B** — App Service Basic tier charges for the always-running plan regardless of actual traffic.

> 💡 Functions Consumption plan = pay per execution, scale to zero. Perfect for unpredictable, spiky workloads

### Q22. While taking your AZ-900 exam, you encounter a question with the phrase 'which is the BEST solution' and all four options could technically work for the scenario. What exam-taking strategy should you apply?

**Correct: B** — When a question asks for the 'BEST' solution, you must find the option that most completely addresses all requirements while being appropriate for the scenario. Microsoft exams favor solutions that meet requirements efficiently without over-engineering.

> 💡 BEST/MOST questions require comparing ALL options. Look for: meets all requirements + simplest solution + most cost-effective + least management

### Q23. A company needs to deploy a critical application that must survive a complete datacenter failure within a region. They want to minimize latency between application tiers. Which Azure feature should they use?

**Correct: B** — Availability Zones are physically separate datacenters within a region, providing datacenter-level fault tolerance with low latency between zones (typically <2ms).

> 💡 Availability Zones = datacenter failure protection. Availability Sets = rack failure protection

### Q24. During the AZ-900 exam, you encounter a question: 'Which Azure service provides a fully managed NoSQL database with guaranteed single-digit millisecond response times?' You've narrowed it down to Azure Cosmos DB and Azure SQL Database. You're not entirely sure, but you know Azure SQL Database is relational. What is the BEST exam strategy?

**Correct: B** — Use elimination strategy effectively. The question specifically asks for 'NoSQL database' - Azure SQL Database is a relational (SQL) database, not NoSQL. This eliminates it as an option. Azure Cosmos DB is Azure's NoSQL database service with guaranteed low latency.

> 💡 Key exam strategy: Use process of elimination. When a question specifies 'NoSQL', any relational/SQL database is automatically wrong

### Q25. An enterprise with multiple Azure subscriptions wants to analyze costs across all subscriptions, identify spending trends, and receive recommendations for reserved instance purchases based on usage patterns. The finance team needs access to these reports without having access to manage Azure resources. Which solution meets these requirements?

**Correct: B** — Azure Cost Management provides cross-subscription cost analysis, trend identification, and reserved instance recommendations. The Billing Reader role grants access to cost and billing information without any resource management permissions, meeting the separation of duties requirement.

> 💡 Billing Reader role = cost and billing access only. Separates financial visibility from technical resource management

### Q26. You're studying for AZ-900 and see these terms: 'CapEx', 'OpEx', 'elasticity', 'scalability'. Which exam domain do these concepts primarily belong to?

**Correct: B** — CapEx vs OpEx, elasticity, and scalability are fundamental cloud computing concepts. These fall under 'Describe cloud concepts' which covers the benefits and characteristics of cloud computing.

> 💡 Know your exam domains: Cloud Concepts (25-30%), Azure Architecture/Services (35-40%), Management/Governance (30-35%)

### Q27. Which statement accurately describes the difference between scalability and elasticity in cloud computing?

**Correct: B** — Elasticity is the ability to automatically scale resources up or down based on demand, while scalability is the broader capability to increase resources (vertically or horizontally) to handle growth.

> 💡 Elasticity = automatic + dynamic. Scalability = capability to grow. The exam tests this distinction!

### Q28. A startup wants to use email and productivity software without managing any infrastructure, software updates, or licensing complexity. Which cloud service model should they use?

**Correct: C** — SaaS provides ready-to-use software applications like email and productivity tools where the provider manages all infrastructure, updates, and licensing.

> 💡 SaaS = ready-to-use software. Microsoft 365, Salesforce, and Gmail are classic SaaS examples

### Q29. An exam question presents this scenario: 'A company wants to minimize management overhead while running a web application. They don't want to manage operating system updates, scaling, or server maintenance.' The options are Azure VMs, Azure App Service, Azure Kubernetes Service, and Azure Functions. What critical exam skill does this question test?

**Correct: B** — This question tests understanding of how different compute services have different levels of management responsibility. Azure App Service (PaaS) handles OS updates, scaling, and maintenance - matching 'minimize management overhead'. This is the shared responsibility concept applied to compute choices.

> 💡 AZ-900 frequently tests 'management overhead' scenarios. Remember: IaaS = you manage most, PaaS = Azure manages more, SaaS = Azure manages everything

### Q30. An organization has the following Azure hierarchy: Management Group 'Corporate' contains Management Group 'IT-Division', which contains Subscription 'Production-Apps'. A policy denying public IP addresses is assigned at 'Corporate', while a policy allowing public IP addresses is assigned at 'Production-Apps'. What happens when a user tries to create a public IP address in the 'Production-Apps' subscription?

**Correct: C** — Azure Policy evaluates all applicable policies in the hierarchy. If any policy with a 'deny' effect matches, the action is blocked regardless of other policies that might allow it. Deny effects are absolute - they cannot be overridden by allow policies.

> 💡 Remember: In Azure Policy, 'Deny' effects cannot be overridden - if any policy denies an action, it's blocked regardless of other policies

### Q31. A company is concerned about vendor lock-in when migrating to the cloud. Which cloud strategy would BEST address this concern while still gaining cloud benefits?

**Correct: C** — Containerization (like Docker/Kubernetes) and open standards create portable applications that can move between cloud providers, reducing vendor lock-in.

> 💡 Containers and open standards increase portability — this is a key consideration for cloud architecture

### Q32. An Azure region contains multiple datacenters. What is the term for the physical locations containing these datacenters within a region that provide fault isolation?

**Correct: B** — Availability Zones are unique physical locations within an Azure region, each with independent power, cooling, and networking to provide fault isolation.

> 💡 Zones = physical separation within a region. Think of them as separate buildings that could have independent failures

### Q33. A development team needs to run containerized microservices with automatic scaling, rolling updates, and self-healing capabilities. They have Kubernetes expertise and want full control over the orchestration configuration. Which Azure service is MOST appropriate?

**Correct: C** — AKS provides a managed Kubernetes service with full orchestration capabilities including auto-scaling, rolling updates, and self-healing, while giving teams control over Kubernetes configuration.

> 💡 AKS = managed Kubernetes. Container Instances = simple, quick container runs without orchestration

### Q34. A financial institution needs dedicated, private network connectivity between their on-premises datacenter and Azure. They require consistent network latency and bandwidth that doesn't traverse the public internet. The connection must support 10 Gbps throughput. Which Azure service meets these requirements?

**Correct: B** — Azure ExpressRoute provides dedicated, private connectivity that doesn't traverse the public internet, with options for 10 Gbps and higher bandwidth with predictable latency.

> 💡 ExpressRoute = private, dedicated connection (not over internet). VPN Gateway = encrypted tunnel over internet

### Q35. What is the passing score for the AZ-900 certification exam?

**Correct: B** — The AZ-900 exam requires a passing score of 700 out of 1000 points. Microsoft uses a scaled scoring system where scores range from 100 to 1000, with 700 being the minimum passing score for most exams.

> 💡 Passing score is 700/1000. Not all questions may be weighted equally - some questions may be worth more than others

### Q36. Which Azure tool should you use BEFORE deploying resources to estimate the monthly cost of your planned Azure solution?

**Correct: B** — Azure Pricing Calculator is designed for estimating costs BEFORE deployment. You can configure services, regions, and options to get cost estimates for planning and budgeting purposes.

> 💡 Pricing Calculator = estimate BEFORE deployment. Cost Management = analyze AFTER deployment

### Q37. An exam question asks: 'Your company needs to deploy virtual machines that can scale automatically based on demand. Which compute option provides this capability?' The options are: A) Virtual Machine Scale Sets, B) Azure Virtual Machines, C) Azure Container Instances, D) Azure Functions. You know all four can technically 'scale' in some way. How should you approach this question?

**Correct: B** — The question specifically mentions TWO requirements: 'virtual machines' AND 'scale automatically based on demand'. Virtual Machine Scale Sets is specifically designed for automatic scaling of identical VMs. Always match ALL keywords in the question to the answer.

> 💡 Match ALL keywords in the question. When multiple requirements are listed (VMs + auto-scale), the answer must satisfy both

### Q38. Which statement about the AZ-900 exam format is TRUE?

**Correct: B** — The AZ-900 exam allows you to mark questions for review and navigate back to any question before final submission. This lets you manage time effectively and reconsider difficult questions.

> 💡 AZ-900 format: ~45 minutes, ~40-60 questions, no hands-on labs, no penalty for guessing. Always answer every question!

### Q39. A financial services firm uses an on-premises trading application that requires sub-millisecond latency. They want to move analytics workloads to the cloud while keeping the trading application on-premises due to latency requirements. The analytics need access to trading data. Which architecture best describes this approach?

**Correct: C** — Hybrid cloud combines on-premises infrastructure (for latency-sensitive trading) with cloud services (for analytics), with data flowing between them.

> 💡 Hybrid cloud = on-premises + cloud working together. Multi-cloud = multiple cloud providers

### Q40. A network administrator needs to allow web traffic (HTTP/HTTPS) to reach a web server VM while blocking all other inbound traffic from the internet. Which Azure resource should they configure?

**Correct: B** — Network Security Groups filter network traffic to and from Azure resources, allowing you to create rules that permit HTTP (port 80) and HTTPS (port 443) while denying other traffic.

> 💡 NSGs are the basic firewall for Azure VMs — free and simple. Azure Firewall is for advanced scenarios

### Q41. A company running production workloads on Azure VMs experiences an outage during a weekend. The operations team wants to be automatically notified via SMS and email whenever VM CPU usage exceeds 90% for more than 5 minutes or when a VM becomes unavailable. Which Azure service should they configure?

**Correct: B** — Azure Monitor allows creating metric alert rules (CPU > 90% for 5 minutes) and availability alerts. Action groups can be configured to send SMS and email notifications when alerts fire, providing real-time operational awareness.

> 💡 Azure Monitor alerts = real-time notification when metrics cross thresholds. Action groups define WHO gets notified and HOW

### Q42. You're taking the AZ-900 exam and have 15 minutes remaining with 8 questions left, including 3 marked for review. What is the BEST time management strategy?

**Correct: B** — First ensure all questions have answers (remember: no penalty for guessing). Complete the 5 remaining questions efficiently, then return to the 3 marked questions with your remaining time for careful review. Never leave questions unanswered.

> 💡 Time management: Answer ALL questions first (even with guesses), THEN review marked questions. Never leave blanks!

