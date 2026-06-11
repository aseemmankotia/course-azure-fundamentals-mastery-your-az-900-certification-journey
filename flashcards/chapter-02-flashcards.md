## Chapter 2: Azure's Global Backbone: Architecture, Compute & Networking — Flashcards

| # | Front (Question) | Back (Answer) |
|---|-----------------|---------------|
| 1 | What is an Azure Region? | A geographical area containing one or more datacenters that are networked together with low-latency connectivity |
| 2 | What are Azure Region Pairs? | Two regions within the same geography (at least 300 miles apart) that provide automatic replication and failover for disaster recovery |
| 3 | What is an Azure Availability Zone? | Physically separate datacenters within an Azure region, each with independent power, cooling, and networking for high availability |
| 4 | What is the correct hierarchy for Azure resource organization from top to bottom? | Management Groups → Subscriptions → Resource Groups → Resources |
| 5 | What is Azure Resource Manager (ARM)? | The deployment and management service for Azure that provides a consistent management layer for creating, updating, and deleting resources |
| 6 | When should you choose Azure Virtual Machines over other compute options? | When you need full control over the operating system, software installation, and configuration (IaaS model) |
| 7 | What are VM Scale Sets used for? | Automatically deploying and managing a group of identical, load-balanced VMs that can scale in or out based on demand |
| 8 | What is Azure App Service? | A fully managed PaaS for hosting web applications, REST APIs, and mobile backends without managing infrastructure |
| 9 | What is the difference between ACI and AKS? | ACI is for running single containers quickly without orchestration; AKS is a managed Kubernetes service for complex container orchestration |
| 10 | What triggers Azure Functions to execute? | Events such as HTTP requests, timers, queue messages, blob storage changes, or other Azure service events |
| 11 | What is Azure Virtual Desktop? | A desktop and app virtualization service that runs in the cloud, providing remote access to Windows desktops and applications |
| 12 | What is an Azure Virtual Network (VNet)? | A logically isolated network in Azure that enables resources to securely communicate with each other, the internet, and on-premises networks |
| 13 | What is the difference between VPN Gateway and ExpressRoute? | VPN Gateway uses encrypted connections over public internet; ExpressRoute provides private, dedicated connections that don't traverse the internet |
| 14 | What is Azure DNS used for? | Hosting DNS domains and managing DNS records using Azure infrastructure, providing name resolution using Microsoft's global network |
| 15 | What is a Resource Group in Azure? | A logical container that holds related Azure resources for an application, allowing you to manage and organize them as a single unit |

### Key Terms

| Term | Definition |
|------|-----------|
| Availability Zone | Unique physical locations within a region with independent infrastructure for fault isolation |
| Azure Resource Manager (ARM) | The unified management layer that handles all API requests for Azure resource operations |
| Virtual Network (VNet) | The fundamental building block for private networks in Azure |
| Serverless Computing | A cloud execution model where the provider manages infrastructure and automatically scales based on demand |
| ExpressRoute | A service providing private, high-bandwidth connections between on-premises infrastructure and Azure |
| Subscription | A billing and access control boundary that contains resource groups and their resources |
| IaaS vs PaaS | Infrastructure as a Service (VMs) gives full control; Platform as a Service (App Service) abstracts infrastructure management |

### Memory Tricks
- **"MRS R"** for hierarchy: **M**anagement Groups → **R**esource **S**ubscriptions → **R**esource Groups → **R**esources
- **"300 Miles Apart, Paired with Heart"** - Region pairs are 300+ miles apart for disaster recovery
- **"Functions are FUN-ctional"** - Azure Functions run when events happen, no servers to FUN-dle (handle)
- **"ACI = A Container Instantly, AKS = A Kubernetes Service"** - Simple containers vs. orchestration
- **"Express yourself Privately"** - ExpressRoute = Private dedicated connection (not public internet like VPN)