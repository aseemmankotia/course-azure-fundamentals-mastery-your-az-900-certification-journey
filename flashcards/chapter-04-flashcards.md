## Chapter 4: Governance, Cost Control & Monitoring: Running Azure Like a Pro — Flashcards

| # | Front (Question) | Back (Answer) |
|---|-----------------|---------------|
| 1 | What is Azure Cost Management and Billing? | A suite of tools for monitoring, allocating, and optimizing cloud costs, including budgets, cost analysis, and spending alerts |
| 2 | What is the difference between the Pricing Calculator and TCO Calculator? | Pricing Calculator estimates costs for specific Azure resources; TCO Calculator compares on-premises costs vs. Azure migration costs |
| 3 | What is Azure Policy used for? | Enforcing organizational standards and compliance by creating, assigning, and managing rules that resources must follow |
| 4 | What does RBAC stand for and what does it control? | Role-Based Access Control; it controls WHO can access Azure resources and WHAT actions they can perform |
| 5 | What are the three built-in RBAC roles? | Owner (full access + assign roles), Contributor (full access, no role assignment), Reader (view only) |
| 6 | What are Resource Locks and what are the two types? | Prevent accidental deletion/modification of resources; Types: Delete (prevent deletion) and ReadOnly (prevent changes) |
| 7 | What are Azure Blueprints? | Packages that combine ARM templates, policies, RBAC, and resource groups for repeatable, standardized environment deployments |
| 8 | What are Resource Tags used for? | Organizing resources with metadata (name:value pairs) for cost tracking, automation, and categorization |
| 9 | What is an ARM template? | A JSON file defining infrastructure as code for deploying and configuring Azure resources declaratively |
| 10 | What is Bicep and how does it relate to ARM? | A domain-specific language that simplifies ARM template authoring; it compiles down to ARM JSON |
| 11 | What are the five pillars of Azure Advisor recommendations? | Reliability, Security, Performance, Cost, and Operational Excellence |
| 12 | What does Azure Service Health provide? | Personalized dashboard tracking Azure outages, planned maintenance, and health advisories affecting YOUR resources |
| 13 | What are the three main components of Azure Monitor? | Metrics (numerical performance data), Logs (event records), and Alerts (notifications based on conditions) |
| 14 | What is Log Analytics used for? | Writing queries (KQL) to analyze log data collected by Azure Monitor from multiple sources |
| 15 | What is Application Insights? | An Application Performance Management (APM) service for monitoring live web applications, detecting anomalies, and diagnosing issues |

### Key Terms

| Term | Definition |
|------|-----------|
| RBAC | Role-Based Access Control - authorization system for managing who has access to Azure resources |
| Azure Policy | Service that creates, assigns, and manages policies enforcing rules over resources |
| ARM Template | JSON-formatted file defining Azure infrastructure for consistent, repeatable deployments |
| TCO Calculator | Tool comparing total cost of ownership between on-premises and Azure |
| Azure Monitor | Comprehensive monitoring solution collecting and analyzing telemetry from cloud and on-premises |
| Resource Tags | Key-value pairs applied to resources for organization and cost management |
| KQL | Kusto Query Language - query language used in Log Analytics |

### Memory Tricks
- **"WHO-WHAT-HOW"**: RBAC controls WHO, Policy controls WHAT rules, Blueprints control HOW environments are built
- **"TCP for Costs"**: TCO = Total Cost comparison (migration), Pricing = Point estimates (Azure only), Cost Management = Continuous monitoring
- **"RSCPO" (Risk Security Costs Performance Operations)**: The five Advisor pillars - think "Rescue CPO" like a rescue mission
- **"MAL finds problems"**: Monitor, Advisor, Logs - your troubleshooting trio (Monitor sees, Advisor advises, Logs record)