import argparse
import logging
from utils import setup_logging
from agent import train

def main():
    try:
        parser = argparse.ArgumentParser(description="Snake AI Training")
        parser.add_argument('--train', action='store_true', help="Run training mode")
        args = parser.parse_args()

        logger = setup_logging()
        logger.info("Snake AI application started")

        if args.train:
            train()
        else:
            logger.info("Please specify a mode with --train")
    except Exception as e:
        logging.error(f"Error in main: {e}")
        raise

if __name__ == '__main__':
    main()