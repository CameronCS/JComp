from JPack.file_sys import get_file, get_package

__package__ = "JPack"
__name__    = "jfile_content.py"
__version__ = "1.1.0.0"
__all__     = ["generate_main", "generate_app", "generate_test", "generate_file"]

def generate_main() -> list[str]:
    return [
        "class Main {\n",
        "\tpublic static void main(String[] args) {\n",
        "\t\tApp app = new App();\n",
        "\t\tapp.runApp();\n",
        "\t}\n",
        "}\n"
    ]

def generate_app() -> list[str]:
    return [
        "public class App {\n",
        "\tpublic App() {\n",
        "\t\tthis.InitiliseApp();\n",
        "\t}\n",
        "\tprivate void InitiliseApp() {\n",
        "\t\t/**\n",
        "\t\t * This is the code block where you\n",
        "\t\t * will initilise anything needed in your app\n",
        "\t\t */\n",
        "\t}\n",
        "\n",
        "\tpublic void runApp() {\n",
        "\t\t/**\n",
        "\t\t * This is where your main run app methods\n",
        "\t\t * will be called or where you will write\n",
        "\t\t * the code to run the app\n",
        "\t\t */\n",
        "\t}\n",
        "}\n"
    ]

def generate_test() -> list[str]: 
    return [
        "class test {\n",
        "\tpublic static void main(String[] args) {\n",
        "\t\t/**\n",
        "\t\t * You can call methods from this point on to run tests\n"
        "\t\t */\n"
        "\t}\n",
        "}\n"
    ]

def generate_file(file: str) -> list[str]:
    _file = get_file(file)

    isPack = file.__contains__("/") or file.__contains__("\\")
    if isPack: package = get_package(file)

    classname = _file.removesuffix(".java")

    return [
        f"package {package};\n\n" if isPack else "",
        f"public class {classname} {'{'}\n",
        "\n",
        f"\tpublic {classname}() {'{'}\n",
        "\t\t/**\n",
        "\t\t * Insert code here\n",
        "\t\t */\n",
        "\t}\n",
        "}\n"
    ]