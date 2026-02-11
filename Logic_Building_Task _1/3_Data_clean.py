names = [" Alice ", "bob", " CHARLIE "]

cleaned_names = []

for name in names:
    name = name.strip()      # Remove extra spaces
    name = name.lower()      # Convert to lowercase
    cleaned_names.append(name)

print("Cleaned Names:", cleaned_names)
