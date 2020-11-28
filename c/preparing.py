import sys
import os

if __name__ == '__main__':
    project_dir = sys.argv[1]
    output_path = os.path.join(project_dir, "c", "index.h")

    with open(output_path, "w") as f:
        f.write("const int kCMagicConst = 228;")
