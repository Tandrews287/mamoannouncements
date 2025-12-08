#!/usr/bin/env python3
"""
Command-line interface for Mamo Announcements
"""

import argparse
import sys
from announcements import AnnouncementManager


def format_announcement(announcement):
    """Format an announcement for display."""
    print(f"\n{'='*60}")
    print(f"ID: {announcement['id']}")
    print(f"Title: {announcement['title']}")
    print(f"Priority: {announcement['priority']}")
    print(f"Created: {announcement['created_at']}")
    print(f"Updated: {announcement['updated_at']}")
    print(f"\nContent:")
    print(announcement['content'])
    print(f"{'='*60}\n")


def list_announcements(args):
    """List all announcements."""
    manager = AnnouncementManager()
    announcements = manager.get_all_announcements()
    
    if not announcements:
        print("No announcements found.")
        return
    
    if args.priority:
        announcements = [a for a in announcements if a['priority'] == args.priority]
    
    print(f"\nFound {len(announcements)} announcement(s):\n")
    for announcement in announcements:
        print(f"[{announcement['id']}] [{announcement['priority'].upper()}] {announcement['title']}")
        print(f"    Created: {announcement['created_at']}")


def create_announcement(args):
    """Create a new announcement."""
    manager = AnnouncementManager()
    announcement = manager.create_announcement(
        title=args.title,
        content=args.content,
        priority=args.priority
    )
    print(f"\n✓ Announcement created successfully with ID: {announcement['id']}")
    format_announcement(announcement)


def view_announcement(args):
    """View a specific announcement."""
    manager = AnnouncementManager()
    announcement = manager.get_announcement(args.id)
    
    if announcement:
        format_announcement(announcement)
    else:
        print(f"Announcement with ID {args.id} not found.")
        sys.exit(1)


def update_announcement(args):
    """Update an existing announcement."""
    manager = AnnouncementManager()
    announcement = manager.update_announcement(
        announcement_id=args.id,
        title=args.title,
        content=args.content,
        priority=args.priority
    )
    
    if announcement:
        print(f"\n✓ Announcement {args.id} updated successfully")
        format_announcement(announcement)
    else:
        print(f"Announcement with ID {args.id} not found.")
        sys.exit(1)


def delete_announcement(args):
    """Delete an announcement."""
    manager = AnnouncementManager()
    
    if not args.force:
        response = input(f"Are you sure you want to delete announcement {args.id}? (y/n): ")
        if response.lower() != 'y':
            print("Deletion cancelled.")
            return
    
    if manager.delete_announcement(args.id):
        print(f"\n✓ Announcement {args.id} deleted successfully")
    else:
        print(f"Announcement with ID {args.id} not found.")
        sys.exit(1)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Mamo Announcements - Manage announcements from the command line",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List all announcements')
    list_parser.add_argument('--priority', choices=['low', 'normal', 'high'],
                           help='Filter by priority')
    list_parser.set_defaults(func=list_announcements)
    
    # Create command
    create_parser = subparsers.add_parser('create', help='Create a new announcement')
    create_parser.add_argument('title', help='Title of the announcement')
    create_parser.add_argument('content', help='Content of the announcement')
    create_parser.add_argument('--priority', choices=['low', 'normal', 'high'],
                              default='normal', help='Priority level (default: normal)')
    create_parser.set_defaults(func=create_announcement)
    
    # View command
    view_parser = subparsers.add_parser('view', help='View a specific announcement')
    view_parser.add_argument('id', type=int, help='ID of the announcement')
    view_parser.set_defaults(func=view_announcement)
    
    # Update command
    update_parser = subparsers.add_parser('update', help='Update an announcement')
    update_parser.add_argument('id', type=int, help='ID of the announcement')
    update_parser.add_argument('--title', help='New title')
    update_parser.add_argument('--content', help='New content')
    update_parser.add_argument('--priority', choices=['low', 'normal', 'high'],
                              help='New priority')
    update_parser.set_defaults(func=update_announcement)
    
    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete an announcement')
    delete_parser.add_argument('id', type=int, help='ID of the announcement')
    delete_parser.add_argument('--force', action='store_true',
                              help='Skip confirmation prompt')
    delete_parser.set_defaults(func=delete_announcement)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    args.func(args)


if __name__ == '__main__':
    main()
