import sys
import json


TOOL_VERSION = '0.1.0'

if __name__ == "__main__":

    if sys.argv[1] == '--help':
        pass

    if sys.argv[1] == '--version':
        print(f'Migration Tool - version {TOOL_VERSION}')
