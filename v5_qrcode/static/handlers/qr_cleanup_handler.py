import glob, os

def clear_output_folder(app):
    output_dir = app.config["OUTPUT_FOLDER"]
    for file_path in glob.glob(os.path.join(output_dir, "*")):
        try:
            os.remove(file_path)
        except Exception as e:
            app.logger.warning(f"Could not delete {file_path}: {e}")
