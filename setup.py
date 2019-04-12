from cx_Freeze import setup, Executable
  
executables = [Executable('pong_main.py', 
               targetName = 'Pong.exe', 
               base = 'Win32GUI', 
               icon = 'sprites/pong.ico',
               shortcutName='Pong Game',
               shortcutDir='DesktopFolder')]

excludes = ['unicodedata', 'logging', 'unittest', 'email', 'html', 'http', 'urllib', 'bz2']

zip_include_packages = ['collections', 'encodings', 'importlib', 'pygame', 'random', 'os', 'wx']

includes = ['pygame', 'random', 'os']

include_files = ['sound', 'sprites', '__init__.py',
                 'background.py', 'ball.py', 'func_preview.py', 
                 'rackets.py', 'score.py', 'sound.py']

options = {
      'build_exe':{
            'include_msvcr': True,
            'excludes': excludes,
            'includes': includes,
            'include_files': include_files,
            'zip_include_packages': zip_include_packages,
      }
}

setup(name = 'Pong',
      version = '0.0.1',
      description = 'Pong Game',
      executables = executables,
      options = options)