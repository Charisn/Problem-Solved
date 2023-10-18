import os
import pandas as pd

def load_rename_dict_from_excel(file_path):
    df = pd.read_excel(file_path)
    
    return dict(zip(df["ΒΟΗΘΗΤΙΚΟΣ ΚΩΔΙΚΟΣ"], df["ΚΩΔΙΚΟΣ EPSILON"]))

def rename_images_based_on_excel(paths, rename_dict):
    for path in paths:
        if not os.path.exists(path):
            print(f"Directory {path} does not exist. Skipping...")
            continue

        for filename in os.listdir(path):
            
            base_name, _ = os.path.splitext(filename)
            
            if base_name in rename_dict:
                new_name = rename_dict[base_name]
                
                if pd.isna(new_name):
                    print(f"Skipping {filename} as corresponding value is NaN.")
                    continue
                
                new_filename = new_name + "-01-Προτεινόμενο.png"
                
                os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
                print(f"Renamed {filename} to {new_filename}")
            else:
                print(f"File {filename} not found in Excel.")

rename_dict = load_rename_dict_from_excel("C:\\Users\\Charis\\Desktop\\upload.xlsx")

paths = ["C:\\Users\\Charis\\Desktop\\file01", "C:\\Users\\Charis\\Desktop\\file02"]

rename_images_based_on_excel(paths, rename_dict)
