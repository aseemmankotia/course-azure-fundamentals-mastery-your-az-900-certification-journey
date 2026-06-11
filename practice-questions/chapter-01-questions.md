## Chapter 1: Cloud Computing Foundations: The 'Why' Behind the Cloud — Practice Questions

### Multiple Choice

**Q1.** Your company wants to reduce the time needed to deploy new applications from weeks to hours. Which cloud benefit BEST describes this advantage?

A) High Availability
B) Fault Tolerance
C) Agility
D) Elasticity

<details>
<summary>Answer</summary>

**Correct: C**

Agility refers to the ability to quickly deploy and configure cloud-based resources as business requirements change. High Availability ensures systems remain operational. Fault Tolerance allows systems to continue operating despite failures. Elasticity refers to automatically scaling resources based on demand.

</details>

---

**Q2.** A retail company experiences a massive increase in website traffic during holiday sales but has minimal traffic during the rest of the year. Which cloud benefit allows them to automatically adjust computing resources based on this fluctuating demand?

A) Disaster Recovery
B) Elasticity
C) High Availability
D) Agility

<details>
<summary>Answer</summary>

**Correct: B**

Elasticity is the ability to automatically increase or decrease computing resources based on actual demand. Disaster Recovery involves recovering from outages. High Availability ensures continuous operation. Agility relates to rapid deployment of resources.

</details>

---

**Q3.** Your organization uses Microsoft 365 for email and collaboration. Which cloud service model does this represent?

A) Infrastructure as a Service (IaaS)
B) Platform as a Service (PaaS)
C) Software as a Service (SaaS)
D) On-premises

<details>
<summary>Answer</summary>

**Correct: C**

Microsoft 365 is a complete software solution delivered over the internet, which defines SaaS. With SaaS, users access ready-to-use applications without managing infrastructure or platforms. IaaS provides virtual machines and infrastructure. PaaS provides a platform for developing applications. On-premises means hosting everything in your own data center.

</details>

---

**Q4.** In the Shared Responsibility Model, when using Platform as a Service (PaaS), who is responsible for managing the operating system?

A) The customer
B) The cloud provider
C) Both the customer and cloud provider equally
D) Neither party

<details>
<summary>Answer</summary>

**Correct: B**

In PaaS, the cloud provider manages the operating system, along with the underlying infrastructure. The customer is responsible for their applications and data. In IaaS, the customer would manage the operating system. The shared responsibility model clearly divides duties between provider and customer.

</details>

---

**Q5.** A startup company has limited upfront capital but needs computing resources immediately. Which financial model should they consider when moving to the cloud?

A) Capital Expenditure (CapEx)
B) Operational Expenditure (OpEx)
C) Fixed cost model
D) Depreciation model

<details>
<summary>Answer</summary>

**Correct: B**

OpEx (Operational Expenditure) uses a pay-as-you-go model with no upfront costs, making it ideal for startups with limited capital. CapEx requires significant upfront investment for physical infrastructure. Fixed cost models don't align with cloud's flexible pricing. Depreciation relates to CapEx assets losing value over time.

</details>

---

### True / False

**Q6.** In a public cloud deployment model, the cloud infrastructure is shared among multiple organizations but each organization's data remains isolated and secure. — **True / False**

*True. Public cloud resources are shared across multiple tenants (organizations), but cloud providers implement strong isolation and security measures to ensure each customer's data and workloads remain separate and protected from other tenants.*

---

**Q7.** When using Infrastructure as a Service (IaaS), the customer is responsible for patching and maintaining the physical servers in the data center. — **True / False**

*False. In IaaS, the cloud provider maintains all physical infrastructure including servers, networking hardware, and data center facilities. The customer is responsible for managing the operating system, middleware, applications, and data running on the virtual infrastructure.*

---

### Short Answer

**Q8.** Explain the difference between High Availability and Fault Tolerance in cloud computing.

<details>
<summary>Answer</summary>

High Availability focuses on keeping systems operational and accessible for the maximum amount of time, often expressed as a percentage (like 99.9% uptime). It typically involves redundant systems that can take over if one fails.

Fault Tolerance is the ability of a system to continue operating without interruption even when one or more components fail. It provides zero downtime by having duplicate components running simultaneously, so if one fails, another immediately handles the workload with no service disruption.

</details>

---

**Q9.** What are the three main cloud deployment models, and briefly describe a scenario where each would be most appropriate?

<details>
<summary>Answer</summary>

**Public Cloud:** Resources owned and operated by a third-party provider, delivered over the internet. Best for: A startup wanting to launch quickly without infrastructure investment.

**Private Cloud:** Cloud resources used exclusively by a single organization, either on-premises or hosted by a provider. Best for: A government agency with strict data sovereignty and compliance requirements.

**Hybrid Cloud:** Combines public and private clouds, allowing data and applications to be shared between them. Best for: A hospital keeping sensitive patient records in a private cloud while using public cloud for its public website.

</details>

---

### Scenario-Based

**Q10.** Contoso Ltd. is a manufacturing company that currently runs all IT systems in their own data center. They are considering moving to the cloud and have the following requirements:

- They want to maintain full control over their virtual machines and install custom software
- They need to reduce capital expenditure on hardware
- They want the cloud provider to handle physical server maintenance
- Their IT team should manage operating system updates and security patches

Which cloud service model should Contoso implement, and explain why this model meets their specific requirements?

<details>
<summary>Answer</summary>

**Recommended Model: Infrastructure as a Service (IaaS)**

IaaS meets all of Contoso's requirements:

1. **Full control over VMs and custom software:** IaaS provides virtual machines where customers have complete control to install and configure any software they need.

2. **Reduced capital expenditure:** IaaS uses the OpEx model—Contoso pays only for what they use without purchasing physical hardware, eliminating large upfront CapEx investments.

3. **Provider handles physical maintenance:** The cloud provider is responsible for the physical infrastructure, including servers, storage, networking, and data center facilities.

4. **Customer manages OS updates:** In the IaaS shared responsibility model, customers are responsible for managing and patching operating systems, which aligns with what Contoso's IT team wants to control.

PaaS would not be suitable because the cloud provider manages the OS. SaaS would not work because it provides finished applications without infrastructure control.

</details>

---