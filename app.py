import os
import platform
import json

PROGRAM_VERSION: str = 'None'

class Locale:

    def __init__(self):
        pass


class TranslationProject:

    def __init__(self, project_name: str, separator: str = '='):
        self.name = project_name
        self.locales = []

        project_path = os.path.join(os.getcwd(), 'project_locales', project_name)
        if os.path.exists(project_path):
            self._load()
        else:
            self.config = {
                'sep': separator,
                'program_version': PROGRAM_VERSION
            }

            os.mkdir(project_path)
            os.mkdir(os.path.join(project_path, 'locales'))

            cfg_file = open(os.path.join(project_path, 'project.json'), 'w+')
            cfg_file.write(json.dumps(self.config, indent=4))
            cfg_file.close()

    def add_locale(self, locale: Locale):
        self.locales.append(locale)

    def delete_locale(self, locale: Locale):
        self.locales.remove(locale)

    def _load(self):
        print('Загрузка проекта...')
        project_path = os.path.join(os.getcwd(), 'project_locales', self.name, 'project.json')
        with open(project_path, 'r+') as project_cfg:
            self.config = json.loads(project_cfg.read())

        print(self.config)



if __name__ == '__main__':

    path = os.path.join(os.getcwd(), 'package.json')
    with open(path, 'r+') as package_info:
        package = json.loads(package_info.read())
        PROGRAM_VERSION = package['program_version']

    print(f'Locale Creator\n'
          f'version: {PROGRAM_VERSION}\n')
    project = TranslationProject('test project')
