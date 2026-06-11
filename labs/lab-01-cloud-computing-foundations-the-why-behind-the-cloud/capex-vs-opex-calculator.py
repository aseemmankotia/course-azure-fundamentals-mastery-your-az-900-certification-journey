# CapEx vs OpEx: Understanding Cloud Financial Models
# This example compares traditional (CapEx) vs cloud (OpEx) costs
# to show why consumption-based pricing is beneficial

class TraditionalDataCenter:
    """Represents CapEx (Capital Expenditure) model - buy upfront"""
    
    def __init__(self, server_cost, num_servers, maintenance_yearly, lifespan_years):
        self.server_cost = server_cost
        self.num_servers = num_servers
        self.maintenance_yearly = maintenance_yearly
        self.lifespan_years = lifespan_years
    
    def calculate_total_cost(self):
        # CapEx: Big upfront cost + ongoing maintenance
        upfront_cost = self.server_cost * self.num_servers
        total_maintenance = self.maintenance_yearly * self.lifespan_years
        return upfront_cost + total_maintenance
    
    def get_year_one_cost(self):
        # Year 1: Full hardware purchase + maintenance
        return (self.server_cost * self.num_servers) + self.maintenance_yearly


class CloudInfrastructure:
    """Represents OpEx (Operational Expenditure) model - pay as you go"""
    
    def __init__(self, monthly_cost_per_vm, num_vms, years):
        self.monthly_cost = monthly_cost_per_vm
        self.num_vms = num_vms
        self.years = years
    
    def calculate_total_cost(self):
        # OpEx: Pay monthly, no upfront costs
        monthly_total = self.monthly_cost * self.num_vms
        return monthly_total * 12 * self.years
    
    def get_year_one_cost(self):
        # Year 1: Just monthly payments
        return self.monthly_cost * self.num_vms * 12
    
    def scale_up(self, additional_vms):
        """Cloud advantage: Easy to scale!"""
        self.num_vms += additional_vms
        print(f"✓ Scaled up! Now running {self.num_vms} VMs")
        print(f"  New monthly cost: ${self.monthly_cost * self.num_vms:,.2f}")


# Compare the two models
print("💰 CapEx vs OpEx: Financial Comparison 💰")
print("="*55)

# Traditional: Buy 10 servers at $5000 each
traditional = TraditionalDataCenter(
    server_cost=5000,
    num_servers=10,
    maintenance_yearly=10000,
    lifespan_years=5
)

# Cloud: Rent 10 VMs at $150/month each
cloud = CloudInfrastructure(
    monthly_cost_per_vm=150,
    num_vms=10,
    years=5
)

print("\n📊 SCENARIO: Running 10 servers for 5 years")
print("-"*55)

print("\n🏢 TRADITIONAL (CapEx - Capital Expenditure):")
print(f"   Year 1 cost: ${traditional.get_year_one_cost():,.2f}")
print(f"   5-year total: ${traditional.calculate_total_cost():,.2f}")
print("   ⚠️  Must pay upfront, hardware depreciates")
print("   ⚠️  Hard to scale - need to buy more servers")

print("\n☁️  CLOUD (OpEx - Operational Expenditure):")
print(f"   Year 1 cost: ${cloud.get_year_one_cost():,.2f}")
print(f"   5-year total: ${cloud.calculate_total_cost():,.2f}")
print("   ✓ No upfront cost - pay monthly")
print("   ✓ Easy to scale up or down")

# Demonstrate cloud scaling
print("\n🚀 CLOUD SCALING DEMONSTRATION:")
print("-"*55)
print("Business grows - need 5 more servers!")
print("\nTraditional: Buy 5 more servers = $25,000 more CapEx 😰")
print("\nCloud:")
cloud.scale_up(5)

print("\n" + "="*55)
print("KEY TAKEAWAY:")
print("CapEx = Own it (big upfront cost, you manage everything)")
print("OpEx  = Rent it (pay as you go, provider manages hardware)")