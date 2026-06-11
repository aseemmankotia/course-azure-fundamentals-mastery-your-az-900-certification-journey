## Chapter 2: Azure's Global Backbone: Architecture, Compute & Networking — Quick Reference

### Core Concepts
| Concept | One-line explanation |
|---------|---------------------|
| Region | Geographic area containing one or more datacenters |
| Region Pair | Two regions 300+ miles apart for disaster recovery replication |
| Availability Zone | Physically separate datacenter within a region (3+ per region) |
| Management Group | Container for managing access/policy across multiple subscriptions |
| Subscription | Billing boundary and access control container for resources |
| Resource Group | Logical container grouping related resources (single region metadata) |
| ARM | Azure Resource Manager - deployment and management layer for all resources |
| VNet | Virtual Network - isolated network in Azure for resource communication |
| VPN Gateway | Encrypted connection between Azure VNet and on-premises network |
| ExpressRoute | Private, dedicated connection to Azure (bypasses public internet) |

### Key Syntax / Commands
```
Resource Hierarchy (Top → Bottom):
Management Groups → Subscriptions → Resource Groups → Resources

Compute Selection Guide:
Full Control     → Virtual Machines
Auto-Scaling VMs → VM Scale Sets  
Web Apps         → App Service
Event-Driven     → Azure Functions (Serverless)
Containers       → ACI (simple) or AKS (orchestrated)
Virtual Desktops → Azure Virtual Desktop
```

### Common Patterns
**Pattern 1: High Availability Deployment**
Deploy resources across 3 Availability Zones within a region for 99.99% SLA

**Pattern 2: Disaster Recovery**
Replicate critical workloads to paired region for geographic redundancy

**Pattern 3: Network Segmentation**
Use VNets with subnets to isolate workloads; connect VNets via peering

### Things to Remember
✅ Resources inherit policies and RBAC from parent Management Groups/Subscriptions
✅ Region pairs receive prioritized recovery during outages; some services auto-replicate
✅ Azure Functions = consumption-based billing (pay only when code runs)
❌ Don't confuse Resource Groups (logical containers) with Availability Zones (physical separation)

### Quick Quiz
1. What connects on-premises to Azure privately without internet? → **ExpressRoute**
2. Minimum Availability Zones per enabled region? → **3**
3. Which compute for containerized microservices at scale? → **AKS**
4. What's the billing boundary in Azure hierarchy? → **Subscription**