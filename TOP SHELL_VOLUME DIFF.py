import trimesh

original = trimesh.load(r"D:\SOFTAGE\4. TOP SHELL\INPUTS\RetroPad - Top Shell.stl")
generated = trimesh.load(r"D:\SOFTAGE\4. TOP SHELL\CODE\TOP SHELL.stl")

print("Original Volume:", original.volume)
print("Generated Volume:", generated.volume)

difference = abs(original.volume - generated.volume)

print("Volume Difference:", difference)
