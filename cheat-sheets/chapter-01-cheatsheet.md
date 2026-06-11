## Chapter 1: Cloud Computing Foundations: The 'Why' Behind the Cloud — Quick Reference

### Core Concepts
| Concept | One-line explanation |
|---------|---------------------|
| Cloud Computing | On-demand delivery of IT resources over the internet with pay-as-you-go pricing |
| IaaS | You manage OS, apps, data; provider manages hardware (VMs, storage, networks) |
| PaaS | You manage apps and data; provider manages OS, runtime, and infrastructure |
| SaaS | Provider manages everything; you just use the software (e.g., Microsoft 365) |
| Public Cloud | Resources owned by third-party provider, shared across multiple organizations |
| Private Cloud | Dedicated infrastructure for a single organization (on-premises or hosted) |
| Hybrid Cloud | Combines public and private clouds with orchestration between them |
| Shared Responsibility | Security duties split between cloud provider and customer based on service model |
| CapEx | Capital Expenditure: upfront cost to buy/own physical infrastructure |
| OpEx | Operational Expenditure: ongoing costs for services consumed |

### Key Benefits Memory Aid
```
HA-SAFE-C
├── High Availability  → Uptime guarantees (99.9%+)
├── Scalability        → Grow resources (vertical/horizontal)
├── Agility            → Deploy quickly, iterate fast
├── Fault Tolerance    → Continue operating despite failures
├── Elasticity         → Auto-scale based on demand
└── Consumption-based  → Pay only for what you use
```

### Common Patterns
**Pattern 1: Responsibility Shifts with Service Model**
IaaS = Customer manages most → PaaS = Shared → SaaS = Provider manages most

**Pattern 2: Scaling Types**
Vertical (scale up) = Bigger machine | Horizontal (scale out) = More machines

### Things to Remember
✅ SaaS = least customer responsibility; IaaS = most customer responsibility
✅ Cloud shifts from CapEx (buying servers) to OpEx (paying for usage)
✅ Elasticity is automatic; Scalability can be manual or automatic
❌ Don't confuse Fault Tolerance (survive failures) with Disaster Recovery (restore after major outage)

### Quick Quiz
1. Which model requires you to manage the OS? → **IaaS**
2. CapEx or OpEx: Monthly Azure subscription fees? → **OpEx**
3. Who secures physical datacenters in all cloud models? → **Cloud Provider (always)**