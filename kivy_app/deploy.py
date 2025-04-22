import os

print("=== Deploy Automático Git ===")
msg = input("deploy automatico raul: ")

# Adiciona tudo
os.system("git add -A")

# Faz o commit
os.system(f'git commit -m "{msg}"')

# Dá push
os.system("git push")
