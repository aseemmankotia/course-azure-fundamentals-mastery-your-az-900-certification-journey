# Azure Blob Storage Tiers Demo
# This example shows how to upload blobs and manage storage tiers
# (Hot, Cool, and Archive) for cost optimization

from azure.storage.blob import BlobServiceClient, BlobClient
from azure.identity import DefaultAzureCredential
import os

# Connection string (in production, use environment variables or Azure Key Vault)
# For learning: You can get this from Azure Portal > Storage Account > Access Keys
connection_string = os.environ.get("AZURE_STORAGE_CONNECTION_STRING", "your-connection-string-here")

def demonstrate_blob_storage():
    """
    Demonstrates basic blob operations and storage tiers.
    
    Storage Tiers Explained:
    - HOT: Frequently accessed data (highest storage cost, lowest access cost)
    - COOL: Infrequently accessed, stored for at least 30 days
    - ARCHIVE: Rarely accessed, stored for at least 180 days (lowest storage cost)
    """
    
    # Create a BlobServiceClient to interact with the storage account
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    # Create a container (like a folder for your blobs)
    container_name = "my-first-container"
    
    try:
        # Create the container if it doesn't exist
        container_client = blob_service_client.create_container(container_name)
        print(f"✅ Container '{container_name}' created successfully!")
    except Exception as e:
        print(f"ℹ️ Container may already exist: {e}")
        container_client = blob_service_client.get_container_client(container_name)
    
    # Upload a blob with HOT tier (default for frequently accessed data)
    blob_name_hot = "reports/daily-report.txt"
    blob_client_hot = blob_service_client.get_blob_client(
        container=container_name, 
        blob=blob_name_hot
    )
    
    # Sample data to upload
    report_data = "Daily Sales Report - Accessed multiple times per day"
    
    # Upload with HOT tier (best for frequently accessed data)
    blob_client_hot.upload_blob(
        report_data, 
        overwrite=True,
        standard_blob_tier="Hot"  # Explicitly set to Hot tier
    )
    print(f"📄 Uploaded '{blob_name_hot}' with HOT tier")
    
    # Upload a blob with COOL tier (for infrequent access)
    blob_name_cool = "archives/monthly-backup.txt"
    blob_client_cool = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name_cool
    )
    
    backup_data = "Monthly backup data - Accessed occasionally for compliance"
    blob_client_cool.upload_blob(
        backup_data,
        overwrite=True,
        standard_blob_tier="Cool"  # Save money on storage, pay more for access
    )
    print(f"📦 Uploaded '{blob_name_cool}' with COOL tier")
    
    # List all blobs and their tiers
    print("\n📋 All blobs in container:")
    print("-" * 50)
    
    for blob in container_client.list_blobs():
        print(f"  Name: {blob.name}")
        print(f"  Tier: {blob.blob_tier}")
        print(f"  Size: {blob.size} bytes")
        print("-" * 50)
    
    # Change tier of an existing blob (e.g., move to Archive for long-term storage)
    print("\n🔄 Changing blob tier from Cool to Archive...")
    blob_client_cool.set_standard_blob_tier("Archive")
    print("✅ Tier changed! (Note: Rehydrating from Archive takes hours)")

if __name__ == "__main__":
    print("="*60)
    print("Azure Blob Storage Tiers Demo")
    print("="*60)
    demonstrate_blob_storage()