# dictionary of all commands in Git with their main role. If th user inputs one command name, he should get an explanation of its function
dictionary = {
    "commit": "capture the state of the project at that time and transfered to local repos ",
    "fetch": "download contents from a remote repository in order to update the local repository ",
    "push": "transfer local changes to a remote repository",
    "clone": "make a copy of the main branch project in order to work paralelly on different parts/modifications",
    "pull_request": "ask for integrating branche-changes in the main branch",
    "pull": "retrieve changes from remote repository and intergrates them in the local version",
    "merge": "a process for bringing separate developments(branches) together again in ther main branch ",
}
user_input = input("what would you like to have explained ? ")
print(f"the functionality of {user_input} is : {dictionary[user_input]}")

if user_input not in dictionary:
    print(f"I cannot tell you anything about {user_input}! ")
else:
    print(f"enter a new question ")
