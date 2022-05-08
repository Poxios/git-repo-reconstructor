import os

f_original = open("folder_list_want_to_be_in_subfolder.csv", 'r')
f_target = open("target_folder_names.csv", 'r')
f_secrets = open("secrets.txt", 'r')

target_lines = ''.join(f_target.readlines()).split('\n')
original_lines = ''.join(f_original.readlines()).split('\n')

original_folder_db = []
for line in original_lines:
    num, folder_name = line.split(',')
    original_folder_db.append((num,folder_name))

    
target_folder_db = []
for line in target_lines:
    num, folder_name = line.split(',')
    target_folder_db.append((num,folder_name))

# Change cmd dir to working dir
os.chdir(f_secrets.readline())

for target_idx, folder_name in original_folder_db:
    os.system(f"git filter-repo --path-rename \"{folder_name}:{target_folder_db[int(target_idx)][1]}/{folder_name}\" --force")
    #print(f"git filter-repo --path-rename '{folder_name}':'{target_folder_db[int(target_idx)][1]}/{folder_name}' --force")

f_original.close()
f_target.close()

