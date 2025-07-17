# File management System Libraries
import os

# key for renaming folders: {'old_name': 'new_name'}
"""
for this project I will be using [Term]_[Year]_[Course] format
Example: 2024_Spring_Intro_to_Data_Science

This allows me to chronologically  sort my classes for easy reading. 

"""
def load_rename_key():
    return {
        'Spring 24 Intro to Data Science' : '2024_Spring_Intro_to_Data_Science',
        'AMH' : '2022_Spring_Modern_American_History', 
        'cgs 1000' : '2022_Spring_Intro_to_Computers_and_Technology',
        'Chem FA21' : '2021_Fall_Intro_Chemestry_Lecture',
        'cHEM lAB' : '2021_Fall_Intro_Chemestry_Lab',
        'Coursera Statistics' : '2022_Summer_Coursera_Statistics',
        'Data & Text Mining' : '2024_Fall_Data_and_Text_Mining',
        'Data Science Club 2023' : '2023_Spring_Data_Science_Club',
        'Database Concepts fa 23' : '2023_Fall_Database_Concepts',
        'ENGLISH 2' : '2021_Spring_English_Comp_2',
        'Fall_2022_Programming_in_C' : '2022_Fall_Programming_in_C',
        'Fall_2023_IT_Concepts' : '2023_Fall_IT_Concepts',
        'Fall_2024_R_Programming' : '2024_Fall_R_Programming',
        'Fundemental Physics Lab' : '2021_Fall_Fundemental_Physics_Lab',
        'Info Behaviors summer 24' : '2024_Summer_Information_Behaviors',
        'intro to enviromental science spring 23' : '2023_Spring_Intro_To_Environmental_Science',
        'Intro to info Science FA23' : '2023_Fall_Intro_To_Info_Science',
        'Java Programming fall 22' : '2022_Fall_Java_Programming',
        'Phylosophy' : '2022_Spring_Philosophy',
        'Professional Writing FA 23' : '2023_Fall_Professional_Writing',
        'Psychology' : '2021_Summer_Psychology',
        'Public Speaker' : '2021_Summer_Public_Speaking',
        'SLS' : '2020_Spring_First_Year_Experiece',
        'Spring 25 Information Ethics and Policy' : '2025_Spring_Information_Ethics_and_Policy',
        'Spring_22_Ethics' : '2022_Spring_Ethics',
        'Spring_23_IDS' : '2023_Spring_IDS_Connections',
        'Spring_23_Physics_1_Lab' : '2023_Spring_Physics_1_Lab',
        'Spring_23_Physics_1_Lecture' : '2023_Spring_Physics_1_Lecture',
        'Spring_24_Intro_to_Data_Science' : '2024_Spring_Intro_to_Data_Science',
        'Spring_25_Predicitve_Analytics' : '2025_Spring_Predicitve_Analytics',
        'STATS Fa 22' : '2022_Fall_Intro_Statistics',
        'Summer 25 Information Literacy' : '2025_Summer_Information_Literacy',
        'Summer 25 Intro to Python' : '2025_Summer_Intro_to_Python',
        'Summer_25_Information_Architecture' : '2025_Summer_Information_Architecture',
        'Summer_2022_Programing_Logic' : '2022_Summer_Programing_Logic',
        'Visual Analytics Fall 24' : '2024_Fall_Visual_Analytics',
        'FA_23_Professional_Writing' : '2023_Fall_Professional_Writing',
        'Advanced Stats and Analysis Spring 24' : '2024_Spring_Advanced_Statistics_and_Analysis',
        '2021 Spring First Year Experiece' : '2021_Spring_First_Year_Experiece'
    }

# Code for renaming folders
class EducationFolderManager:
    def __init__(self, folder_map, base_path):
        self.folder_map = folder_map
        self.base_path = base_path

    def rename_folders(self):
        for folder_name in os.listdir(self.base_path):
            full_path = os.path.join(self.base_path, folder_name)
            if os.path.isdir(full_path):
                new_name = self.folder_map.get(folder_name)
                if new_name:
                    new_full_path = os.path.join(self.base_path, new_name)
                    try:
                        os.rename(full_path, new_full_path)
                        print(f"Renamed: '{folder_name}' -> '{new_name}'")
                    except Exception as e:
                        print(f"Failed to rename '{folder_name}': {e}")
                else:
                    print(f"Skipped: '{folder_name}' (no matching key)")

# Running the function
def main():
    education_folder_path = r"C:\\Users\\FTP\\Desktop\\Education"
    folder_map = load_rename_key()
    manager = EducationFolderManager(folder_map, education_folder_path)
    manager.rename_folders()

if __name__ == "__main__":
    main()
