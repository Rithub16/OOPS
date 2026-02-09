class InstagramAccount:

    # Constructor
    def __init__(self, account_name, password):
        self.account_name = account_name # Public variable
        self._private_reels = [] # Protected variable
        self.__archived_reels = [] # Private variable
        self.__password = password # Private password

    # 1. Add private reel
    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)

    # 2. Display private reels
    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:", self._private_reels)
        else:
            print("Access Denied! Only followers can view private reels")

    # 3. Add archived reel
    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)

    # 4. Display archived reels
    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:", self.__archived_reels)
        else:
            print("Access Denied! Only account holder can view archived reels")

    # 5. Getter method for archived reels
    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied!"

    # 6. Setter method to update password
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully.")
        else:
            print("Incorrect old password. Cannot update password.")


# -------------------------------
# Task Implementation
# -------------------------------

# Create object
account = InstagramAccount("rithu_official", "1234")

# Add at least 2 private reels
account.add_private_reel("Goa Trip")
account.add_private_reel("Birthday Celebration")

# Add at least 2 archived reels
account.add_archived_reel("Old Dance Video")
account.add_archived_reel("College Memories")

print("\n--- Display Private Reels ---")
account.display_private_reels(True) # As follower
account.display_private_reels(False) # As non-follower

print("\n--- Display Archived Reels ---")
account.display_archived_reels("1234") # Correct password
account.display_archived_reels("0000") # Wrong password

print("\n--- Update Password ---")
account.set_password("1234", "5678")

print("\n--- Check With New Password ---")
account.display_archived_reels("5678")