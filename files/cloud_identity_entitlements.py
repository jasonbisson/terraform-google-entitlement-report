import argparse
import os
from googleapiclient.discovery import build

def get_arguments():
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(
        description='Google Customer ID')
    parser.add_argument(
        "--customer_id", help="Google Customer ID. C123abcde", required=True)
    args = parser.parse_args()
    return (args)

def main():
    args = get_arguments()
    service = build("admin", "directory_v1")
    results = service.groups().list(customer=args.customer_id).execute()
    groups = results.get("groups",)

    if not groups:
        print("No groups in the domain.")
    else:
        print("Group,Member")
        for group in groups:
            try:
                members_result = service.members().list(groupKey=group['id']).execute()
                members = members_result.get('members',)
                if not members:
                    print(f"{group.get('name', 'No Name')},No Members")
                else:
                    for member in members:
                        member_email = member.get('email', 'No Email')
                        print(f"{group.get('name', 'No Name')},{member_email}")
            except Exception as e:
                print(f"Error listing members for group {group['email']}: {e}")

if __name__ == "__main__":
    main()