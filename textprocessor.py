# Step 1: Read the contents of input.txt
with open("input.txt", "r") as infile:
    content = infile.read()

# Step 2: Count the number of words
word_count = len(content.split())

# Step 3: Convert text to uppercase
processed_text = content.upper()

# Step 4: Write processed text and word count to output.txt
with open("output.txt", "w") as outfile:
    outfile.write("=== PROCESSED TEXT ===\n")
    outfile.write(processed_text + "\n\n")
    outfile.write(f"WORD COUNT: {word_count}\n")

# Step 5: Print success message
print("File 'output.txt' has been created successfully with processed text and word count.")