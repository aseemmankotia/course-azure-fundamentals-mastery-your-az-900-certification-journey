# Azure Resource Tags Management
# Tags help organize resources for billing, management, and governance
# This example shows how to work with tags using Azure SDK

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
import os

# For beginners: Tags are key-value pairs that help you organize resources
# Example: {"Environment": "Production", "Department": "Finance", "CostCenter": "CC-1234"}

def demonstrate_resource_tags():
    """
    Demonstrates how to add, update, and read tags on Azure resources.
    Tags are essential for:
    - Cost tracking and allocation
    - Resource organization
    - Automation and governance
    """
    
    # Get subscription ID from environment variable
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID", "your-subscription-id")
    
    # Authenticate using DefaultAzureCredential (works with Azure CLI, managed identity, etc.)
    credential = DefaultAzureCredential()
    
    # Create the Resource Management client
    resource_client = ResourceManagementClient(credential, subscription_id)
    
    # Define common tags for governance
    # Best Practice: Define a standard tagging strategy for your organization
    standard_tags = {
        "Environment": "Development",      # dev, staging, production
        "Department": "IT",                 # Which department owns this?
        "CostCenter": "CC-12345",          # For billing allocation
        "Project": "AZ900-Learning",       # Project name
        "Owner": "john.doe@company.com",   # Who to contact
        "CreatedDate": "2024-01-15",       # When was it created?
        "AutoShutdown": "true"             # For automation scripts
    }
    
    print("=== Azure Resource Tagging Example ===")
    print("\nStandard tags to apply:")
    for key, value in standard_tags.items():
        print(f"  {key}: {value}")
    
    # List all resource groups and their tags
    print("\n--- Current Resource Groups and Tags ---")
    for rg in resource_client.resource_groups.list():
        print(f"\nResource Group: {rg.name}")
        print(f"  Location: {rg.location}")
        if rg.tags:
            print("  Tags:")
            for key, value in rg.tags.items():
                print(f"    - {key}: {value}")
        else:
            print("  Tags: None (Consider adding tags for governance!)")
    
    # Example: Update tags on a resource group
    # Uncomment to actually update tags
    """
    rg_name = "my-resource-group"
    resource_client.resource_groups.update(
        rg_name,
        {"tags": standard_tags}
    )
    print(f"\nUpdated tags on {rg_name}")
    """
    
    return standard_tags

def calculate_tag_compliance(resource_client, required_tags):
    """
    Check how many resources are compliant with your tagging policy.
    This is similar to what Azure Policy does automatically.
    """
    total_resources = 0
    compliant_resources = 0
    non_compliant = []
    
    # Check each resource group
    for rg in resource_client.resource_groups.list():
        total_resources += 1
        
        # Check if all required tags are present
        if rg.tags:
            missing_tags = [tag for tag in required_tags if tag not in rg.tags]
            if not missing_tags:
                compliant_resources += 1
            else:
                non_compliant.append({
                    "name": rg.name,
                    "missing_tags": missing_tags
                })
        else:
            non_compliant.append({
                "name": rg.name,
                "missing_tags": required_tags
            })
    
    compliance_percentage = (compliant_resources / total_resources * 100) if total_resources > 0 else 0
    
    print(f"\n=== Tag Compliance Report ===")
    print(f"Required tags: {required_tags}")
    print(f"Total resources: {total_resources}")
    print(f"Compliant: {compliant_resources}")
    print(f"Compliance rate: {compliance_percentage:.1f}%")
    
    if non_compliant:
        print("\nNon-compliant resources:")
        for item in non_compliant:
            print(f"  - {item['name']}: Missing {item['missing_tags']}")
    
    return compliance_percentage

if __name__ == "__main__":
    print("Note: This example requires Azure SDK and valid credentials.")
    print("Install: pip install azure-identity azure-mgmt-resource\n")
    
    # Demonstrate the tagging concepts
    tags = demonstrate_resource_tags()
    
    # Show required tags for compliance checking
    required_tags = ["Environment", "CostCenter", "Owner"]
    print(f"\nRequired tags for compliance: {required_tags}")