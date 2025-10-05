# ==============================================
# Career Guidance Binary Decision Tree
# Author: [Your Name]
# Index: [Your Index Number]
# Description:
#   This console-based program uses a binary decision tree
#   to guide users toward suitable IT-related career paths
#   through a series of yes/no questions.
# ==============================================

class Node:
    """Represents a single node in the decision tree (question or career)."""
    def __init__(self, data, is_question=True):
        self.data = data
        self.is_question = is_question
        self.left = None   # Yes branch
        self.right = None  # No branch

# -----------------------------
# Initialize base decision tree
# -----------------------------
def initialize_tree():
    root = Node("Do you enjoy solving logical problems?")
    root.left = Node("Do you prefer working with data over building interfaces?")
    root.left.left = Node("Data Scientist", is_question=False)
    root.left.right = Node("Software Engineer", is_question=False)
    root.right = Node("Are you interested in how users interact with systems?")
    root.right.left = Node("UI/UX Designer", is_question=False)
    root.right.right = Node("Are you passionate about protecting systems from threats?")
    root.right.right.left = Node("Cybersecurity Analyst", is_question=False)
    root.right.right.right = Node("IT Support Specialist", is_question=False)
    return root

# --------------------------------
# Function 1: Take the career quiz
# --------------------------------
def take_quiz(node):
    """Interactively traverse the tree based on yes/no answers."""
    if node is None:
        print("⚠ The decision tree is empty.")
        return
    while node.is_question:
        answer = input(f"{node.data} (yes/no): ").strip().lower()
        if answer == 'yes':
            node = node.left
        elif answer == 'no':
            node = node.right
        else:
            print("Please answer 'yes' or 'no'.")
    print(f"\n🎯 Recommended Career: {node.data}\n")

# --------------------------------
# Function 2: View all careers
# --------------------------------
def view_careers(node):
    """Display all possible career outcomes (leaf nodes)."""
    careers = []
    def traverse(n):
        if n is None:
            return
        if not n.is_question:
            careers.append(n.data)
        traverse(n.left)
        traverse(n.right)
    traverse(node)
    print("\nAvailable Career Recommendations:")
    for c in careers:
        print(f" - {c}")

# --------------------------------
# Function 3: Search by keyword
# --------------------------------
def search_tree(node, keyword):
    """Search the tree for a question or career containing the keyword."""
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

# --------------------------------
# Helper: Find parent of target
# --------------------------------
def find_parent(node, parent, target):
    if node is None:
        return None, None
    if not node.is_question and node.data.lower() == target.lower():
        return parent, parent.left == node if parent else None
    l = find_parent(node.left, node, target)
    if l[0]:
        return l
    return find_parent(node.right, node, target)

# --------------------------------
# Function 4: Add new question
# --------------------------------
def add_question(node):
    """Replace a career leaf with a new question and two new careers."""
    target = input("Enter the exact career to replace: ").strip()
    parent, is_left = find_parent(node, None, target)
    if parent is None:
        print("Career not found. Please check the name and try again.")
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
    print("✅ Question and new careers added successfully!")

# --------------------------------
# Function 5: Remove a career
# --------------------------------
def remove_career(node):
    """Remove a career (leaf node) from the tree."""
    target = input("Enter the exact career to remove: ").strip()
    parent, is_left = find_parent(node, None, target)
    if parent is None:
        print("Career not found.")
        return
    if is_left:
        parent.left = None
    else:
        parent.right = None
    print("🗑️ Career removed successfully!")

# --------------------------------
# Main Menu Loop
# --------------------------------
def main():
    tree = initialize_tree()
    while True:
        print("\n" + "="*45)
        print("   🎓 Career Guidance System Menu")
        print("="*45)
        print("1. Take Career Quiz")
        print("2. View All Career Recommendations")
        print("3. Search for a Career/Question")
        print("4. Add Question and Careers")
        print("5. Remove a Career")
        print("6. Exit")
        choice = input("Enter choice (1-6): ").strip()
        if choice == '1':
            take_quiz(tree)
        elif choice == '2':
            view_careers(tree)
        elif choice == '3':
            keyword = input("Enter keyword to search: ").strip()
            search_tree(tree, keyword)
        elif choice == '4':
            add_question(tree)
        elif choice == '5':
            remove_career(tree)
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-6.")

if __name__ == "__main__":
    main()
