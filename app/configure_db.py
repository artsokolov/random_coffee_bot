import logging
import time

from db import engine, Base

from sqlalchemy import text, Engine
from sqlalchemy.orm import Session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

WAIT_IN_SECONDS = 3
MAX_TRIES = 60 * WAIT_IN_SECONDS # 3 minutes


def check_database(db_engine: Engine):
    current_tries = 0
    connection_established = False
    while current_tries < MAX_TRIES and not connection_established:
        try:
            with db_engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            connection_established = True
        except Exception as e:
            logger.error(e)

        current_tries += 1
        time.sleep(WAIT_IN_SECONDS)


def main():
    logger.info("Checking database connection.")
    check_database(engine)

    # logger.info("Running migrations")
    # metadata.create_all(engine)


main()
