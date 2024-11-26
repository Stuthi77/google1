from google.cloud import storage

# Initialize the client
client = storage.Client()

# List available buckets
buckets = list(client.list_buckets())
print("Buckets:", buckets)
