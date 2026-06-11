# Cloud Service Models: IaaS vs PaaS vs SaaS
# This example demonstrates the differences between cloud service models
# using a simple pizza analogy that's easy to understand

# Define what you manage vs what the cloud provider manages
# for each service model

class CloudServiceModel:
    """Represents a cloud service model and its responsibilities"""
    
    def __init__(self, name, you_manage, provider_manages, example):
        self.name = name
        self.you_manage = you_manage
        self.provider_manages = provider_manages
        self.example = example
    
    def display_info(self):
        print(f"\n{'='*50}")
        print(f"Service Model: {self.name}")
        print(f"{'='*50}")
        print(f"\nExample: {self.example}")
        print(f"\nYOU manage:")
        for item in self.you_manage:
            print(f"  ✓ {item}")
        print(f"\nCLOUD PROVIDER manages:")
        for item in self.provider_manages:
            print(f"  ☁ {item}")


# Create the three main service models
iaas = CloudServiceModel(
    name="IaaS (Infrastructure as a Service)",
    you_manage=[
        "Applications",
        "Data",
        "Runtime",
        "Middleware",
        "Operating System"
    ],
    provider_manages=[
        "Virtualization",
        "Servers",
        "Storage",
        "Networking"
    ],
    example="Azure Virtual Machines - You rent the computer, install everything yourself"
)

paas = CloudServiceModel(
    name="PaaS (Platform as a Service)",
    you_manage=[
        "Applications",
        "Data"
    ],
    provider_manages=[
        "Runtime",
        "Middleware",
        "Operating System",
        "Virtualization",
        "Servers",
        "Storage",
        "Networking"
    ],
    example="Azure App Service - Just deploy your code, platform handles the rest"
)

saas = CloudServiceModel(
    name="SaaS (Software as a Service)",
    you_manage=[
        "Your data and configurations",
        "User access and permissions"
    ],
    provider_manages=[
        "Everything else!",
        "Applications",
        "Runtime",
        "Middleware",
        "Operating System",
        "Infrastructure"
    ],
    example="Microsoft 365 - Just sign in and use it"
)

# Display all service models
print("\n🌥️  CLOUD SERVICE MODELS EXPLAINED 🌥️")
print("Understanding what YOU manage vs what the PROVIDER manages\n")

for model in [iaas, paas, saas]:
    model.display_info()

# Simple comparison summary
print("\n" + "="*50)
print("QUICK COMPARISON (Pizza Analogy):")
print("="*50)
print("\nIaaS = Buying ingredients and making pizza at home")
print("PaaS = Using a pizza kit (dough provided, you add toppings)")
print("SaaS = Ordering pizza delivery (just eat it!)")