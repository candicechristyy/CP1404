import datetime
from project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"

def main():
    filename = 'projects.txt'
    projects = load_projects(filename)

    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} from projects.txt")
    print(MENU)
    choice = input(">>> ").strip().lower()

    while choice != 'q':

        if choice == 'l':
            filename = input("Filename: ")
            projects = load_projects(filename)

        elif choice == 's':
            with open('projects_save.txt', 'w') as out_file:
                print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n", file=out_file)
                for project in projects:
                    print(f"{project.name}\t{project.start_date.strftime("%d/%m/%Y")}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)

        elif choice == 'd':
            sorted_projects = sorted(projects)
            incomplete_projects = [project for project in sorted_projects if not project.is_complete()]
            completed_projects = [project for project in sorted_projects if project.is_complete()]

            print("Incomplete projects:")
            for project in incomplete_projects:
                print(project)

            print("Complete projects:")
            for project in completed_projects:
                print(project)

        elif choice == 'f':
            date = input("Show projects that start after date (dd/mm/yy): ")
            filter_date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
            projects_with_filtered_date = sorted([project for project in projects if project.start_date >= filter_date])

            for project in projects_with_filtered_date:
                print(project)

        elif choice == 'a':
            print("Let's add a new project")
            new_name = input("Name: ")
            new_start_date = input("Start date (dd/mm/yy): ")
            new_priority = input("Priority: ")
            new_cost_estimate = input("Cost estimate: $")
            new_percent_completed = input("Percent complete: ")
            new_project = Project(new_name, new_start_date, new_priority, new_cost_estimate, new_percent_completed)
            projects.append(new_project)

        elif choice == 'u':
            for i in range(len(projects)):
                print(f"{i} {projects[i]}")

            project_update_choice = int(input("Project choice: "))
            print(projects[project_update_choice])

            updated_percentage = input("New Percentage: ")
            projects[project_update_choice].completion_percentage = int(updated_percentage)

            updated_priority = input("New Priority: ")
            if updated_priority != '':
                projects[project_update_choice].priority = int(updated_priority)

        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").strip().lower()

    save_choice = input("Would you like to save to projects.txt? ").lower()
    if save_choice == 'yes' or save_choice == 'y':
        with open('projects_save.txt', 'w') as out_file:
            print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
            for project in projects:
                print(
                    f"{project.name}\t{project.start_date.strftime("%d/%m/%Y")}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
                    file=out_file)

    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)
    return projects


main()
