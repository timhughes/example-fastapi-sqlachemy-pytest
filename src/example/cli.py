#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Tim Hughes <thughes@thegoldfish.org>
#
# Distributed under terms of the MIT license.


import argparse
import logging
import sys

import uvicorn
from example.main import app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(sys.argv[0])


def serve(args):
    logger.info(f"Running server {args}")
    uvicorn.run(app, host="0.0.0.0", port=8000)


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_server = subparsers.add_parser("serve", help="start the server")
    parser_server.add_argument("--config", help="path to configuration file")
    parser_server.set_defaults(func=serve)

    args = parser.parse_args()
    serve(args)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Exiting on KeyboardInterrupt")
    except Exception as exc:
        logger.info(f"Exiting on unknown error {exc}")
    finally:
        pass
