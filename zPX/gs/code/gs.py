import ollama


response = ollama.chat(model='llama3.2', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])

image_path = '/Users/peter/CODE/oss/ollama/img/ivlogo.png'  # Replace with your image path

# Use Ollama to analyze the image with Llama 3.2-Vision
response = ollama.chat(
    model="llama3.2-vision",
    messages=[{
      "role": "user",
      "content": "Describe this image?",
      "images": [image_path]
    }],
)

# Extract the model's response about the image
cleaned_text = response['message']['content'].strip()
print(f"Model Response: {cleaned_text}")