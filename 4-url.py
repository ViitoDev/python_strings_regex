url = str(input("Enter your url:\n"))

if url.startswith("https://") and url.endswith(".com"):
    print(f"The {url} is valid!")
else:
    print("Invalid url!")