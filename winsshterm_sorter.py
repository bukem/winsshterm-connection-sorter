#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import xml.etree.ElementTree as ET
import shutil
from datetime import datetime

def sort_nodes(node):
    """
    Recursively sort nodes in the XML tree.
    First by Type (Container first, then Connection), then by Name alphabetically.
    """
    # Get all child nodes
    children = list(node)
    
    # Sort children by Type and then by Name
    children.sort(key=lambda x: (
        # Type="Container" comes first, Type="Connection" comes second
        0 if x.get('Type') == 'Container' else 1,
        # Then sort by Name attribute alphabetically
        x.get('Name', '').lower()
    ))
    
    # Clear the parent node and add sorted children back
    for child in list(node):
        node.remove(child)
    
    for child in children:
        node.append(child)
        # Recursively sort children of this node if it's a Container
        if child.get('Type') == 'Container':
            sort_nodes(child)

def sort_connections_file(file_path):
    """
    Sort connections in the Win SSH Term configuration file.
    """
    try:
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # Create backup
        backup_path = create_backup(file_path)
        print(f"Backup created: {backup_path}")
        
        # Sort all nodes under the root
        sort_nodes(root)
        
        # Write the sorted XML back to the file
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
        print(f"Connections sorted successfully in {file_path}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def create_backup(file_path):
    """
    Create a backup of the original file with timestamp.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_dir = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    backup_name = f"{os.path.splitext(file_name)[0]}_backup_{timestamp}{os.path.splitext(file_name)[1]}"
    backup_path = os.path.join(file_dir, backup_name)
    
    shutil.copy2(file_path, backup_path)
    return backup_path

def main():
    """
    Main function to handle command line arguments and execute sorting.
    """
    if len(sys.argv) != 2:
        print("Usage: python sort_connections.py <path_to_connections_file>")
        return
    
    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        return
    
    if not file_path.lower().endswith('.xml'):
        print("Error: File must be an XML file.")
        return
    
    sort_connections_file(file_path)

if __name__ == "__main__":
    main()
