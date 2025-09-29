# Career Guidance Binary Decision Tree
# Author: [Your Name]
# Index: [Your Index Number]

class Node:
    def __init__(self, data, is_question=True):
        self.data = data          # Question text or Career Name
        self.is_question = is_question
        self.left = None          # Yes branch
        self.right = None         # No branch

# Sample initial tree
def initialize_tree():
    root = Node("Do you enjoy solving logical problems?")
    # Left subtree
    root.left = Node("Do you prefer working with data over building interfaces?")
    root.left.left = Node("Data Scientist", is_question=False)
    root.left.right = Node("Software Engineer", is_question=False)
    # Right subtree
    root.right = Node("Are you interested in how users interact with systems?")
    root.right.left = Node("UI/UX Designer", is_question=False)
    root.right.right = Node("Are you passionate about protecting systems from threats?")
    root.right.right.left = Node("Cybersecurity Analyst", is_question=False)
    root.right.right.right = Node("IT Support Specialist", is_question=False)
    return root

# Take career quiz
def take_quiz(node):
    if node is None:
        print("The decision tree is empty. Please initialize or build the tree first.")
        return
    while node.is_question:
        answer = input(f"{node.data} (yes/no): ").strip().lower()
        if answer == 'yes':
            node = node.left
        elif answer == 'no':
            node = node.right
        else:
            print("Please answer 'yes' or 'no'.")
    print(f"Recommended Career: {node.data}")

# Traverse tree and collect career paths (leaf nodes)
def view_careers(node):
    careers = []
    def traverse(n):
        if n is None:
            return
        if not n.is_question:
            careers.append(n.data)
        traverse(n.left)
        traverse(n.right)
    traverse(node)
    print("Career Recommendations:")
    for c in careers:
        print(f"- {c}")

# Search for a question or career
def search_tree(node, keyword):
    found = []
    def search(n, path):
        if n is None:
            return
        if keyword.lower() in n.data.lower():
            found.append((n.data, path))
        search(n.left, path + " -> Yes")
        search(n.right, path + " -> No")
    search(node, "")
    if found:
        for data, path in found:
            print(f"Found: {data} | Path: {path}")
    else:
        print(f"'{keyword}' not found in the tree.")

# Add a new question and careers
def add_question(node):
    target = input("Enter the exact leaf career to replace: ").strip()
    parent, is_left = find_parent(node, None, target)
    if parent is None:
        print("Career not found.")
        return
    new_question = input("Enter the new yes/no question: ").strip()
    career_yes = input("Enter career for 'Yes' answer: ").strip()
    career_no = input("Enter career for 'No' answer: ").strip()
    
    new_node = Node(new_question)
    new_node.left = Node(career_yes, is_question=False)
    new_node.right = Node(career_no, is_question=False)
    
    if is_left:
        parent.left = new_node
    else:
        parent.right = new_node
    print("Question and careers added successfully!")

# Helper to find parent of a leaf node
def find_parent(node, parent, target):
    if node is None:
        return None, None
    if not node.is_question and node.data == target:
        return parent, parent.left == node if parent else None
    l = find_parent(node.left, node, target)
    if l[0]:
        return l
    return find_parent(node.right, node, target)

# Remove a career
def remove_career(node):
    target = input("Enter the exact career to remove: ").strip()
    parent, is_left = find_parent(node, None, target)
    if parent is None:
        print("Career not found.")
        return
    # Remove the leaf
    if is_left:
        parent.left = None
    else:
        parent.right = None
    print("Career removed successfully!")

# Main menu
def main():
    tree = initialize_tree()
    while True:
        print("\n--- Career Guidance System ---")
        print("1. Take Career Quiz")
        print("2. View All Career Recommendations")
        print("3. Search for a Career/Question")
        print("4. Add Question and Careers")
        print("5. Remove a Career")
        print("6. Exit")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            take_quiz(tree)
        elif choice == '2':
            view_careers(tree)
        elif choice == '3':
            keyword = input("Enter keyword to search: ")
            search_tree(tree, keyword)
        elif choice == '4':
            add_question(tree)
        elif choice == '5':
            remove_career(tree)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
