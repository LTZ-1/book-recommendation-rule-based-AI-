import json

def load_resources(file_path="resources.json"):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Resource file not found.")
        return {}

def get_input(prompt, options):
    print(f"\n{prompt}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
        except ValueError:
            pass
        print("Invalid input. Please enter a valid number.")

def recommend_resource(subject, level, resource_type, knowledge_base):
    return knowledge_base.get(subject, {}).get(level, {}).get(
        resource_type,
        "No matching resource found. Try different inputs or check with your library.",
    )

def main():
    print("=== Digital Library Book Finder ===")

    knowledge_base = load_resources()

    subjects = list(knowledge_base.keys())
    levels = ["Beginner", "Intermediate", "Advanced"]
    types = ["Ebook", "Video", "Article"]

    subject = get_input("Select subject:", subjects)
    level = get_input("Select difficulty level:", levels)
    resource_type = get_input("Select resource type:", types)

    resource = recommend_resource(subject, level, resource_type, knowledge_base)
    print(f"\nRecommended Resource:\n{resource}")

if __name__ == "__main__":
    main()