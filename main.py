import os

chosen_folder = input("Enter path to folder: ")
solution_name = input("Enter the container name: ")
list_of_libraries = []


def extract_line_import(line_text):
    return_line = ""
    if line_text.startswith("import"):
        if ' as ' in line_text:
            return_line = line_text[0:line_text.index(' as ')].lstrip('import').strip()
        else:
            return_line = line_text.lstrip('import').strip()
    elif line_text.startswith("from"):
        return_line = line_text[0:line_text.index(' import ')].lstrip('from').strip()
    return return_line.split(".")[0]


if __name__ == "__main__":
    py_files = []
    for filename in os.listdir(chosen_folder):
        if filename.endswith('py'):
            py_files.append(filename)
            with open(os.path.join(chosen_folder, filename), 'r', errors="ignore") as f:
                for line in f.readlines():
                    # print(line)
                    if 'import' in line:
                        candidate = extract_line_import(line.strip().rstrip('\n'))
                        if len(candidate) > 0:
                            list_of_libraries.append(candidate)

    # make Dockerfile
    f = open(os.path.join(chosen_folder, "Dockerfile"), "w")
    f.write("FROM python:3\n")
    f.write("COPY .  /usr/src.app\n")
    f.write("WORKDIR /usr/src.app\n")
    install_string = 'RUN pip3 install'
    for library in list_of_libraries:
        install_string += ' ' + library
    f.write(install_string + '\n')
    cmd_string = 'CMD [ "python", "./' + py_files[0] + '" ]'
    f.write(cmd_string + '\n')

    # make batch file to build and run
    f = open(os.path.join(chosen_folder, "build_and_run.cmd"), "w")
    f.write("docker build -t " + solution_name + " .\n")
    f.write("docker run " + solution_name + "\n")
