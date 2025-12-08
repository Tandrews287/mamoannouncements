#!/usr/bin/env python3
"""
Mamo Announcements - A simple announcement management system
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class AnnouncementManager:
    """Manages announcements with CRUD operations."""
    
    def __init__(self, data_file: str = "announcements.json"):
        """
        Initialize the announcement manager.
        
        Args:
            data_file: Path to the JSON file for storing announcements
        """
        self.data_file = data_file
        self.announcements = self._load_announcements()
    
    def _load_announcements(self) -> List[Dict]:
        """Load announcements from the data file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def _save_announcements(self) -> None:
        """Save announcements to the data file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.announcements, f, indent=2)
    
    def create_announcement(self, title: str, content: str, priority: str = "normal") -> Dict:
        """
        Create a new announcement.
        
        Args:
            title: Title of the announcement
            content: Content/body of the announcement
            priority: Priority level (low, normal, high)
        
        Returns:
            The created announcement
        """
        announcement_id = len(self.announcements) + 1
        announcement = {
            "id": announcement_id,
            "title": title,
            "content": content,
            "priority": priority,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        self.announcements.append(announcement)
        self._save_announcements()
        return announcement
    
    def get_all_announcements(self) -> List[Dict]:
        """Get all announcements."""
        return self.announcements
    
    def get_announcement(self, announcement_id: int) -> Optional[Dict]:
        """
        Get a specific announcement by ID.
        
        Args:
            announcement_id: ID of the announcement
        
        Returns:
            The announcement if found, None otherwise
        """
        for announcement in self.announcements:
            if announcement["id"] == announcement_id:
                return announcement
        return None
    
    def update_announcement(self, announcement_id: int, title: Optional[str] = None,
                          content: Optional[str] = None, priority: Optional[str] = None) -> Optional[Dict]:
        """
        Update an existing announcement.
        
        Args:
            announcement_id: ID of the announcement to update
            title: New title (if provided)
            content: New content (if provided)
            priority: New priority (if provided)
        
        Returns:
            The updated announcement if found, None otherwise
        """
        for announcement in self.announcements:
            if announcement["id"] == announcement_id:
                if title is not None:
                    announcement["title"] = title
                if content is not None:
                    announcement["content"] = content
                if priority is not None:
                    announcement["priority"] = priority
                announcement["updated_at"] = datetime.now().isoformat()
                self._save_announcements()
                return announcement
        return None
    
    def delete_announcement(self, announcement_id: int) -> bool:
        """
        Delete an announcement.
        
        Args:
            announcement_id: ID of the announcement to delete
        
        Returns:
            True if deleted successfully, False otherwise
        """
        for i, announcement in enumerate(self.announcements):
            if announcement["id"] == announcement_id:
                self.announcements.pop(i)
                self._save_announcements()
                return True
        return False
    
    def get_announcements_by_priority(self, priority: str) -> List[Dict]:
        """
        Get announcements filtered by priority.
        
        Args:
            priority: Priority level to filter by
        
        Returns:
            List of announcements with the specified priority
        """
        return [a for a in self.announcements if a["priority"] == priority]
