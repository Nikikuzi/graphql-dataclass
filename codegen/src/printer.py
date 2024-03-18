import pathlib
from os.path import join

from clean_py.clean_py import clean_python_code

from .utils import get_valid_folder, to_snake_case, to_camel_case
from .consts import PY_EXTENSION, TYPE_REFS_NAME, ENUMS_NAME, MUTATIONS_NAME, QUERIES_NAME, SCALARS_NAME, \
    SIMPLE_TYPES_NAME, TEMPLATE_FOLDER, TYPES_NAME, UNIONS_NAME, FORWARD_REFERENCE_NAME, FORWARD_REFERENCE_SIGNATURE, \
    INIT_FILE, INDENTED_IMPORT_SIGNATURE, IMPORT_SIGNATURE
import os
import logging as logger
from .enums import TemplateType
from .priority import ExtractionResults

class Printer():

    extractionResults: ExtractionResults

    def __init__(self, extractionResults) -> None:
        self.extraction_results = extractionResults

    def save_files(self, folder: str, clean_folder: bool, create_forward_reference: bool):
        try:
            if folder:
                folder = get_valid_folder(folder)
            else:
                logger.warning('Destination folder missing')
            self.__initialize(folder, clean_folder)
            self.save_file(TemplateType.SCALAR_TEMPLATE, str(pathlib.Path(folder, SCALARS_NAME + PY_EXTENSION).absolute()), 'scalar_defs', folder)
            self.save_file(TemplateType.ENUM_TEMPLATE, str(pathlib.Path(folder, ENUMS_NAME + PY_EXTENSION).absolute()), 'enum_classes', folder)
            self.save_file(TemplateType.FREE_TYPE_TEMPLATE, str(pathlib.Path(folder, SIMPLE_TYPES_NAME + PY_EXTENSION).absolute()), 'simple_type_classes', folder)
            self.save_file(TemplateType.TYPE_TEMPLATE, str(pathlib.Path(folder, TYPES_NAME + PY_EXTENSION).absolute()), 'type_classes', folder)
            self.save_operation_file(TemplateType.QUERY_TEMPLATE, str(pathlib.Path(folder, QUERIES_NAME + PY_EXTENSION).absolute()), ('query_classes', 'queries_enum_class'))
            self.save_operation_file(TemplateType.MUTATION_TEMPLATE, str(pathlib.Path(folder, MUTATIONS_NAME + PY_EXTENSION).absolute()), ('mutation_classes', 'mutations_enum_class'))
            self.save_file(TemplateType.TYPE_REFS_TEMPLATE, str(pathlib.Path(folder, TYPE_REFS_NAME + PY_EXTENSION).absolute()), 'type_refs', folder)
            self.__save_forward_reference(folder, create_forward_reference)
            self.__clean_code(folder)
        except Exception as ex:
            raise ex

    def save_file(self, enum_template, file_name, attr_name_result, folder):
        """For internal use"""
        try:
            if len(getattr(self.extraction_results, attr_name_result).values()) > 0:
                with open(file_name, 'w', encoding='UTF-8') as wrapper:
                    wrapper.write(self.load_template_code(enum_template.value))
                    wrapper.write('\n')
                    self.__print_imports(enum_template, wrapper)
                    for name, curr_class in getattr(self.extraction_results, attr_name_result).items():
                        if enum_template == TemplateType.TYPE_TEMPLATE:
                            if name in self.extraction_results.unions:
                                continue
                            if self.extraction_results.circular.get(name) is None:
                                self.write_class_code(curr_class, wrapper)
                            else:
                                self.__write_circular_class_code(name, curr_class, folder)
                        else:
                            self.write_class_code(curr_class, wrapper)
                    if enum_template == TemplateType.TYPE_TEMPLATE:
                        self.__write_unions(getattr(self.extraction_results, attr_name_result), folder)
        except Exception as ex:
            raise ex

    def save_operation_file(self, enum_template, file_name, attr_name_results):
        """For internal use"""
        try:
            if not getattr(self.extraction_results, attr_name_results[0]): return

            with open(file_name, 'w', encoding='UTF-8') as wrapper:
                wrapper.write(self.load_template_code(enum_template.value))
                wrapper.write('\n')
                for curr_class in getattr(self.extraction_results, attr_name_results[0]).values():
                    self.write_class_code(curr_class, wrapper)
                if getattr(self.extraction_results, attr_name_results[0]):
                    wrapper.write('\n')
                    for queriesEnum in getattr(self.extraction_results, attr_name_results[1]).values():
                        self.write_class_code(queriesEnum, wrapper)
        except Exception as ex:
            raise ex

    def write_class_code(self, classCode, wrapper):
        """For internal use"""
        try:
            wrapper.write('\n\n')
            wrapper.writelines("%s\n"  % i for i in classCode)
        except Exception as ex:
            raise ex

    def load_template_code(self, templateName):
        """For internal use"""
        try:
            fileName = os.path.join(get_valid_folder(TEMPLATE_FOLDER), templateName)
            with(templateFile := open(fileName)):
                return templateFile.read()
        except Exception as ex:
            raise ex

    def __write_circular_class_code(self, name, class_lines, folder):
        with open(str(pathlib.Path(folder, to_snake_case(name) + PY_EXTENSION).absolute()), 'w', encoding='UTF-8') as wrapper:
            wrapper.write(self.load_template_code(TemplateType.CIRCULAR_CLASS_TEMPLATE.value))
            wrapper.write("\n")
            self.__print_imports(TemplateType.CIRCULAR_CLASS_TEMPLATE, wrapper, name)
            self.write_class_code(class_lines, wrapper)

    def __clean_code(self, folder):
        for name in os.listdir(folder):
            # Open file
            with open(os.path.join(folder, name)) as f:
                fixed_file = clean_python_code(f.read())
            with open(os.path.join(folder, name), 'w') as f:
                f.write(fixed_file)

    def __save_forward_reference(self, folder, create_forward_reference: bool):
        if create_forward_reference:
            with open(str(pathlib.Path(folder, FORWARD_REFERENCE_NAME + PY_EXTENSION).absolute()), 'w', encoding='UTF-8') as wrapper:
                self.__print_imports(TemplateType.FORWARD_REFERENCE_TEMPLATE, wrapper)
                res = ','.join(f"'{to_camel_case(tp)}':{to_camel_case(tp)}" for tp in self.extraction_results.type_classes.keys())
                wrapper.write(FORWARD_REFERENCE_SIGNATURE%res)

    def __initialize(self, folder, clean_folder: bool):
        if clean_folder:
            files = os.listdir(folder)
            for f in files:
                os.remove(join(folder, f))
        with open(join(folder, INIT_FILE), "w") as f:
            f.write("")

    def __write_unions(self, types, folder):
        with open(str(pathlib.Path(folder, UNIONS_NAME + PY_EXTENSION).absolute()), 'w', encoding='UTF-8') as wrapper:
            wrapper.write(self.load_template_code(TemplateType.UNION_TEMPLATE.value))
            wrapper.write('\n')
            self.__print_imports(TemplateType.UNION_TEMPLATE, wrapper)
            for name, type_data in types.items():
                if name in self.extraction_results.unions:
                    self.write_class_code(type_data, wrapper)

    def __print_imports(self, enum_template, wrapper, name=None):
        if enum_template not in [TemplateType.SCALAR_TEMPLATE, TemplateType.ENUM_TEMPLATE]:
            if enum_template != TemplateType.FREE_TYPE_TEMPLATE:
                for key in self.extraction_results.circular.keys():
                    if key != name:
                        if enum_template not in (TemplateType.UNION_TEMPLATE, TemplateType.FORWARD_REFERENCE_TEMPLATE):
                            wrapper.write(INDENTED_IMPORT_SIGNATURE%(to_snake_case(key), to_camel_case(key)))
                        else:
                            wrapper.write(IMPORT_SIGNATURE%(to_snake_case(key), to_camel_case(key)))
                if enum_template != TemplateType.TYPE_TEMPLATE:
                    for key in self.extraction_results.type_classes.keys():
                        if self.extraction_results.circular.get(to_camel_case(key)) is None:
                            if enum_template not in (TemplateType.UNION_TEMPLATE, TemplateType.FORWARD_REFERENCE_TEMPLATE):
                                wrapper.write(INDENTED_IMPORT_SIGNATURE%(TYPES_NAME if key not in self.extraction_results.unions else UNIONS_NAME, to_camel_case(key)))
                            elif enum_template == TemplateType.UNION_TEMPLATE and key not in self.extraction_results.unions:
                                wrapper.write(IMPORT_SIGNATURE%(TYPES_NAME, to_camel_case(key)))
                            elif enum_template != TemplateType.UNION_TEMPLATE:
                                wrapper.write(
                                    IMPORT_SIGNATURE%(TYPES_NAME if key not in self.extraction_results.unions else UNIONS_NAME, to_camel_case(key)))
                if enum_template == TemplateType.TYPE_TEMPLATE:
                    for key in self.extraction_results.type_classes.keys():
                        if key in self.extraction_results.unions:
                            wrapper.write(INDENTED_IMPORT_SIGNATURE%(UNIONS_NAME, to_camel_case(key)))
            for key in self.extraction_results.enum_classes.keys():
                wrapper.write(IMPORT_SIGNATURE%(ENUMS_NAME, to_camel_case(key)))

            for key in self.extraction_results.scalar_defs.keys():
                wrapper.write(IMPORT_SIGNATURE%(SCALARS_NAME, key))
            if enum_template != enum_template.FREE_TYPE_TEMPLATE:
                for key in self.extraction_results.simple_type_classes.keys():
                    wrapper.write(IMPORT_SIGNATURE%(SIMPLE_TYPES_NAME, to_camel_case(key)))