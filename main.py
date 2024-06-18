import os

def display_menu():
  print("\n simpile to do list manager")
  print("1. View to do list ")
  print("2. Add task")
  print("3. Mark task as completed")
  print("4. Delete task")
  print("5. Exit")

def view_list():
  if os.path.exists('list.txt'):
    with open('list.txt', 'r')as f:
      to_list = f.readlines()
    if to_list:
      print("\n ___to do list___")
      for i, item in enumerate(to_list, start=1):
        print(f"{i}.{item.strip()}")

    else:
      print("\n your list is empty")

  else:
    print("\n your list is empty")

def add_task():
  task= input("Enter tak to add :")
  with open('list.txt', 'a') as f:
    f.write(task + '\n')

  print(f"\n Task {task} has been added to the list")

def mark_task():
  view_list()
  try:
    task_number = int(input("Enter the number of task to mark as completed:"))
    with open('list.txt', 'r') as f:
      lines = f.readlines()

    if 1<= task_number<= len(lines):
      completed_task = lines[task_number -1].strip()
      lines[task_number -1] = f"[x] {completed_task}\n"
      with open('list.txt','w') as f:
        f.writelines(lines)

      print(f"\n Task {completed_task} has been marked as completed")
    else:
      print("Invalid task number")

  except ValueError:
    print("Invalid input. Please enter a valid task number.")

def delet_task():
  view_list
  try:
    task_number= int(input("\nEnter the number of task to delete:" ))
    with open('list.txt','r') as f:
      lines = f.readlines()
    if 1<= task_number <= len(lines):
      del_task = lines[task_number -1].strip()
      del lines[task_number -1]
      with open('list.txt','w') as f:
        f.writelines(lines)
      print(f"Task {del_task} deleted from your list")

    else:
      print("Invalid task number")

  except ValueError:
    print("Invalid input. Please enter a valid number")

def main():
  while True:
    display_menu()
    choice = input("Enter your choice (1-5):")
    if choice == '1':
      view_list()
    elif choice == '2':
      add_task()
    elif choice== '3':
      mark_task()
    elif choice=='4':
      delet_task()
    elif choice =='5':
      print("\n Exiting program... ")
      break
  else:
    print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
  main()
