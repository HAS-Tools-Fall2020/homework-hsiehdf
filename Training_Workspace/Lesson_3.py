# %%
months= ["J","F","M"]
avg_monthly_precip = [12,13,14]
files = [months, avg_monthly_precip]

for fnames in files:
    print ("The value of the variable 'fnames' is:", len(fnames))


# %%
%%time
for_list = []
for i in range (50000):
    for_list.append (i*i)

# %%
%%time  
comp_list=[[i*i in range(50000)]]
# %%
my_path=os.path.join("homework-hsiehdf-git" , "Training_Workspace")
os.path.exists(my_path)

# %%
print(os.getcwd())
filepath=os.path.join("Training_Workspace","lesson_3.py")
print(filepath)

# %%
os.chdir("homework-hsiehdf-git")
# %%
