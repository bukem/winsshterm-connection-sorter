# WinSSHTerm Connection Sorter

A Python utility for sorting connections in WinSSH Term configuration files.

## Description

WinSSHTerm Connection Sorter is a simple command-line tool that helps organize your WinSSHTerm connections by sorting them alphabetically while maintaining their hierarchical structure. The tool sorts nodes in the connections.xml file according to the following rules:

1. Container nodes come before Connection nodes
2. Within each type (Container or Connection), nodes are sorted alphabetically by name
3. The hierarchical structure is preserved during sorting
