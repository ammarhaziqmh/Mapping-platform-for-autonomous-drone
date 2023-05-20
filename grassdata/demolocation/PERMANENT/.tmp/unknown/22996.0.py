#!/usr/bin/env python3

import grass.script as gs


def main():
    gs.run_command('g.region', flags='p')


if __name__ == '__main__':
    main()
