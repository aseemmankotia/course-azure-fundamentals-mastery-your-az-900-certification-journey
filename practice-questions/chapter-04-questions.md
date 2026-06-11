## Chapter 4: Governance, Cost Control & Monitoring: Running Azure Like a Pro — Practice Questions

### Multiple Choice

**Q1.** Your organization wants to ensure that all virtual machines deployed in Azure have a specific tag called "CostCenter" applied. Which Azure service should you use to enforce this requirement?

A) Azure Monitor
B) Azure Policy
C) Azure Advisor
D) Azure Service Health

<details>
<summary>Answer</summary>

**Correct: B**

Azure Policy is the correct service for enforcing organizational standards and compliance requirements, including mandatory tagging. Azure Monitor is for collecting and analyzing telemetry data. Azure Advisor provides recommendations but does not enforce rules. Azure Service Health tracks Azure outages and planned maintenance.

</details>

---

**Q2.** A company is planning to migrate their on-premises servers to Azure and wants to compare the costs of running workloads on-premises versus in Azure over five years. Which tool should they use?

A) Azure Pricing Calculator
B) Azure Cost Management
C) Total Cost of Ownership (TCO) Calculator
D) Azure Advisor

<details>
<summary>Answer</summary>

**Correct: C**

The TCO Calculator is specifically designed to estimate cost savings by comparing on-premises infrastructure costs with Azure cloud costs over time. The Pricing Calculator estimates costs for new Azure resources. Azure Cost Management analyzes existing Azure spending. Azure Advisor provides recommendations but not migration cost comparisons.

</details>

---

**Q3.** Which Azure Monitor feature would you use to query and analyze log data collected from multiple Azure resources?

A) Application Insights
B) Azure Metrics
C) Log Analytics
D) Azure Alerts

<details>
<summary>Answer</summary>

**Correct: C**

Log Analytics is the Azure Monitor feature that allows you to write queries to analyze log data collected from various sources. Application Insights is specifically for application performance monitoring. Azure Metrics handles numerical time-series data. Azure Alerts notify you when conditions are met but don't provide query capabilities.

</details>

---

**Q4.** Your security team wants to prevent accidental deletion of a production storage account while still allowing administrators to modify its configuration. Which type of resource lock should be applied?

A) ReadOnly lock
B) Delete lock
C) CanNotModify lock
D) Full lock

<details>
<summary>Answer</summary>

**Correct: B**

A Delete lock prevents the resource from being deleted but allows modifications to the resource configuration. A ReadOnly lock would prevent both deletion and modifications, which is more restrictive than required. CanNotModify and Full lock are not valid Azure resource lock types.

</details>

---

**Q5.** Which Azure Advisor recommendation category helps you improve the performance of your applications?

A) Cost
B) Security
C) Reliability
D) Performance

<details>
<summary>Answer</summary>

**Correct: D**

Azure Advisor provides recommendations across five pillars: Cost, Security, Reliability, Operational Excellence, and Performance. The Performance category specifically focuses on improving the speed and responsiveness of your applications. Cost focuses on spending optimization. Security addresses vulnerabilities. Reliability focuses on ensuring business continuity.

</details>

---

### True / False

**Q6.** Bicep templates are a domain-specific language that compiles into ARM templates and provide a simpler syntax for deploying Azure resources. — **True / False**

*True. Bicep is a domain-specific language (DSL) created by Microsoft that provides a cleaner, more readable syntax compared to JSON-based ARM templates. When you deploy a Bicep template, it is automatically transpiled (converted) into an ARM template behind the scenes, making it fully compatible with Azure Resource Manager.*

---

**Q7.** Role-Based Access Control (RBAC) in Azure can only be assigned at the subscription level. — **True / False**

*False. Azure RBAC can be assigned at multiple levels (scopes) including management groups, subscriptions, resource groups, and individual resources. RBAC assignments follow inheritance, meaning permissions granted at a higher level (like a subscription) are inherited by lower levels (like resource groups and resources within that subscription).*

---

### Short Answer

**Q8.** What are the five pillars of recommendations provided by Azure Advisor?

<details>
<summary>Answer</summary>

The five pillars of Azure Advisor recommendations are:
1. **Cost** - Optimize and reduce Azure spending
2. **Security** - Detect threats and vulnerabilities
3. **Reliability** - Ensure business continuity
4. **Operational Excellence** - Improve process and workflow efficiency
5. **Performance** - Improve application speed and responsiveness

</details>

---

**Q9.** What is the primary difference between the Azure Pricing Calculator and the TCO Calculator?

<details>
<summary>Answer</summary>

The Azure Pricing Calculator estimates the cost of specific Azure resources and services you plan to deploy in Azure. The TCO (Total Cost of Ownership) Calculator compares the costs of running workloads in your on-premises datacenter versus running them in Azure, helping organizations understand potential savings from cloud migration. The Pricing Calculator is for planning new Azure deployments, while the TCO Calculator is for migration planning and cost comparison.

</details>

---

### Scenario-Based

**Q10.** Contoso Ltd. is a financial services company that needs to deploy resources across multiple Azure subscriptions. They have the following requirements:

- All resources must be deployed in specific approved regions only
- Virtual machines must use only approved VM sizes
- All resources must have mandatory tags for department and project
- The configuration must be repeatable across new subscriptions

Which combination of Azure services should Contoso use to meet these requirements?

A) Azure Policy for region and VM size restrictions, resource tags for organization, and ARM templates for repeatability
B) Azure Blueprints to package policies, RBAC, and ARM templates together for repeatable deployment across subscriptions
C) Azure Advisor for recommendations, resource locks for protection, and Bicep templates for deployment
D) Azure Monitor for tracking compliance, Azure Policy for restrictions, and manual tag application

<details>
<summary>Answer</summary>

**Correct: B**

Azure Blueprints is the ideal solution because it allows organizations to package together Azure Policies (for region restrictions, VM size restrictions, and mandatory tags), RBAC role assignments, and ARM templates into a single blueprint definition. This blueprint can then be assigned to multiple subscriptions, ensuring consistent governance and deployment across the organization. 

Option A addresses individual requirements but doesn't provide the unified, repeatable deployment mechanism across subscriptions. Option C doesn't address policy enforcement. Option D relies on manual processes and doesn't meet the repeatability requirement.

</details>

---