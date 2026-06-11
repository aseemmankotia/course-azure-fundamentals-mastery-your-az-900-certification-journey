## Chapter 4: Governance, Cost Control & Monitoring: Running Azure Like a Pro — Quick Reference

### Core Concepts
| Concept | One-line explanation |
|---------|---------------------|
| Azure Cost Management | Built-in tool to analyze, monitor, and optimize Azure spending |
| Pricing Calculator | Estimates costs for new Azure deployments before you build |
| TCO Calculator | Compares on-premises costs vs Azure for migration decisions |
| Azure Policy | Enforces organizational rules (what CAN be done) |
| RBAC | Controls WHO can do what with Azure resources |
| Resource Locks | Prevents accidental deletion or modification (CanNotDelete/ReadOnly) |
| Azure Blueprints | Packages policies, RBAC, and templates for repeatable environments |
| Resource Tags | Key-value pairs for organizing and tracking resources |
| ARM Templates | JSON files for Infrastructure as Code deployments |
| Bicep | Simplified, cleaner syntax alternative to ARM templates |
| Azure Advisor | Personalized recommendations across 5 pillars |
| Azure Service Health | Tracks Azure outages affecting YOUR resources |
| Azure Monitor | Collects metrics, logs, and configures alerts |

### Key Syntax / Commands
```
# Common RBAC Roles
Owner → Full access + can assign roles
Contributor → Full access, cannot assign roles
Reader → View only

# Resource Lock Types
CanNotDelete → Can modify, cannot delete
ReadOnly → Cannot modify or delete
```

### Common Patterns
**Pattern 1: Governance Hierarchy**
Management Groups → Subscriptions → Resource Groups → Resources (policies inherit downward)

**Pattern 2: Cost Optimization Workflow**
TCO Calculator (migrate?) → Pricing Calculator (estimate) → Cost Management (optimize ongoing)

### Things to Remember
✅ Advisor's 5 pillars: Reliability, Security, Performance, Cost, Operational Excellence
✅ Tags do NOT inherit from resource groups—apply at each level
❌ Don't confuse Policy (rules/compliance) with RBAC (permissions/access)

### Quick Quiz
1. Which calculator for migration decisions? → TCO Calculator
2. What prevents accidental resource deletion? → Resource Locks (CanNotDelete)