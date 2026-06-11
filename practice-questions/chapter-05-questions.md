## Chapter 5: Exam Day Victory: Strategies, Practice Tests & Final Review — Practice Questions

### Multiple Choice

**Q1.** You have 45 minutes remaining on your AZ-900 exam and 30 questions left to answer. What is the BEST time management approach?

A) Spend extra time on the first 10 questions to ensure they are correct
B) Allocate approximately 1.5 minutes per question and flag difficult ones for review
C) Skip all scenario-based questions and answer the short ones first
D) Guess on all remaining questions to finish quickly

<details>
<summary>Answer</summary>

**Correct: B**

Allocating roughly 1.5 minutes per question allows you to pace yourself evenly. Flagging difficult questions lets you return to them after answering easier ones, maximizing your score. Option A risks running out of time for later questions. Option C ignores potentially easy points in scenarios. Option D wastes the opportunity to demonstrate your knowledge.

</details>

---

**Q2.** During the AZ-900 exam, you encounter a question asking about the "best" solution. Two answers seem technically correct. What elimination technique should you apply?

A) Always choose the longest answer
B) Select the first answer that seems correct
C) Consider which option aligns with Microsoft's recommended practices and the specific scenario context
D) Choose the cheapest option mentioned

<details>
<summary>Answer</summary>

**Correct: C**

When multiple answers seem correct, Microsoft exams typically want the answer that aligns with their recommended best practices and fits the specific scenario described. Option A is a myth with no basis. Option B may cause you to miss the better answer. Option D is only relevant if cost optimization is specifically mentioned in the question.

</details>

---

**Q3.** What is the passing score for the AZ-900 certification exam?

A) 650 out of 1000
B) 700 out of 1000
C) 750 out of 1000
D) 800 out of 1000

<details>
<summary>Answer</summary>

**Correct: B**

The AZ-900 exam requires a minimum score of 700 out of 1000 to pass. This is the standard passing score for most Microsoft Fundamentals certifications. Options A, C, and D represent incorrect passing thresholds.

</details>

---

**Q4.** You are reviewing for the AZ-900 exam and have limited study time. Which domain should receive the MOST attention based on exam weight?

A) Describe cloud concepts (25-30%)
B) Describe Azure architecture and services (35-40%)
C) Describe Azure management and governance (30-35%)
D) All domains are weighted equally

<details>
<summary>Answer</summary>

**Correct: B**

"Describe Azure architecture and services" carries the highest weight at 35-40% of the exam. While all domains are important, prioritizing the highest-weighted domain maximizes your potential score when study time is limited. Options A and C have lower weights, and Option D is factually incorrect.

</details>

---

**Q5.** A question on your exam states: "Your company needs a solution that provides 99.99% availability." You notice one answer mentions a single virtual machine and another mentions an Availability Zone deployment. What common exam trap should you avoid?

A) Choosing the answer with the most technical jargon
B) Selecting the simpler solution without considering the specific SLA requirement
C) Picking the answer that mentions the newest Azure feature
D) Choosing the answer with the lowest cost

<details>
<summary>Answer</summary>

**Correct: B**

A common exam trap is ignoring specific requirements stated in the question. A single VM cannot provide 99.99% SLA—only Availability Zone deployments can achieve this level of availability in Azure. Always match your answer to the exact requirements given. Options A, C, and D represent other incorrect decision-making approaches that ignore the stated requirement.

</details>

---

### True / False

**Q6.** On the AZ-900 exam, you can return to previous questions and change your answers before submitting the exam. — **True / False**

**True**

*The AZ-900 exam allows you to flag questions and navigate back to review and change answers before final submission. This is why flagging uncertain questions is an effective strategy—you can revisit them after completing easier questions with your remaining time.*

---

**Q7.** Scenario-based questions on the AZ-900 exam always require you to select multiple correct answers. — **True / False**

**False**

*Scenario-based questions can have various formats including single-answer multiple choice, multiple-answer selections, or drag-and-drop matching. The question will clearly indicate if you need to select more than one answer (for example, "Select TWO" or "Select all that apply"). Never assume you need multiple answers unless explicitly stated.*

---

### Short Answer

**Q8.** List three things you should do the night before and morning of your AZ-900 exam to prepare for exam day logistics.

<details>
<summary>Answer</summary>

Acceptable answers include any three of the following:
- Get adequate sleep (7-8 hours recommended)
- Prepare valid identification documents
- Know your testing center location or test your home setup for online proctoring
- Eat a balanced meal before the exam
- Arrive 15-30 minutes early for in-person testing
- Test your computer, webcam, and internet connection for online exams
- Review the exam policies and what items are allowed/prohibited
- Prepare a quiet, clutter-free space for online testing

</details>

---

**Q9.** What should you do immediately after passing the AZ-900 exam to continue your Azure certification journey?

<details>
<summary>Answer</summary>

After passing AZ-900, you should:
- Download and share your digital badge from Microsoft Certification Dashboard
- Identify your career path (Administrator, Developer, Architect, Data, Security, or AI)
- Choose your next role-based certification (such as AZ-104 for Administrator or AZ-204 for Developer)
- Begin studying for the next certification while foundational knowledge is fresh
- Update your resume and LinkedIn profile with the new certification

</details>

---

### Scenario-Based

**Q10.** You are taking the AZ-900 exam and encounter the following question:

*"Contoso Ltd. is a small retail company considering moving their on-premises servers to Azure. They have unpredictable traffic patterns with very high demand during holiday seasons and minimal traffic during other months. The IT manager wants to minimize costs while ensuring they can handle peak demand. Which cloud benefit BEST addresses their needs?"*

The options are:
A) High availability
B) Elasticity
C) Geo-distribution
D) Disaster recovery

Explain which answer is correct and describe the process you would use to eliminate incorrect options.

<details>
<summary>Answer</summary>

**Correct: B) Elasticity**

**Elimination process:**

1. **Identify the key requirements in the scenario:** unpredictable traffic, high demand during holidays, minimal traffic other times, minimize costs, handle peak demand.

2. **Eliminate options that don't match the requirements:**
   - **A) High availability** - This addresses uptime and fault tolerance, not scaling for variable demand. Eliminate.
   - **C) Geo-distribution** - This addresses serving users in different geographic locations, not handling traffic fluctuations. Eliminate.
   - **D) Disaster recovery** - This addresses business continuity after failures, not cost optimization for variable workloads. Eliminate.

3. **Confirm the remaining answer:** **B) Elasticity** directly addresses the ability to automatically scale resources up during peak demand (holidays) and scale down during low-traffic periods, which minimizes costs by only paying for what you use.

**Test-taking tip:** Circle or mentally note specific words like "unpredictable," "minimize costs," and "peak demand"—these are clues pointing to elasticity as the cloud benefit that allows dynamic scaling based on demand.

</details>