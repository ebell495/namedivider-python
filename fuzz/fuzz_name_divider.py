#!/usr/local/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from namedivider import NameDivider 


@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    name = fdp.ConsumeString(len(data))
    if len(name) > 2:
        divided_name = NameDivider().divide_name(name)
        divided_name.to_dict()


# atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()