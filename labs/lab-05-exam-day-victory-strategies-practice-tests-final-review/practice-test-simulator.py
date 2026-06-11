# AZ-900 Practice Test Simulator
# Simulates the exam experience with timed questions

import time
import random

# Sample AZ-900 style questions covering all domains
practice_questions = [
    {
        "domain": "Cloud Concepts (25-30%)",
        "question": "Which cloud model allows organizations to share responsibility for security with the cloud provider?",
        "options": [
            "A) On-premises",
            "B) Public cloud",
            "C) Private cloud hosted locally",
            "D) Air-gapped data center"
        ],
        "correct": "B",
        "explanation": "Public cloud uses a shared responsibility model where Microsoft manages physical security and infrastructure, while you manage your data and access."
    },
    {
        "domain": "Azure Architecture (35-40%)",
        "question": "A company needs to ensure their application remains available even if an entire Azure datacenter fails. What should they use?",
        "options": [
            "A) Availability Sets",
            "B) Availability Zones",
            "C) A single VM with premium storage",
            "D) Azure Backup"
        ],
        "correct": "B",
        "explanation": "Availability Zones are physically separate datacenters within an Azure region, providing protection against datacenter-level failures."
    },
    {
        "domain": "Azure Services (15-20%)",
        "question": "Which Azure service would you use to run code in response to an HTTP request without managing servers?",
        "options": [
            "A) Azure Virtual Machines",
            "B) Azure Functions",
            "C) Azure Kubernetes Service",
            "D) Azure Dedicated Host"
        ],
        "correct": "B",
        "explanation": "Azure Functions is a serverless compute service that lets you run event-triggered code without managing infrastructure."
    },
    {
        "domain": "Security & Compliance (25-30%)",
        "question": "Which Azure service provides a centralized view of security recommendations across all your Azure resources?",
        "options": [
            "A) Azure Monitor",
            "B) Azure Advisor",
            "C) Microsoft Defender for Cloud",
            "D) Azure Activity Log"
        ],
        "correct": "C",
        "explanation": "Microsoft Defender for Cloud (formerly Azure Security Center) provides unified security management and threat protection."
    },
    {
        "domain": "Pricing & Support (20-25%)",
        "question": "Which Azure support plan is the MINIMUM required to get 24/7 technical support by phone?",
        "options": [
            "A) Basic",
            "B) Developer",
            "C) Standard",
            "D) Professional Direct"
        ],
        "correct": "C",
        "explanation": "Standard support plan is the minimum tier that includes 24/7 phone and email support for technical issues."
    }
]

def run_practice_test(questions, time_per_question=60):
    """Run a timed practice test simulation"""
    
    print("=" * 60)
    print("       AZ-900 PRACTICE TEST SIMULATOR")
    print("=" * 60)
    print(f"\nTotal Questions: {len(questions)}")
    print(f"Time per question: {time_per_question} seconds")
    print(f"Total time: {len(questions) * time_per_question // 60} minutes")
    print("\nTip: In the real exam, you have 45-60 minutes for 40-60 questions.")
    print("That's roughly 1 minute per question!")
    print("\n" + "-" * 60)
    input("Press Enter to start the test...")
    
    score = 0
    results = []
    total_time = 0
    
    # Shuffle questions for variety
    shuffled_questions = questions.copy()
    random.shuffle(shuffled_questions)
    
    for i, q in enumerate(shuffled_questions, 1):
        print(f"\n{'='*60}")
        print(f"Question {i} of {len(questions)} | Domain: {q['domain']}")
        print("=" * 60)
        print(f"\n{q['question']}\n")
        
        for option in q['options']:
            print(f"  {option}")
        
        # Start timer for this question
        start_time = time.time()
        
        # Get user answer
        print(f"\n⏱️  You have {time_per_question} seconds...")
        answer = input("\nYour answer (A/B/C/D): ").strip().upper()
        
        # Calculate time taken
        time_taken = time.time() - start_time
        total_time += time_taken
        
        # Check answer
        is_correct = answer == q['correct']
        if is_correct:
            score += 1
            print("\n✅ CORRECT!")
        else:
            print(f"\n❌ Incorrect. The correct answer is: {q['correct']}")
        
        print(f"\n📖 Explanation: {q['explanation']}")
        print(f"⏱️  Time taken: {time_taken:.1f} seconds")
        
        if time_taken > time_per_question:
            print("⚠️  Warning: You exceeded the recommended time!")
        
        results.append({
            "question": i,
            "correct": is_correct,
            "time": time_taken,
            "domain": q['domain']
        })
        
        if i < len(questions):
            input("\nPress Enter for next question...")
    
    # Display final results
    display_results(score, len(questions), total_time, results)

def display_results(score, total, total_time, results):
    """Display detailed test results"""
    
    percentage = (score / total) * 100
    passing_score = 70  # AZ-900 requires ~700/1000 (roughly 70%)
    
    print("\n" + "=" * 60)
    print("                 TEST RESULTS")
    print("=" * 60)
    
    print(f"\n📊 Score: {score}/{total} ({percentage:.1f}%)")
    print(f"⏱️  Total time: {total_time:.1f} seconds ({total_time/60:.1f} minutes)")
    print(f"📈 Average time per question: {total_time/total:.1f} seconds")
    
    if percentage >= passing_score:
        print("\n🎉 PASSED! Great job!")
    else:
        print(f"\n📚 Keep studying! You need {passing_score}% to pass.")
    
    # Domain breakdown
    print("\n" + "-" * 40)
    print("Performance by Domain:")
    print("-" * 40)
    
    domains = {}
    for r in results:
        domain = r['domain']
        if domain not in domains:
            domains[domain] = {'correct': 0, 'total': 0}
        domains[domain]['total'] += 1
        if r['correct']:
            domains[domain]['correct'] += 1
    
    for domain, stats in domains.items():
        pct = (stats['correct'] / stats['total']) * 100
        status = "✅" if pct >= 70 else "⚠️"
        print(f"{status} {domain}: {stats['correct']}/{stats['total']} ({pct:.0f}%)")

# Run the practice test
if __name__ == "__main__":
    run_practice_test(practice_questions, time_per_question=90)