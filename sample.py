import google.generativeai as genai

# Configure the API key
genai.configure(api_key="YOUR_GOOGLE_API_KEY")

# Example usage
response = genai.text(prompt="Write a short story about AI.")
print(response)
