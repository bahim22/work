#! ./work/.venv/bin/python3

"""
"scripts installed into virtualenv have a “shebang” line which
points to the env Python interpreter, i.e. #!/<path-to-venv>/bin/python"

#! ~/flow/work/.venv/bin/python3
#! work/.venv/bin/python3
#! /home/ib-ub/flow/work/.venv/bin/python3
"""

SUFFIXES = {
    1000: [
        'KB', 'MB', 'GB', 'TB', 'PB'
    ],
    1024: [
        'KiB', 'MiB', 'GiB', 'TiB', 'PiB'
    ]
}


def approx_size(size, kb_is_1024_bytes=True):
    '''convert file size to human-readable, decimal form

    Keyword arguments:

    size -- file size in bytes
    kb_is_1024_bytes -- if True, use multiples of 1024
                        if False, use multiples of 1000

    Returns: string
'''
    if size < 0:
        raise ValueError('int must be non-zero')

    multiple = 1024 if kb_is_1024_bytes else 1000

    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('int too large')
