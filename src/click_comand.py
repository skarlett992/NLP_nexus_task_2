import json
import click
from src.face_detect import face_detect
from src.document_recognizer import get_text_from_document
from src.name_recognize import name_recognize
import os.path

@click.command()
@click.option('--input', type=click.Path(exists=True), help="input file")
@click.option('--verbose', type=click.BOOL, default=False, help="verbose mode ( output detailed logs )", required=False)
def get_params(input, verbose):
    click.echo(f'input: {input},verbose: {verbose}')
    face_detect(input)

    result_text = get_text_from_document(input)
    basic_info = name_recognize(result_text)

    data_set = {"basic_info": basic_info, "full_text": result_text}

    json_dump = json.dumps(data_set)

    output = 'output/output_text.txt'
    if len(result_text) > 0 and not os.path.isfile(output):
        with open(output, "w") as fd:
            fd.write(json_dump)
    print(f'file {output} created in output')

# TODO: добавить poetry
# TODO: добавить обработку verbose через default-ый getLogger
# TODO: добавить yapf и isort
# TODO: предусмотреть вариант, когда вводят pdf и jpg  еще нет (не сохранять отдельные jpg)
# TODO: предусмотреть аугментацию
# TODO: доработать распознавание ФИО, добавить распознавание пола и возраста, страны и тд
# TODO: добавить распознавание номера документа
# TODO: добавить постобработку


