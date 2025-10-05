# ------------------------------------------------------------
# Social Network Graph Analysis Console Application
# Author: [Your Name]
# Index: [Your Index Number]
# Description:
#   Models a social network as an undirected weighted graph.
#   Supports adding/removing users and friendships, viewing
#   network structure, finding shortest paths (Dijkstra),
#   finding mutual friends, and suggesting new friends.
# ------------------------------------------------------------

import heapq

class SocialNetwork:
    def __init__(self):
        # Graph: user -> list of (friend, interaction_weight)
        self.graph = {}

    # Add a new user node
    def add_user(self, user):
        if user in self.graph:
            print("User already exists.")
        else:
            self.graph[user] = []
            print(f"User '{user}' added.")

    # Add a bidirectional edge (friendship)
    def add_friendship(self, user1, user2, weight):
        if not self.graph:
            print("Network is empty. Add users first.")
            return
        if user1 not in self.graph or user2 not in self.graph:
            print("Both users must exist in the network.")
            return
        if user1 == user2:
            print("A user cannot be friends with themselves.")
            return
        # Prevent duplicate friendship
        if any(friend == user2 for friend, _ in self.graph[user1]):
            print("Friendship already exists.")
            return
        self.graph[user1].append((user2, weight))
        self.graph[user2].append((user1, weight))
        print(f"Friendship added between {user1} and {user2} with weight {weight}.")

    # View all users and their friendships
    def view_network(self):
        if not self.graph:
            print("Network is empty.")
            return
        print("\n--- Social Network Structure ---")
        print(f"Total users: {len(self.graph)}")
        total_edges = sum(len(f) for f in self.graph.values()) // 2
        print(f"Total connections: {total_edges}")
        for user, friends in self.graph.items():
            friend_list = ', '.join(f"{f} (w={w})" for f, w in friends)
            print(f"{user}: {friend_list or 'No friends'}")

    # Find the shortest path (strongest connection route)
    def shortest_path(self, start, end):
        if start not in self.graph or end not in self.graph:
            print("Both users must exist.")
            return
        heap = [(0, start, [start])]
        visited = set()
        while heap:
            cost, node, path = heapq.heappop(heap)
            if node == end:
                print(f"Shortest path: {' -> '.join(path)}")
                print(f"Total interaction cost: {cost}")
                return
            if node in visited:
                continue
            visited.add(node)
            for neighbor, weight in self.graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + weight, neighbor, path + [neighbor]))
        print("No connection found.")

    # Find mutual friends between two users
    def mutual_friends(self, user1, user2):
        if user1 not in self.graph or user2 not in self.graph:
            print("Both users must exist.")
            return
        friends1 = {f for f, _ in self.graph[user1]}
        friends2 = {f for f, _ in self.graph[user2]}
        mutual = friends1 & friends2
        print(f"Mutual friends between {user1} and {user2}: {', '.join(mutual) if mutual else 'None'}")

    # Suggest new friends based on mutual connections
    def suggested_friends(self, user):
        if user not in self.graph:
            print("User not found.")
            return
        direct = {f for f, _ in self.graph[user]}
        suggestions = {}
        for friend in direct:
            for fof, _ in self.graph[friend]:
                if fof != user and fof not in direct:
                    suggestions[fof] = suggestions.get(fof, 0) + 1
        result = [u for u, c in suggestions.items() if c >= 2]
        print(f"Suggested friends for {user}: {', '.join(result) if result else 'None'}")

    # Remove user and their connections
    def remove_user(self, user):
        if user not in self.graph:
            print("User not found.")
            return
        for friend, _ in list(self.graph[user]):
            self.graph[friend] = [(f, w) for f, w in self.graph[friend] if f != user]
        del self.graph[user]
        print(f"User '{user}' and all related friendships removed.")

    # Remove a friendship link
    def remove_friendship(self, user1, user2):
        if user1 not in self.graph or user2 not in self.graph:
            print("Both users must exist.")
            return
        self.graph[user1] = [(f, w) for f, w in self.graph[user1] if f != user2]
        self.graph[user2] = [(f, w) for f, w in self.graph[user2] if f != user1]
        print(f"Friendship between {user1} and {user2} removed.")

# ------------------- MENU-DRIVEN INTERFACE -------------------
def main():
    sn = SocialNetwork()
    while True:
        print("\n--- Social Network Console ---")
        print("1. Add User")
        print("2. Add Friendship")
        print("3. View Network")
        print("4. Shortest Connection Path")
        print("5. Mutual Friends")
        print("6. Suggested Friends")
        print("7. Remove User")
        print("8. Remove Friendship")
        print("9. Exit")

        choice = input("Enter choice: ").strip()
        if choice == '1':
            sn.add_user(input("Enter user name: ").strip())
        elif choice == '2':
            u1 = input("First user: ").strip()
            u2 = input("Second user: ").strip()
            try:
                weight = int(input("Interaction strength (1-5): ").strip())
                sn.add_friendship(u1, u2, weight)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            sn.view_network()
        elif choice == '4':
            sn.shortest_path(input("Start user: ").strip(), input("End user: ").strip())
        elif choice == '5':
            sn.mutual_friends(input("User 1: ").strip(), input("User 2: ").strip())
        elif choice == '6':
            sn.suggested_friends(input("Enter user: ").strip())
        elif choice == '7':
            sn.remove_user(input("Enter user: ").strip())
        elif choice == '8':
            sn.remove_friendship(input("User 1: ").strip(), input("User 2: ").strip())
        elif choice == '9':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
