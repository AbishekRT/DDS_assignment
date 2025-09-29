# Social Network Graph Analysis Console Application
# Author: [Your Name]
# Index: [Your Index Number]

import heapq

class SocialNetwork:
    def __init__(self):
        # Graph representation: user -> list of (friend, weight)
        self.graph = {}

    # Add a user
    def add_user(self, user):
        if user in self.graph:
            print("User already exists.")
        else:
            self.graph[user] = []
            print(f"User '{user}' added.")

    # Add friendship (undirected edge)
    def add_friendship(self, user1, user2, weight):
        if user1 not in self.graph or user2 not in self.graph:
            print("Both users must exist in the network.")
            return
        # Prevent duplicate friendships
        if any(friend == user2 for friend, _ in self.graph[user1]):
            print("Friendship already exists.")
            return
        self.graph[user1].append((user2, weight))
        self.graph[user2].append((user1, weight))
        print(f"Friendship added between {user1} and {user2} with interaction weight {weight}.")

    # Display network structure
    def view_network(self):
        print("\n--- Social Network Structure ---")
        print(f"Total users: {len(self.graph)}")
        total_connections = sum(len(friends) for friends in self.graph.values()) // 2
        print(f"Total friendship connections: {total_connections}")
        for user, friends in self.graph.items():
            friend_list = ', '.join([f"{f} (weight {w})" for f, w in friends])
            print(f"{user}: {friend_list if friend_list else 'No friends'}")

    # Dijkstra's algorithm for shortest path
    def shortest_path(self, start, end):
        if start not in self.graph or end not in self.graph:
            print("Both users must exist in the network.")
            return
        heap = [(0, start, [start])]  # (total_weight, current_user, path)
        visited = set()
        while heap:
            cost, node, path = heapq.heappop(heap)
            if node == end:
                print(f"Path from {start} to {end}: {' -> '.join(path)}")
                print(f"Total Interaction Cost: {cost}")
                return
            if node in visited:
                continue
            visited.add(node)
            for neighbor, weight in self.graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + weight, neighbor, path + [neighbor]))
        print(f"No path found between {start} and {end}.")

    # Mutual friends
    def mutual_friends(self, user1, user2):
        if user1 not in self.graph or user2 not in self.graph:
            print("Both users must exist in the network.")
            return
        friends1 = set(f for f, _ in self.graph[user1])
        friends2 = set(f for f, _ in self.graph[user2])
        mutual = friends1 & friends2
        print(f"Mutual friends between {user1} and {user2}: {', '.join(mutual) if mutual else 'None'}")

    # Suggested friends
    def suggested_friends(self, user):
        if user not in self.graph:
            print("User must exist in the network.")
            return
        user_friends = set(f for f, _ in self.graph[user])
        suggestions = {}
        for friend in user_friends:
            for friend_of_friend, _ in self.graph[friend]:
                if friend_of_friend != user and friend_of_friend not in user_friends:
                    suggestions[friend_of_friend] = suggestions.get(friend_of_friend, 0) + 1
        # Only suggest users with at least 2 mutual friends
        suggested = [u for u, count in suggestions.items() if count >= 2]
        print(f"Suggested friends for {user}: {', '.join(suggested) if suggested else 'None'}")

    # Remove a user
    def remove_user(self, user):
        if user not in self.graph:
            print("User not found.")
            return
        # Remove from all friends' lists
        for friend, _ in self.graph[user]:
            self.graph[friend] = [(f, w) for f, w in self.graph[friend] if f != user]
        del self.graph[user]
        print(f"User '{user}' removed along with all friendships.")

    # Remove a friendship
    def remove_friendship(self, user1, user2):
        if user1 not in self.graph or user2 not in self.graph:
            print("Both users must exist in the network.")
            return
        self.graph[user1] = [(f, w) for f, w in self.graph[user1] if f != user2]
        self.graph[user2] = [(f, w) for f, w in self.graph[user2] if f != user1]
        print(f"Friendship between {user1} and {user2} removed.")


# Menu-driven interface
def main():
    sn = SocialNetwork()
    while True:
        print("\n--- Social Network Console ---")
        print("1. Add User")
        print("2. Add Friendship")
        print("3. View Network Structure")
        print("4. Shortest Connection Path")
        print("5. Mutual Friends")
        print("6. Suggested Friends")
        print("7. Remove User")
        print("8. Remove Friendship")
        print("9. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            user = input("Enter user name/ID: ").strip()
            sn.add_user(user)
        elif choice == '2':
            u1 = input("Enter first user: ").strip()
            u2 = input("Enter second user: ").strip()
            print("Interaction strength options (1-5):")
            print("1: Very strong, 2: Strong, 3: Moderate, 4: Weak, 5: Very weak")
            weight = int(input("Enter weight: ").strip())
            sn.add_friendship(u1, u2, weight)
        elif choice == '3':
            sn.view_network()
        elif choice == '4':
            start = input("Enter start user: ").strip()
            end = input("Enter end user: ").strip()
            sn.shortest_path(start, end)
        elif choice == '5':
            u1 = input("Enter first user: ").strip()
            u2 = input("Enter second user: ").strip()
            sn.mutual_friends(u1, u2)
        elif choice == '6':
            user = input("Enter user for suggestions: ").strip()
            sn.suggested_friends(user)
        elif choice == '7':
            user = input("Enter user to remove: ").strip()
            sn.remove_user(user)
        elif choice == '8':
            u1 = input("Enter first user: ").strip()
            u2 = input("Enter second user: ").strip()
            sn.remove_friendship(u1, u2)
        elif choice == '9':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
