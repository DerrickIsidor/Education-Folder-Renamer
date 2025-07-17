# Education Folder Renamer

A personal file management script that automatically renames and organizes academic course folders using consistent Information Architecture (IA) principles.

## Project Overview

As a student and aspiring data professional, I realized my `Education` folder was full of inconsistently named course folders. This made it difficult to locate materials and prepare for archiving. So I created this Python tool to automate folder naming based on a scalable structure:  
`[Year]_[Semester]_[Course_Name]`

## Information Architecture Concepts Used

- **Labeling**: Clear, descriptive, and uniform folder names
- **Classification**: Terms grouped by year and semester
- **Hierarchy**: Courses organized chronologically
- **Metadata**: Naming conventions act as implicit metadata for course content

## Features

- Automatically renames folders based on a predefined mapping
- Prints a log of renamed, skipped, and failed folders
- Easy to extend with new course names
- Optional to turn into a GUI or web-based tool in the future

## Technologies

- Python 3
- Standard Libraries: `os`, `try/except`, and custom `dict` logic
- File system operations (cross-platform support possible)


