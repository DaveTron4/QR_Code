import os
import stat
import shutil

def clear_output_folder(app, user_folder_path):
    if os.path.exists(user_folder_path):
        try:
            def remove_readonly(func, path, excinfo):
                os.chmod(path, stat.S_IWRITE)
                func(path)
            
            shutil.rmtree(user_folder_path, onerror=remove_readonly)
            app.logger.info(f"Deleted folder: {user_folder_path}")
        except Exception as e:
            app.logger.warning(f"Could not delete {user_folder_path}: {e}")
    else:
        app.logger.warning(f"Folder {user_folder_path} does not exist.")
