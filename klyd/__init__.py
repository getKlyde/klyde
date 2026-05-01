import sys

frame = sys._getframe()
while frame:
    if frame.f_code.co_name == '_get_module_details' and frame.f_locals.get('mod_name') == 'klyd.__main__':
        from klyd.cli import cli
        sys.argv[0] = 'python -m klyd'
        cli()
        sys.exit(0)
    frame = frame.f_back
